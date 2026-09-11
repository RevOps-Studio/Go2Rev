"""Genera vistas vacías e índices desde la definición documental, sin aplicar Go2Rev."""
from pathlib import Path
import hashlib
import json
import os
import re

ROOT = Path(__file__).resolve().parents[2]
OP = ROOT / 'producto/metodo/operacion_conversacional/v0.3'
SOURCE = ROOT / 'producto/metodo/esquema/v0.1/plantillas.json'


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value.rstrip() + '\n', encoding='utf-8', newline='\n')


def relative(path, base):
    return os.path.relpath(path, base.parent).replace('\\', '/')


def load():
    data = json.loads(SOURCE.read_text(encoding='utf-8'))
    routes = json.loads((OP / 'rutas_de_lectura.json').read_text(encoding='utf-8'))
    ids, paths = set(), set()
    for doc in data['documentos']:
        target = (ROOT / doc['ruta']).resolve()
        target.relative_to(ROOT / 'producto/metodo')
        if target.is_symlink() or '/plantillas/' not in doc['ruta'] or target in paths:
            raise ValueError('Destino de plantilla no admisible: ' + doc['ruta'])
        paths.add(target)
        for item in [doc] + [b for b in doc['partes'] if b['tipo'] != 'texto']:
            for record in [item] + item.get('campos', []):
                if record['id'] in ids:
                    raise ValueError('Identidad repetida: ' + record['id'])
                ids.add(record['id'])
        for b in doc['partes']:
            if b['tipo'] == 'campos' and b['columnas'] != ['Campo', 'Regla', 'Valor']:
                raise ValueError('Tabla de campos no reconocida')
            if b['tipo'] == 'matriz':
                if any(len(row) != len(b['columnas']) for row in b['filas']):
                    raise ValueError('Matriz irregular: ' + b['id'])
                # Las matrices vacías pueden tener etiquetas metodológicas en la primera columna.
                if any(any(row[1:]) for row in b['filas']):
                    raise ValueError('Valor no vacío en matriz: ' + b['id'])
    if len(paths) != 37 or [r['nodo'] for r in routes['nodos']] != [f'N{i:02d}' for i in range(1, 18)]:
        raise ValueError('Cobertura de formatos o nodos incompleta')
    required = {ROOT/p for r in routes['nodos'] for p in r['plantillas']}
    if not required <= paths:
        raise ValueError('Plantilla del mapa sin definición')
    for row in routes['nodos']:
        principal = [d for d in data['documentos'] if d['ruta'] == row['plantilla_principal']]
        if (len(principal) != 1 or not principal[0]['plantilla_principal'] or
                principal[0]['productor'] != row['nodo'] or principal[0]['contrato'] != row['contrato'] or
                row['plantilla_principal'] not in row['plantillas']):
            raise ValueError('Interfaz y plantilla principal no coinciden: ' + row['nodo'])
        cited = set(re.findall(r'K\d\d\.T\d\d\.B\d\d(?:\.F\d\d)?', procedure(row)))
        if not cited <= ids:
            raise ValueError('Referencia a campo o bloque ausente: ' + row['nodo'])
    return data, routes


def render(doc, data):
    path = ROOT / doc['ruta']
    result = []
    for part in doc['partes']:
        if part['tipo'] == 'texto':
            result += part['lineas']
            continue
        result += [f'<a id="{part["id"].lower().replace(".", "-")}"></a>', '',
                   f'<!-- bloque: {part["id"]} -->']
        rows = [part['columnas'], part['separador']]
        if part['tipo'] == 'campos':
            rows += [[('★ ' if f['nucleo'] else '') + f['etiqueta'], f['regla'], ''] for f in part['campos']]
        else:
            rows += part['filas']
        for i, row in enumerate(rows):
            result.append('|' + '|'.join(row) + '|' if i == 1 else '| ' + ' | '.join(row) + ' |')
    note = ('\nVista generada · Corregir la [definición de campos](' + relative(SOURCE, path) +
            '), no esta vista. ★ = campo de la plantilla principal: aplicar condición y momento; las piezas auxiliares pueden ser indispensables. ' +
            'Cabecera: ' + ', '.join(data['cabecera']['campos']) + '. ' + data['cabecera']['regla'] + '\n')
    result.insert(1, note)
    return '\n'.join(result)


