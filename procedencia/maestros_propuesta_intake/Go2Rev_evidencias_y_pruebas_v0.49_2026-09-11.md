# Go2Rev Evidencias y pruebas v0.49

11 de septiembre de 2026 · Registro de construcción y revisión documental

[Plan v0.53](Go2Rev_plan_de_trabajo_v0.53_2026-09-11.md) · [Producto v0.42](Go2Rev_producto_y_metodo_v0.42_2026-09-11.md)

## Base y decisiones conservadas

Go2Rev sigue teórico y sin clientes. Carlos aceptó la arquitectura de diecisiete nodos el 10 de septiembre y autorizó integrar v0.4 en main el 11 de septiembre. Se conservan B2B, recorridos A/B, salida económica de Diagnostic prevista desde contratación, preparación comprobada con acompañamiento acotado, autonomía de RevOS y operación independiente del LLM. Las autorizaciones de construir y publicar mejoras en ramas no equivalen a autorizar su integración en main.

La base estable verificada al iniciar esta mejora es `15d2cebd08cb53073a8b5a67f11ba065ef41bd4a`, coincidente en main local y remoto, con árbol de trabajo limpio. La rama `mejora/intake-diagnostic` parte de esa base. La etiqueta base-fundacional-v0.4 y las anteriores permanecen como hitos de recuperación.

Los [maestros de la base v0.4](procedencia/maestros_base_v0.4/LEEME.md) conservan las versiones 0.52/0.41/0.48 y el detalle de sus revisiones previas. Sus contenidos se archivan sin reescritura. La [procedencia metodológica](procedencia/LEEME.md) mantiene las correspondencias con originales. No se repiten recuperación ni PORT-01, ni se atribuye una lectura nueva de RevOS/GTM o de Back to the plan.

## Encargo de intake y análisis

Carlos solicita un documento para anticipar tipo, calidad y cantidad de información necesaria del cliente, distinguir importancia y bloqueos, y reducir la fricción de ponerlo a trabajar al principio. Pide pensar el enfoque para revisarlo. La respuesta construida es una [propuesta de producto v0.1](producto/propuestas/intake_diagnostic/v0.1/01_propuesta_de_intake.md), separada de las instrucciones operativas.

Se examinan N01/N02, contratos K01/K02 y SOL, investigación/suficiencia, recomendación e interfaces N03–N06 con economía exploratoria, contraste externo, suficiencia común y guardado. La relación de archivos está en la propuesta. La vista generada de SOL se utiliza para comprobar cobertura; no se edita como fuente.

La revisión encuentra que el método ya asigna al asistente la lectura, extracción e investigación, limita las solicitudes a necesidades de decisión, acepta recepciones parciales y distingue suficiencia por uso. La carencia concreta es una guía reunida que anticipe selección, cobertura, momento y esfuerzo, más la experiencia inicial del cliente.

## Decisiones propuestas, aún no aceptadas

| Propuesta | Fundamento y límite |
|---|---|
| Material existente y corrección de síntesis al comenzar | Reduce tareas de elaboración previstas para el cliente. Es una decisión de diseño; no se atribuye ahorro de tiempo observado |
| Catálogo interno y peticiones seleccionadas | Desarrolla las familias de N02 sin convertirlas en un cuestionario íntegro ni trasladar las plantillas del consultor al cliente |
| Imprescindible/deseable/opcional por uso; bloqueo como efecto localizado | Conserva CONTR/EVAL/USO y la recepción por campo. La aplicabilidad A/B o de una forma de oferta se decide por separado |
| Cantidad determinada por cobertura | Define ámbito, unidad, periodo, selección y decisión antes de pedir volumen; sin cuotas universales ni tasas a partir de material seleccionado |
| Calidad con recepción parcial y alternativas | Usa estados existentes, preserva desconocidos y evita transformar recepción o aprobación en evidencia |
| Investigación externa y economía producidas por Go2Rev | El cliente facilita hechos propios; el asistente contrasta entorno y construye derivaciones. Una referencia externa no acredita rendimiento o disponibilidad propios |
| Ampliaciones con razón y esfuerzo explícitos | Aplica proporcionalidad al trabajo nuevo solicitado. No fija duración ni requiere un sistema de medición |

El documento incluye el catálogo de trece familias de necesidad, secuencia de recogida, condiciones para seguir o limitar, criterios de cobertura/calidad, contenido de la comunicación inicial y correspondencia de incorporación. No crea instancias de negocio ni una solicitud real. La futura comunicación reutilizable y los ajustes operativos se concretarán tras la revisión de producto.

## Alcance de la revisión documental

Se revisan cobertura de mandato/oferta, A/B, compra/acceso/venta, investigación externa, entrega, economía/caja y restricciones; separación de imprescindible y bloqueante; responsabilidades de producción; compatibilidad con estados e interfaces; conservación de permisos vigentes y salidas de K01. La propuesta mantiene las diecisiete capacidades y usa los registros ya definidos.

Se comprobaron 55 enlaces locales en los siete documentos nuevos o actualizados, sin ausencias, y la estructura de sus tablas. Los tres maestros archivados coinciden byte a byte con la base de Git y permanecen exactamente tres maestros vigentes en la raíz. Las fuentes operativas, herramientas y distribuciones no presentan cambios frente a la base; el ZIP v0.4 conserva SHA256 `5c093230d7c9fc8647cf90d2282181d6a997797f4d2ee6ee660d28ecb957afea`. Al permanecer idéntico el paquete estable no se repiten generación de derivados, recálculo ni renderizado. No se utiliza una revisión estructural como prueba de reducción real de fricción.

## Estado y límites

Propuesta del asistente para revisión de Carlos; no decisión de producto aceptada ni nueva distribución. Se mantiene v0.4 y no se modifica la fuente estructurada de plantillas. No se han ejecutado un intake, entrevistas, campañas, protocolos de prestación ni cálculos de una empresa. No se incorporan originales empresariales ni tiempos observados.

Continúan pendientes la ejecución Linux/LibreOffice y las decisiones de automatización económica ya diferidas. Captación y validación comercial no forman parte de esta mejora. Los resultados de aplicación y la reducción de esfuerzo se podrán examinar únicamente durante prestaciones posteriores autorizadas.
