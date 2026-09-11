# Construcción de la distribución fundacional

`construir_paquete.py` crea el inventario y manifiesto del [paquete vigente](../../producto/paquete_fundacional/v0.2/LEEME.md) y una distribución ZIP en `entregables/`. Utiliza solo las carpetas de versiones actuales enumeradas en el propio constructor y las herramientas documentales expresamente incluidas. Requiere Python y su biblioteca estándar; no ejecuta la metodología, el modelo económico ni los renderizadores.

El constructor comprueba archivos y enlaces antes de distribuir, añade una entrada `INICIO.md` dentro del ZIP y conserva rutas relativas. Las vistas Word y el libro deben existir previamente; se incluyen tal como están, sin atribuir comprobación de comportamiento. El manifiesto fija todos los contenidos salvo su propia huella; el ZIP tiene una huella externa junto a él.

La regeneración sustituye inventario, manifiesto y distribución de esta versión. Antes de publicar un cambio general, preservar el conjunto anterior y aplicar las reglas de versiones del producto. Los maestros, el archivo histórico, entornos de dependencias y temporales de revisión no se distribuyen. El paquete de una prestación se prepara conforme a N17, fuera de estas fuentes generales.

## Regenerar ayudas de uso

Ejecutar primero `python herramientas/paquete/construir_lecturas.py`: genera dieciocho cargas derivadas y el ZIP de estructura vacía desde instrucciones actuales, rutas y plantilla de índice. Después regenerar las vistas afectadas y ejecutar `python herramientas/paquete/construir_paquete.py`. Las compilaciones identifican originales y dependencias adicionales; no son nuevas fuentes editables.

La escritura de texto usa UTF-8 y finales LF. Los ZIP fijan orden, fecha y atributos de entrada. La identidad de bytes de compresión requiere la misma biblioteca y versión; no se declara reproducibilidad entre motores diferentes.
