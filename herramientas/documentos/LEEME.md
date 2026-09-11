# Vistas Word del método

Requiere Python con `python-docx` y `lxml`. Ejecutar `python herramientas/documentos/construir_lectura.py` para arquitectura o añadir `--guia` para implementación. Arquitectura reúne cuatro fuentes operativas; implementación reúne entorno, carpetas, glosario, guía, alcance y composición de entregables.

El constructor lee únicamente fuentes actuales del producto y sus estilos. Los archivos se guardan junto a las fuentes; `salida/` contiene revisión temporal excluida de la distribución. Los documentos existentes pueden utilizarse sin regenerarlos.

Para revisar presentación en Windows con Word instalado, utilizar `renderizar_word.ps1` con rutas absolutas de entrada y PDF de salida; Word se abre en segundo plano y cierra sin modificar el original. `renderizar_paginas.py` necesita `pypdfium2` para obtener imágenes del PDF. Un entorno sin Word debe usar un renderizador de DOCX disponible y revisar el resultado; la generación de DOCX no exige Word. La revisión visual no acredita aplicación del método.
