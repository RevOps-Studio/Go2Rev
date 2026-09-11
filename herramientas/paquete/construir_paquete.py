"""Distribuye fuentes generales actuales; no aplica la metodología."""
from pathlib import Path
from urllib.parse import unquote
import hashlib
import json
import os
import re
import zipfile

ROOT = Path(__file__).resolve().parents[2]
PACKAGE = ROOT / 'producto/paquete_fundacional/v0.2'
MANIFEST = PACKAGE / 'manifiesto.json'
INVENTORY = PACKAGE / 'INVENTARIO.md'
COMPONENTS = [
    ('Arquitectura', '0.2', 'producto/arquitectura/v0.2'),
    ('Encargo y conocimiento', '0.1', 'producto/metodo/encargo_y_conocimiento/v0.1'),
    ('Investigación y Diagnostic', '0.2', 'producto/metodo/investigacion_y_diagnostic/v0.2'),
    ('Oferta entrega y economía', '0.1', 'producto/metodo/oferta_entrega_y_economia/v0.1'),
    ('Posicionamiento demanda y conversión', '0.1', 'producto/metodo/posicionamiento_demanda_y_conversion/v0.1'),
    ('Medición preparación y transferencia', '0.1', 'producto/metodo/medicion_preparacion_y_transferencia/v0.1'),
    ('Operación conversacional', '0.2', 'producto/metodo/operacion_conversacional/v0.2'),
    ('Paquete fundacional', '0.2', 'producto/paquete_fundacional/v0.2'),
]
TOOL_FILES = [
    'herramientas/documentos/LEEME.md',
    'herramientas/documentos/construir_lectura.py',
    'herramientas/documentos/renderizar_word.ps1',
    'herramientas/documentos/renderizar_paginas.py',
    'herramientas/modelo_economico/LEEME.md',
    'herramientas/modelo_economico/construir_modelo.mjs',
    'herramientas/paquete/LEEME.md',
    'herramientas/paquete/construir_paquete.py',
    'herramientas/paquete/construir_lecturas.py',
]
START = '# Go2Rev Base fundacional 0.2\n\nAbrir el [paquete y guía de implementación](producto/paquete_fundacional/v0.2/LEEME.md). La base está construida y conserva su estado teórico. La primera aplicación y sus comprobaciones requieren un ámbito autorizado.\n\nLa carpeta producto contiene las fuentes, plantillas vacías, libro editable y vistas de lectura. Herramientas contiene los generadores opcionales; no hace falta ejecutarlos para leer o utilizar el método. El inventario y manifiesto están junto a la guía del paquete.\n'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def role(path):
    if '/plantillas/' in path:
        return 'Plantilla vacía'
    if path.endswith('.docx'):
        return 'Vista de lectura derivada'
    if path.endswith('.xlsx'):
        return 'Modelo editable vacío'
    if path.endswith('definicion_modelo.mjs'):
        return 'Definición editable del modelo'
    if path.endswith('manifiesto.json'):
        return 'Inventario de integridad'
    if path.endswith('INVENTARIO.md'):
        return 'Índice derivado de archivos'
    if '/lecturas/' in path:
        return 'Compilación derivada por tarea'
    if path.endswith('.zip'):
        return 'Estructura documental vacía'
    if path.endswith('rutas_de_lectura.json'):
        return 'Localizadores para compilar lecturas'
    if path.startswith('herramientas/'):
        return 'Herramienta documental opcional'
    return 'Instrucción o especificación metodológica'


