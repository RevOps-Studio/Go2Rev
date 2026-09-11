# Herramientas de documentación

Estas herramientas generan y revisan dos vistas de lectura del producto. `construir_lectura.py` utiliza los seis archivos actuales de arquitectura; con `--guia` utiliza guía de implementación, alcance y composición de entregables del paquete fundacional. Solo leen estas fuentes actuales y sus recursos de estilo. No ejecutan la metodología ni generan información empresarial.

El constructor mantiene página Letter, márgenes amplios, jerarquía de títulos y tablas legibles. Arquitectura conserva su identidad visual; la guía usa títulos negros. Los Word se generan limpios, con portada, capítulos continuos, enlaces relativos y encabezados de tabla repetidos.

La carpeta `salida/` contiene exclusivamente archivos temporales de revisión documental y procedencia del render. No es fuente metodológica ni parte de la distribución. Cada Word final se guarda junto a sus fuentes en `producto/arquitectura/v0.2/` o `producto/paquete_fundacional/v0.1/`. El constructor requiere Python con `python-docx` y `lxml`; abrir el producto no exige ejecutar esta herramienta. Una regeneración sobrescribe solo el derivado general, nunca un archivo de prestación.

La ausencia de LibreOffice en este entorno ya está identificada. La revisión visual utiliza Word en segundo plano y la biblioteca de renderizado del runtime disponible. El uso de Word requiere el permiso de ejecución del entorno. La inspección de páginas confirma presentación; no equivale a prueba de la metodología.
