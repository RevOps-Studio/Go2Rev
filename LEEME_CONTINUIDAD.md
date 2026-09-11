# Continuidad de Go2Rev

11 de septiembre de 2026 · Índice, no maestro

Go2Rev v0.5 incorpora el intake operativo en la rama mejora/intake-diagnostic, autorizado por Carlos el 11 de septiembre de 2026. La [solicitud 4](https://github.com/RevOps-Studio/Go2Rev/pull/4) conserva esa mejora para revisión de integración. La revisión actual propone distinguir entregables, consumo y proceso en una rama dependiente, sin cambiar el conjunto operativo. Main y la etiqueta base-fundacional-v0.4 mantienen la base estable anterior. El método sigue teórico, sin clientes ni pruebas de aplicación.

## Tres documentos vivos

- [Plan v0.55](Go2Rev_plan_de_trabajo_v0.55_2026-09-11.md): propuesta de clasificación, dependencia del intake y trabajo posterior.
- [Producto v0.44](Go2Rev_producto_y_metodo_v0.44_2026-09-11.md): definición vigente y propuesta separada de lo aceptado.
- [Evidencias v0.51](Go2Rev_evidencias_y_pruebas_v0.51_2026-09-11.md): petición, fuentes, correspondencia y revisión documental.

## Trabajo actual

La rama `mejora/entregables-y-consumo` parte del intake publicado en `885258909f0c8c0b7c64c680ede8bddb876b02db`. La [clasificación propuesta](producto/propuestas/entregables_y_consumo/v0.1/01_clasificacion_y_criterios.md) distingue interno de proceso, interno de consumo y externo entregable, con circulación separada y checkpoints como momentos de decisión. El [anexo de 37 plantillas](producto/propuestas/entregables_y_consumo/v0.1/02_correspondencia_de_plantillas.md) localiza la correspondencia sin cambiar contratos.

Carlos revisa el criterio antes de incorporar reglas y desarrollar formatos. Continuar esta rama para ajustes de la propuesta. Su solicitud de integración se dirige a `mejora/intake-diagnostic`; el orden hacia main es intake y después esta mejora. La guía, catálogo y comunicación del intake, así como todos los componentes de v0.5, permanecen iguales. Los maestros anteriores se conservan en [procedencia](procedencia/maestros_intake_operativo/LEEME.md).

## Entrada del producto

[Paquete fundacional v0.5](producto/paquete_fundacional/v0.5/LEEME.md), [guía Word](producto/paquete_fundacional/v0.5/Go2Rev_guia_de_implementacion_v0.5.docx) y [distribución](entregables/Go2Rev_fundacional_v0.5.zip). El paquete contiene las fuentes, plantillas, modelo y derivados. La operación usa su entrada propia, sin cargar maestros ni archivo de procedencia.

[Arquitectura](producto/arquitectura/v0.2/01_arquitectura_metodologica.md) mantiene diecisiete nodos y correspondencia con once pasos; [operación conversacional](producto/metodo/operacion_conversacional/v0.3/LEEME.md) abre carpetas, entorno, primera pasada y continuidad.

[Procedencia del diseño](procedencia/LEEME.md) conserva las correspondencias de originales pertinentes y los maestros sustituidos. Back to the plan permanece congelado y fuera de las búsquedas rutinarias. No repetir recuperación ni PORT-01 por una nueva sesión.