def procedure(row):
    raw = (ROOT / row['instruccion']).read_text(encoding='utf-8')
    match = re.search(r'<!-- procedimiento:inicio -->\n(.*?)<!-- procedimiento:fin -->', raw, re.S)
    if not match:
        raise ValueError('Procedimiento breve ausente: ' + row['nodo'])
    return match.group(1).strip()


def header(row):
    return (f'## {row["nodo"]} · {row["titulo"]}\n\n**Entrada:** {row["entrada"]}\n\n'
            f'**Salida:** {row["contrato"]}; consumo por ' + (', '.join(row['consumidores']) or 'receptor y continuidad del encargo') +
            f'.\n\n**Cierre:** {row["cierre"]}\n\n**Destino:** {row["destino"]}. Mantener fuente, vista e índice.\n')


def json_schema(row, documents, data):
    blocks = {}
    for doc in documents:
        for b in doc['partes']:
            if b['tipo'] == 'texto':
                continue
            desc = b['titulo'] + '. ' + b['aplicabilidad']
            if b['tipo'] == 'campos':
                props = {f['id']: {'type': ['string', 'null'], 'title': f['etiqueta'], 'description': f['regla']} for f in b['campos']}
                item = {'type': 'object', 'additionalProperties': False, 'properties': props}
            else:
                item = {'type': 'object', 'additionalProperties': False,
                        'properties': {c: {'type': ['string', 'null']} for c in b['columnas']}}
            blocks[b['id']] = {'type': 'array', 'description': desc, 'items': item}
    return {'$schema': 'https://json-schema.org/draft/2020-12/schema',
            'title': 'Representación documental opcional de ' + row['contrato'],
            '$comment': 'Valida únicamente estructura de una exportación textual. No valida suficiencia, exigibilidad condicional, verdad, permisos ni aceptación. Las colecciones permiten bloques repetibles. No obliga a operar Go2Rev en JSON.',
            'type': 'object', 'additionalProperties': False,
            'properties': {'cabecera': {'type': 'object', 'additionalProperties': False,
                'properties': {c: {'type': ['string', 'null']} for c in data['cabecera']['campos']}},
                'bloques': {'type': 'object', 'additionalProperties': False, 'properties': blocks}},
            'required': ['cabecera', 'bloques']}


def main():
    data, routes = load()
    for doc in data['documentos']:
        write(ROOT / doc['ruta'], render(doc, data))
    first = ['# Primera pasada y núcleo por resultado', '', 'Versión 0.3 · Vista generada de rutas, procedimientos y definición de campos.', '',
             'Editar los pasos en la instrucción sustantiva, las interfaces en rutas_de_lectura.json y los campos en esquema/v0.1/plantillas.json. ' + data['regla_de_nucleo'], '']
    for row in routes['nodos']:
        first += [f'<a id="{row["nodo"].lower()}"></a>', '', header(row)]
        doc = next(d for d in data['documentos'] if d['ruta'] == row['plantilla_principal'])
        first += ['**Núcleo localizado en la plantilla principal:**']
        for b in doc['partes']:
            if b['tipo'] != 'texto':
                anchor=b['id'].lower().replace('.', '-')
                first += [f'- [{b["titulo"] or "Campos del resultado"}]({relative(ROOT/doc["ruta"], OP/"10_primera_pasada.md")}#{anchor}) · {b["id"]}']
        first += ['', f'[Pasos e instrucción]({relative(ROOT/row["instruccion"], OP/"10_primera_pasada.md")}) · [Contrato completo]({relative(ROOT/row["contrato_archivo"], OP/"10_primera_pasada.md")})', '']
        selected = [d for d in data['documentos'] if d['ruta'] in row['plantillas']]
        schema = json_schema(row, selected, data)
        write(SOURCE.parent/'json_schema'/f'{row["contrato"]}.schema.json', json.dumps(schema, ensure_ascii=False, indent=2))
    write(OP/'10_primera_pasada.md', '\n'.join(first))
    print(json.dumps({'plantillas':len(data['documentos']), 'schemas_estructurales':17,
                      'definicion_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest()}))


if __name__ == '__main__':
    main()
