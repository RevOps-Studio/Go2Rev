# Construcción de la distribución fundacional

`construir_paquete.py` crea el inventario y manifiesto del [paquete vigente](../../producto/paquete_fundacional/v0.6/LEEME.md) y una distribución ZIP en `entregables/`. Utiliza solo las carpetas de versiones actuales enumeradas en el propio constructor y las herramientas documentales expresamente incluidas. Requiere Python y su biblioteca estándar; no ejecuta la metodología, el modelo económico ni los renderizadores.

El constructor comprueba archivos y enlaces antes de distribuir, añade una entrada `INICIO.md` dentro del ZIP y conserva rutas relativas. Las vistas Word y el libro deben existir previamente; se incluyen tal como están, sin atribuir comprobación de comportamiento. El manifiesto fija todos los contenidos salvo su propia huella; el ZIP tiene una huella externa junto a él.

La regeneración sustituye inventario, manifiesto y distribución de esta versión. Antes de publicar un cambio general, preservar el conjunto anterior y aplicar las reglas de versiones del producto. Los maestros, el archivo histórico, entornos de dependencias y temporales de revisión no se distribuyen. El paquete de una prestación se prepara conforme a N17, fuera de estas fuentes generales.

## Regenerar ayudas de uso

Ejecutar primero `python herramientas/paquete/construir_plantillas.py`: genera las 37 plantillas vacías, el índice de primera pasada y 17 JSON Schema de estructura opcional. Después ejecutar `python herramientas/paquete/construir_lecturas.py`: genera la carga común, 17 cargas iniciales, 17 extensiones, el registro de tamaño y el ZIP de estructura vacía. Después regenerar las vistas afectadas y ejecutar `python herramientas/paquete/construir_paquete.py`. Las compilaciones identifican originales y dependencias adicionales; no son nuevas fuentes editables.

La escritura de texto usa UTF-8 y finales LF. Los ZIP fijan orden, fecha y atributos de entrada. La identidad de bytes de compresión requiere la misma biblioteca y versión; no se declara reproducibilidad entre motores diferentes.

## Control de carga y alcance de la revisión

La configuración en rutas_de_lectura.json fija entrada ≤600 palabras, común ≤2000, nodo ≤3000 y común+nodo ≤4999. El constructor falla antes de escribir las lecturas si se supera un límite. Cuenta palabras por espacios, incluidos localizadores, tablas y cabeceras; no estima tokens o tiempo. Las extensiones preservan el detalle y se leen por condición, sin un límite que recorte el razonamiento necesario.

Los generadores validan identidades, rutas, matrices vacías y cobertura. Los JSON Schema exportados solo describen una representación textual opcional; su validación no acredita contenido completo o suficiente. La equivalencia documental y regeneración no ejecutan la metodología.
