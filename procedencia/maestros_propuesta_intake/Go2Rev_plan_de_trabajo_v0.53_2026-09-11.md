# Go2Rev Plan de trabajo v0.53

11 de septiembre de 2026 · Responsable de producto Carlos Estrada

[Producto v0.42](Go2Rev_producto_y_metodo_v0.42_2026-09-11.md) · [Evidencias v0.49](Go2Rev_evidencias_y_pruebas_v0.49_2026-09-11.md)

## Objetivo y base estable

Mantener una primera metodología completa, lista para implementar en el primer cliente dentro del alcance declarado. Go2Rev sigue teórico y sin clientes. La base estable es el [conjunto v0.4](producto/paquete_fundacional/v0.4/LEEME.md), integrado en main con autorización de Carlos e identificado por la etiqueta base-fundacional-v0.4. La arquitectura conserva diecisiete nodos y correspondencia con once pasos. FND01–FND08 están construidos y revisados documentalmente; los protocolos de prestación no se han ejecutado.

Las mejoras se trabajan en ramas propias desde main actualizado. Los hitos, ramas y versiones anteriores se conservan. Esta continuación registra una propuesta de intake; no publica otra versión operativa.

## Trabajo actual: intake de Diagnostic

Carlos solicita anticipar tipo, calidad y cantidad de información del cliente, distinguir lo imprescindible, deseable, opcional y bloqueante, y reducir el trabajo inicial que se le pide. El encargo actual es pensar y preparar una propuesta revisable antes de acordar su incorporación.

Rama: `mejora/intake-diagnostic`, desde main `15d2cebd08cb53073a8b5a67f11ba065ef41bd4a`.

| Trabajo | Resultado | Estado |
|---|---|---|
| Revisar cobertura vigente | N01/N02, solicitudes, interfaces de Diagnostic, investigación externa, suficiencia y guardado | Revisado; existen fundamentos suficientes para desarrollar el intake sin alterar la arquitectura |
| Diseñar recogida proporcionada | [Propuesta de intake v0.1](producto/propuestas/intake_diagnostic/v0.1/01_propuesta_de_intake.md): reparto de trabajo, clasificación por uso, arranque, catálogo, cobertura/calidad, bloqueos y experiencia del cliente | Borrador construido para revisión de producto |
| Revisar decisiones con Carlos | Aportación inicial de material existente y corrección de síntesis; catálogo interno; bloqueo localizado; ampliaciones con utilidad y esfuerzo explícitos | Pendiente de su valoración del documento |
| Incorporar el diseño al producto | Guía del consultor, comunicación inicial reutilizable y referencias/formatos que resulten necesarios | Propuesto; concretar con la revisión de producto antes de modificar el método operativo |
| Mantener continuidad | Tres maestros, procedencia y rama revisable | Esta continuación conserva v0.4 como base estable y la propuesta separada |

La propuesta es un archivo de producto. No crea otro plan maestro, un nuevo nodo, registros empresariales ni un sistema de captura. Se conserva la distribución v0.4 y sus fuentes operativas. No se ejecuta un intake ni se mide esfuerzo real con información de una empresa.

## Límites pendientes conservados

La ejecución de la ruta Linux/LibreOffice continúa pendiente de un entorno disponible; su implementación no acredita portabilidad ejecutada. La presentación disponible fue revisada con Word en Windows.

Sigue diferida la decisión sobre un selector simultáneo de escenarios y una relación automática entre periodo y horizonte de caja en el libro. Se revisará esa automatización con una necesidad de implementación fundada. El libro no cambia con esta propuesta.

Captación y validación comercial continúan diferidas. Carlos dedica 4–5 horas semanales a decisiones de producto y arquitectura; el asistente produce las piezas. Esa dedicación no es capacidad de prestación. Las descripciones de actuaciones del intake corresponden a una futura prestación autorizada.
