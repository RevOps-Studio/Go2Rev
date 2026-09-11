"""Genera ayudas de lectura y estructura vacía desde fuentes actuales del producto."""
from pathlib import Path
from urllib.parse import unquote
import hashlib
import json
import os
import re
import zipfile

ROOT = Path(__file__).resolve().parents[2]
OP = ROOT / 'producto/metodo/operacion_conversacional/v0.2'
PACKAGE = ROOT / 'producto/paquete_fundacional/v0.3'
OUT = PACKAGE / 'lecturas'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write(path, text):
    path.write_text(text.rstrip() + '\n', encoding='utf-8', newline='\n')


def source(name):
    path = (ROOT / name).resolve()
    path.relative_to(ROOT / 'producto')
    if not path.is_file() or path.is_symlink():
        raise ValueError(f'Fuente ausente o no admisible: {name}')
    return path


def bundle(name, title, paths, first=''):
    paths = list(dict.fromkeys(p.resolve() for p in paths))
    aliases = {p: 'fuente-' + str(i + 1) for i, p in enumerate(paths)}
    extra = set()
    def links(text, base):
        def link(m):
            label, target = m.groups()
            if re.match(r'^[a-z]+://', target):
                return m.group(0)
            rel, _, fragment = unquote(target.strip('<>')).partition('#')
            path = (base.parent / rel).resolve() if rel else base.resolve()
            if path in aliases:
                return f'[{label}](#{aliases[path]})'
            if path != ROOT / 'herramientas/modelo_economico/LEEME.md':
                path.relative_to(ROOT / 'producto')
            if not path.is_file():
                raise FileNotFoundError(f'{base}: {target}')
            extra.add(path.relative_to(ROOT).as_posix())
            return label + ' (archivo adicional: ' + path.relative_to(ROOT).as_posix() + (('#' + fragment) if fragment else '') + ')'
        return re.sub(r'\[([^\]]+)\]\(([^\n]+?)\)', link, text)
    blocks = []
    if first:
        blocks += [links(first, OP / '10_primera_pasada.md')]
    for p in paths:
        raw = p.read_bytes()
        blocks += [f'<a id="{aliases[p]}"></a>\n\n## Fuente: {p.relative_to(ROOT).as_posix()}\n\nSHA256: {sha(raw)}\n\n' + links(raw.decode('utf-8-sig'), p)]
    header = f'# {title}\n\nConjunto 0.3 · Compilación derivada; editar los originales identificados, no esta lectura.\n\nLeer la entrada común CARGA_INICIO junto a la tarea. Esta carga reúne instrucción, contrato y recursos de la capacidad. Un enlace a un archivo adicional no acredita su lectura. Abrirlo cuando su condición o dependencia sea necesaria; si no está disponible, delimitar el uso dependiente.\n\n'
    if extra:
        header += '## Archivos adicionales localizables\n\n' + '\n'.join('- ' + s for s in sorted(extra)) + '\n\n'
    write(OUT / name, header + '\n\n'.join(blocks))


def main():
    OUT.mkdir(exist_ok=True)
    routes = json.loads((OP / 'rutas_de_lectura.json').read_text(encoding='utf-8'))
    rows = routes['nodos']
    if [r['nodo'] for r in rows] != [f'N{i:02d}' for i in range(1, 18)]:
        raise ValueError('Mapa de diecisiete nodos incompleto')
    common = ['ENTRADA_GO2REV.md', '00_glosario.md', '08_carpetas_y_guardado.md', '12_nucleo_y_suficiencia.md', '05_continuidad_y_cambios.md', 'plantillas/04_indice_del_encargo.md']
    bundle('CARGA_INICIO.md', 'Go2Rev · Entrada y continuidad', [OP / p for p in common])
    first = (OP / '10_primera_pasada.md').read_text(encoding='utf-8')
    for row in rows:
        paths = [source(row['instruccion']), source(row['contrato_archivo'])]
        paths += [source(p) for p in row['plantillas']]
        # Auxiliares de análisis por capacidad; no lectura recursiva de todo el método.
        family = paths[0].parent
        if row['nodo'] in ['N03','N04','N05','N06']:
            paths += [family / p for p in ['01_investigacion_y_suficiencia.md','08_investigacion_externa_y_contraste.md','09_rutina_de_fuentes_y_acceso.md','10_catalogo_inicial_de_fuentes.md']]
        if row['nodo'] in ['N08','N11','N12']:
            paths += [family / p for p in ['04_formulas_y_dominio.md','05_variantes_de_oferta_y_operacion.md','06_comparacion_y_umbrales.md','08_guia_del_modelo.md']]
        if row['nodo'] in ['N07','N09','N10']:
            paths += [family / p for p in ['04_costes_cohortes_y_capacidad.md','05_variantes_y_traspasos.md']]
        match = re.search(r'^## ' + row['nodo'] + r'\b.*?(?=^## N\d\d\b|\Z)', first, re.M | re.S)
        if not match:
            raise ValueError('Primera pasada ausente: ' + row['nodo'])
        bundle('CARGA_' + row['nodo'] + '.md', 'Go2Rev · ' + row['titulo'], paths, match.group(0))
    folders = ['00 Sistema', '01 Entregables', '01 Entregables/Diagnostic', '01 Entregables/Design', '01 Entregables/Economia', '01 Entregables/Despliegue', '02 Anexos', '02 Anexos/Material del cliente', '02 Anexos/Investigacion externa', '02 Anexos/Actas y transcripciones', '03 QA', '04 Archivo', '05 Operacion']
    items = {p + '/': b'' for p in folders}
    items['00 Sistema/Indice del encargo.md'] = (OP / 'plantillas/04_indice_del_encargo.md').read_bytes()
    items['INICIO.md'] = ('# Estructura vacía del encargo\n\nExtraer dentro de la raíz acordada de un nuevo encargo, separada de la biblioteca Go2Rev. Si existe trabajo previo, recuperar su índice y conciliar la correspondencia de carpetas antes de incorporar esta estructura; no sobrescribir archivos existentes.\n\nCompletar el índice cuando exista mandato y contenido. Crear Fuentes y Lectura en los conjuntos de Entregables y en Operacion al producir la primera pieza de ese tipo. Seguir carpetas y guardado en el paquete Go2Rev 0.3. Esta estructura contiene instrucciones y campos vacíos.\n').encode('utf-8')
    with zipfile.ZipFile(PACKAGE / 'Go2Rev_estructura_vacia_v0.3.zip', 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for name, data in sorted(items.items()):
            info = zipfile.ZipInfo(name, (2026, 9, 11, 0, 0, 0))
            info.create_system = 3
            info.external_attr = (0o40755 if name.endswith('/') else 0o100644) << 16
            if name.endswith('/'): info.external_attr |= 0x10
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, data)
    print(json.dumps({'lecturas': 18, 'carpetas': len(folders), 'datos_empresariales': False}))


if __name__ == '__main__':
    main()
