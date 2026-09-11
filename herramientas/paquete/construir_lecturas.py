"""Compila lecturas escalonadas; controla carga documental, no suficiencia metodológica."""
from pathlib import Path
from urllib.parse import unquote
import hashlib
import json
import os
import re
import zipfile
from construir_plantillas import load, procedure, header

ROOT = Path(__file__).resolve().parents[2]
OP = ROOT / 'producto/metodo/operacion_conversacional/v0.3'
PACKAGE = ROOT / 'producto/paquete_fundacional/v0.5'
OUT = PACKAGE / 'lecturas'


def write(path, text):
    path.write_text(text.rstrip() + '\n', encoding='utf-8', newline='\n')


def source(name):
    path = (ROOT / name).resolve()
    path.relative_to(ROOT / 'producto')
    if not path.is_file() or path.is_symlink():
        raise ValueError('Fuente ausente o no admisible: ' + name)
    return path


def anchor(path):
    return 'fuente-' + hashlib.sha256(path.relative_to(ROOT).as_posix().encode()).hexdigest()[:12]


def links(text, base):
    def convert(m):
        label, target = m.groups()
        if re.match(r'^[a-z]+://', target) or target.startswith('#'):
            return m.group(0)
        rel, _, fragment = unquote(target.strip('<>')).partition('#')
        path = (base.parent / rel).resolve()
        path.relative_to(ROOT)
        if not path.is_file():
            raise FileNotFoundError(f'{base}: {target}')
        dest = os.path.relpath(path, OUT).replace('\\', '/')
        return f'[{label}]({dest}' + (('#' + fragment) if fragment else '') + ')'
    return re.sub(r'\[([^\]]+)\]\(([^\n]+?)\)', convert, text)


def include(path, content=None, scope='archivo íntegro'):
    raw = path.read_bytes()
    text = raw.decode('utf-8-sig') if content is None else content
    sha = hashlib.sha256(raw).hexdigest()
    return (f'<a id="{anchor(path)}"></a>\n\n## Fuente: {path.name}\n\n'
            f'Procedencia: `{path.relative_to(ROOT).as_posix()}` · SHA256 `{sha}` · Incluye: {scope}.\n\n' + links(text, path))


def main():
    OUT.mkdir(exist_ok=True)
    _, routes = load()
    limits = routes['presupuesto_palabras']
    outputs = {}
    preamble = ('Conjunto 0.5 · Compilación derivada, no fuente editable. El contenido expresamente incluido sustituye la apertura del original metodológico de esa versión; una sección no sustituye el resto del archivo. Las fuentes del encargo y del mercado requieren lectura efectiva.\n\n')
    common = ['ENTRADA_GO2REV.md', '13_invariantes.md', '12_nucleo_y_suficiencia.md', 'plantillas/04_indice_del_encargo.md']
    outputs['CARGA_INICIO.md'] = '# Go2Rev · Entrada común\n\n' + preamble + '\n\n'.join(include(OP / p) for p in common)
    stats = {'entrada': len((OP/'ENTRADA_GO2REV.md').read_text(encoding='utf-8').split()),
             'comun': len(outputs['CARGA_INICIO.md'].split()), 'nodos': []}
    for row in routes['nodos']:
        n=row['nodo']; extension=f'CARGA_{n}_extension.md'
        table = ['## Ampliar según la tarea', '', 'Abrir las secciones indicadas antes del uso dependiente; conservar el resto localizable.', '', '| Condición | Lectura y sección |', '|---|---|']
        for item in row['extensiones']:
            p=source(item['ruta'])
            table.append(f'| {item["cuando"]} | [{p.stem}]({extension}#{anchor(p)}): {item["seccion"]} |')
        core = '# Go2Rev · ' + n + ' · Lectura inicial\n\n' + preamble + header(row) + '\n'
        core += include(source(row['instruccion']), procedure(row), 'sección Procedimiento de primera pasada íntegra')
        core += '\n\n' + include(source(row['plantilla_principal'])) + '\n\n' + '\n'.join(table)
        outputs[f'CARGA_{n}.md']=core
        unique = list(dict.fromkeys(item['ruta'] for item in row['extensiones']))
        outputs[extension] = (f'# Go2Rev · {n} · Extensión por pregunta\n\n' + preamble +
                              'Esta colección conserva archivos completos. Usar el índice de condiciones de la carga inicial y leer las secciones pertinentes; su presencia no acredita que se hayan consumido.\n\n' +
                              '\n\n'.join(include(source(p)) for p in unique))
        count=len(core.split())
        stats['nodos'].append({'nodo':n,'nucleo':count,'comun_mas_nodo':stats['comun']+count,'extension':len(outputs[extension].split())})
    errors=[]
    if stats['entrada']>limits['entrada']: errors.append('Entrada')
    if stats['comun']>limits['comun']: errors.append('Común')
    for item in stats['nodos']:
        if item['nucleo']>limits['nodo'] or item['comun_mas_nodo']>limits['comun_mas_nodo']: errors.append(item['nodo'])
    if errors:
        raise ValueError('Presupuesto documental superado: '+', '.join(errors)+'\n'+json.dumps(stats,ensure_ascii=False))
    for name, value in outputs.items(): write(OUT/name,value)
    stats['medida']='Palabras separadas por espacio, incluidos encabezados, tablas y localizadores; no mide tokens, tiempo ni calidad de aplicación.'
    stats['limites']=limits
    write(OUT/'carga_documental.json',json.dumps(stats,ensure_ascii=False,indent=2))
    folders=['00 Sistema','01 Entregables','01 Entregables/Diagnostic','01 Entregables/Design','01 Entregables/Economia','01 Entregables/Despliegue','02 Anexos','02 Anexos/Material del cliente','02 Anexos/Investigacion externa','02 Anexos/Actas y transcripciones','03 QA','04 Archivo','05 Operacion']
    items={p+'/':b'' for p in folders}
    # La copia de encargo conserva campos e instrucciones de guardado, sin enlaces al árbol de la biblioteca.
    index=(OP/'plantillas/04_indice_del_encargo.md').read_text(encoding='utf-8')
    index=re.sub(r'\[([^\]]+)\]\([^)]+\)',r'\1 (en la biblioteca Go2Rev)',index)
    items['00 Sistema/Indice del encargo.md']=index.encode('utf-8')
    items['INICIO.md']=('# Estructura vacía del encargo\n\nExtraer dentro de la raíz acordada, separada de la biblioteca Go2Rev. Recuperar el índice si existe trabajo previo y conciliar las rutas antes de incorporar esta estructura; conservar los archivos existentes.\n\nCompletar el índice cuando exista mandato y contenido. Crear Fuentes y Lectura al producir la primera pieza de ese tipo. Seguir carpetas y guardado del conjunto 0.5.\n').encode('utf-8')
    with zipfile.ZipFile(PACKAGE/'Go2Rev_estructura_vacia_v0.5.zip','w',compression=zipfile.ZIP_DEFLATED) as z:
        for name,value in sorted(items.items()):
            info=zipfile.ZipInfo(name,(2026,9,11,0,0,0));info.create_system=3
            info.external_attr=(0o40755 if name.endswith('/') else 0o100644)<<16
            if name.endswith('/'):info.external_attr|=0x10
            info.compress_type=zipfile.ZIP_DEFLATED;z.writestr(info,value)
    print(json.dumps(stats,ensure_ascii=True))


if __name__=='__main__':
    main()
