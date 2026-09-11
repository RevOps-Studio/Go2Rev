"""Convierte un DOCX a PDF con LibreOffice instalado; independiente del constructor."""
from pathlib import Path
import argparse
import os
import shutil
import subprocess
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('entrada', type=Path)
    parser.add_argument('salida', type=Path, help='Archivo PDF de destino')
    parser.add_argument('--soffice', help='Ruta al ejecutable si no está en PATH')
    args = parser.parse_args()
    source, target = args.entrada.resolve(), args.salida.resolve()
    if not source.is_file() or source.suffix.lower() != '.docx' or target.suffix.lower() != '.pdf':
        parser.error('Se requieren un DOCX existente y un destino PDF.')
    executable = args.soffice or shutil.which('soffice') or shutil.which('libreoffice')
    if not executable:
        parser.error('LibreOffice no está disponible. Instalarlo mediante el procedimiento del entorno o indicar --soffice; la generación DOCX es independiente.')
    target.parent.mkdir(parents=True, exist_ok=True)
    # El perfil y la conversión se aíslan: un PDF antiguo no puede pasar por un resultado nuevo.
    with tempfile.TemporaryDirectory(prefix='go2rev-render-') as folder:
        work = Path(folder)
        command = [executable, '-env:UserInstallation=' + (work/'perfil').as_uri(),
                   '--headless', '--convert-to', 'pdf:writer_pdf_Export', '--outdir', str(work), str(source)]
        options = {'creationflags': subprocess.CREATE_NO_WINDOW} if os.name == 'nt' else {}
        result = subprocess.run(command, capture_output=True, text=True, timeout=120, **options)
        produced = work / (source.stem + '.pdf')
        if result.returncode or not produced.is_file() or not produced.read_bytes().startswith(b'%PDF-'):
            raise RuntimeError('LibreOffice no produjo un PDF válido. ' + result.stderr.strip() + ' ' + result.stdout.strip())
        shutil.copyfile(produced, target)
    print(target)


if __name__ == '__main__':
    main()
