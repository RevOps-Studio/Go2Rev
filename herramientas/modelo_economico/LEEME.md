# Construcción del modelo económico

El libro vacío puede usarse sin ejecutar herramientas. Para regenerarlo, esta herramienta lee la [definición editable JSON](../../producto/metodo/oferta_entrega_y_economia/v0.1/modelo/definicion_modelo.json), con celdas, fórmulas, estilos, validaciones y disposición. Las relaciones y sus dominios se explican en la [especificación metodológica](../../producto/metodo/oferta_entrega_y_economia/v0.1/04_formulas_y_dominio.md); la [guía del modelo](../../producto/metodo/oferta_entrega_y_economia/v0.1/08_guia_del_modelo.md) describe su uso. Una modificación general de fórmulas mantiene coherentes esas fuentes y su revisión.

## Regenerar el original vacío

Requiere Python 3.11 o posterior y openpyxl 3.1.5. Desde la raíz del repositorio o de la distribución extraída:

```text
python -m pip install -r herramientas/modelo_economico/requirements.txt
python herramientas/modelo_economico/construir_modelo.py
```

La dependencia se instala una vez en el entorno elegido; no es necesario reinstalarla en cada sesión. El generador produce `producto/metodo/oferta_entrega_y_economia/v0.1/modelo/Go2Rev_modelo_economico_v0.2.xlsx`. La opción `--salida` permite indicar otra ruta para el original vacío generado. Ambas formas sustituyen el archivo de destino: nunca dirigirlas a una copia cumplimentada de una prestación.

El generador necesita únicamente la definición actual, Python y la biblioteca indicada. No lee libros anteriores, archivos históricos, datos empresariales, un runtime de proveedor ni conexiones externas. El JSON contiene instrucciones generales y campos de entrada vacíos. El código rechaza valores en esas entradas y constantes numéricas fuera de las fórmulas.

## Cálculo, conservación y revisión

La herramienta escribe fórmulas y solicita recálculo al abrir el XLSX; **no calcula sus resultados**. Esta separación responde al comportamiento documentado de [openpyxl para fórmulas](https://openpyxl.readthedocs.io/en/stable/simple_formulae.html). Tampoco ejecuta las [validaciones de celda](https://openpyxl.readthedocs.io/en/stable/validation.html): las incorpora para el motor de hoja de cálculo. La [documentación de instalación y uso](https://openpyxl.readthedocs.io/en/stable/tutorial.html) describe la biblioteca.

Durante una prestación, abrir y recalcular la copia de trabajo en el motor XLSX que se utilizará antes de interpretar resultados. Una vista previa que no calcule puede mostrar las fórmulas sin resultado actualizado. Conservar siempre la fuente de parámetros, el libro y la conclusión K12 con la misma combinación y revisión.

El archivo generado fija fechas, orden y atributos de sus entradas ZIP. La identidad de bytes se comprueba con la misma definición y versiones del entorno; no se declara idéntica compresión entre versiones diferentes. Los informes y vistas de revisión se conservan en `salida/`, fuera del producto y de la distribución.
