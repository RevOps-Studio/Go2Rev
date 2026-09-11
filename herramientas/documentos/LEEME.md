# Vistas Word del método

Requiere Python 3.10 o posterior. Instalar las versiones declaradas con `python -m pip install -r herramientas/documentos/requirements.txt`. `python-docx` y `lxml` generan DOCX; `pypdfium2` convierte PDF a imágenes. Ejecutar `python herramientas/documentos/construir_lectura.py` para arquitectura o añadir `--guia` para implementación. Arquitectura reúne cuatro fuentes operativas; implementación reúne entorno, carpetas, glosario, guía, alcance y composición de entregables.

El constructor lee únicamente fuentes actuales del producto y sus estilos. Los archivos se guardan junto a las fuentes; `salida/` contiene revisión temporal excluida de la distribución. Los documentos existentes pueden utilizarse sin regenerarlos.

Para revisar presentación en Windows con Word instalado, utilizar `renderizar_word.ps1` con rutas absolutas de entrada y PDF de salida; Word se abre en segundo plano y cierra sin modificar el original.

Como alternativa, con LibreOffice instalado en Linux, macOS o Windows, ejecutar `python herramientas/documentos/renderizar_libreoffice.py entrada.docx salida.pdf`; añadir `--soffice` con la ruta al ejecutable cuando no esté en PATH. El conversor usa un perfil temporal propio y exige un PDF nuevo. Las opciones proceden de la [documentación oficial de LibreOffice](https://help.libreoffice.org/latest/en-US/text/shared/guide/start_parameters.html?DbPAR=SHARED), consultada el 11 de septiembre de 2026. LibreOffice es una dependencia externa opcional; este archivo no presupone que esté instalado.

Ejecutar `renderizar_paginas.py` sobre el PDF para revisar sus imágenes. La paginación puede variar entre Word y LibreOffice o por fuentes disponibles; revisar todas las páginas en el motor empleado. La generación DOCX no exige ninguno de esos motores. La revisión visual no acredita aplicación del método.

El cierre del conjunto 0.4 comprueba generación y presentación en Windows/Word. La ruta LibreOffice está implementada y revisada documentalmente; no se atribuye una ejecución en Linux ni identidad de bytes entre motores.