def main():
    paths = {}
    for label, version, directory in COMPONENTS:
        base = ROOT / directory
        if not base.is_dir():
            raise FileNotFoundError(directory)
        for p in sorted(base.rglob('*')):
            if p.is_file():
                if p.is_symlink() or p.suffix not in {'.md', '.mjs', '.xlsx', '.docx', '.json', '.zip'}:
                    raise ValueError(f'Archivo no previsto: {p}')
                p.resolve().relative_to(ROOT)
                paths[p.relative_to(ROOT).as_posix()] = (label, version)
    for name in TOOL_FILES:
        if not (ROOT / name).is_file():
            raise FileNotFoundError(name)
        paths[name] = ('Herramientas documentales', 'conjunto 0.2')
    for p in [INVENTORY, MANIFEST]:
        paths[p.relative_to(ROOT).as_posix()] = ('Paquete fundacional', '0.2')
    lines = ['# Inventario de la distribución', '', 'Conjunto fundacional 0.2 · 11 de septiembre de 2026', '',
             f'La distribución contiene {len(paths) + 1} archivos: los enumerados aquí y la entrada INICIO.md situada en la raíz del ZIP. El manifiesto incluye la huella de todos salvo la suya propia. Este índice es un derivado de rutas y funciones; no es un maestro ni un resultado de aplicación.', '',
             'Las versiones base se fijan con la revisión de integración del conjunto 0.2. El manifiesto distingue el contenido exacto tras las correcciones editoriales. Las vistas derivadas y herramientas están identificadas como tales.', '']
    labels = [c[0] for c in COMPONENTS] + ['Herramientas documentales']
    for label in labels:
        lines += ['## ' + label, '', '| Archivo | Función | Versión base |', '|---|---|---|']
        for name, (group, version) in sorted(paths.items()):
            if group == label:
                target = os.path.relpath(ROOT / name, PACKAGE).replace('\\', '/')
                lines.append(f'| [{name}]({target}) | {role(name)} | {version} |')
        lines.append('')
    INVENTORY.write_text('\n'.join(lines), encoding='utf-8', newline='\n')
    content = {name: (ROOT / name).read_bytes() for name in paths if ROOT / name != MANIFEST}
    content['INICIO.md'] = START.encode('utf-8')
    entries = []
    for name, data in sorted(content.items()):
        group, version = paths.get(name, ('Entrada de distribución', '0.2'))
        entries.append({'ruta': name, 'componente': group, 'version_base': version,
                        'funcion': 'Entrada derivada' if name == 'INICIO.md' else role(name),
                        'bytes': len(data), 'sha256': sha(data)})
    manifest = {'producto': 'Go2Rev', 'version_conjunto': '0.2', 'fecha': '2026-09-11',
                'estado': 'Construcción cerrada; base teórica sin pruebas de la metodología',
                'revision_integracion': 'Puesta en marcha 2026-09-11',
                'entrada': 'INICIO.md', 'archivos_totales': len(content) + 1,
                'exclusion_de_huella': MANIFEST.relative_to(ROOT).as_posix(), 'archivos': entries}
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
    content[MANIFEST.relative_to(ROOT).as_posix()] = MANIFEST.read_bytes()
    # Resolver enlaces de texto dentro de la distribución, sin abrir el archivo histórico.
    for name, data in content.items():
        if not name.endswith('.md'):
            continue
        for target in re.findall(r'\]\(([^\n]+?)\)', data.decode('utf-8-sig')):
            target = unquote(target.strip('<>').split('#')[0])
            if not target or re.match(r'^[A-Za-z]+://', target):
                continue
            resolved = os.path.normpath(os.path.join(os.path.dirname(name), target)).replace('\\', '/')
            if resolved not in content:
                raise ValueError(f'Enlace fuera del paquete o ausente: {name}: {target}')
    output = ROOT / 'entregables'
    output.mkdir(exist_ok=True)
    dest = output / 'Go2Rev_fundacional_v0.2.zip'
    with zipfile.ZipFile(dest, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for name, data in sorted(content.items()):
            info = zipfile.ZipInfo(name, date_time=(2026, 9, 11, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, data)
    with zipfile.ZipFile(dest) as z:
        if z.testzip() is not None or set(z.namelist()) != set(content):
            raise ValueError('Distribución incompleta')
        for entry in entries:
            if sha(z.read(entry['ruta'])) != entry['sha256']:
                raise ValueError('Contenido de distribución no coincide')
    (output / 'Go2Rev_fundacional_v0.2.sha256').write_text(sha(dest.read_bytes()) + '  ' + dest.name + '\n', encoding='utf-8', newline='\n')
    print(json.dumps({'archivos': len(content), 'huellas': len(entries), 'zip': str(dest)}, ensure_ascii=True))


if __name__ == '__main__':
    main()
