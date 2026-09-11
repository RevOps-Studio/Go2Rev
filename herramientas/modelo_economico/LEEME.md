# Construcción del modelo económico

Esta herramienta regenera el libro vacío desde la [definición editable del producto](../../producto/metodo/oferta_entrega_y_economia/v0.1/modelo/definicion_modelo.mjs). Las fórmulas se explican en la [especificación metodológica](../../producto/metodo/oferta_entrega_y_economia/v0.1/04_formulas_y_dominio.md). Una modificación de fórmulas actualiza ambas fuentes y su revisión; el archivo de prestación nunca se usa como entrada de producción.

El ejecutor usa Node y `@oai/artifact-tool` del runtime documental instalado. `node_modules` es una referencia local a esas dependencias, no contenido del producto. Ejecutar `construir_modelo.mjs` con ese runtime regenera un único libro del producto y guarda las vistas de revisión en `salida/`. Se recalculan únicamente las fórmulas del formato vacío; no se introducen parámetros ni se ejecuta una prestación.

La ejecución sobrescribe el derivado vacío. Las correcciones generales pertenecen a la definición en `producto/`; nunca regenerar sobre un archivo cumplimentado en una prestación. La herramienta no consume archivos históricos, datos de empresa ni conexiones externas. La futura prestación puede editar el libro existente o usar otro medio que conserve sus contratos; no necesita ejecutar este generador.
