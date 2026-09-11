# Construcción fundacional de Go2Rev

Lee `LEEME_CONTINUIDAD.md` y las secciones vigentes de los tres maestros antes de continuar. El Plan mantiene tareas; Producto mantiene definición y arquitectura; Evidencias mantiene decisiones de construcción, fuentes y revisión documental.

## Mandato vigente

Construir íntegramente la primera metodología Go2Rev para poder implementarla en el primer cliente. Su estado es teórico y no ha habido clientes. Carlos aceptó la arquitectura de diecisiete nodos el 10 de septiembre de 2026 y fijó que las pruebas de la metodología se realizarán únicamente después de completar su construcción.

Durante la construcción se producen instrucciones sustantivas, contratos, plantillas vacías, fórmulas generales, guías y protocolos. Cada tarea debe contribuir a un componente del entregable final o resolver una carencia de ese componente. Los archivos activos contienen exclusivamente conocimiento metodológico general y decisiones de producto. No se crean expedientes empresariales, registros de oportunidades, datos de demostración, personajes ni resultados de aplicación.

La revisión de construcción es documental: cobertura, razonamiento, interfaces, consistencia de fórmulas, integridad de archivos y legibilidad. No se ejecutan recorridos de negocio, campañas, entrevistas ni pruebas de la metodología durante su construcción. Diseñar los protocolos forma parte del producto; ejecutarlos es una etapa posterior a la construcción completa.

Los procedimientos Diagnostic, Design y Despliegue describen lo que se hará en una futura prestación contratada. Sus acciones no son tareas actuales de desarrollo. Mantén esta distinción en todos los formatos, incluidos MD, documentos, hojas, YAML, JSON y código.

## Fuentes y continuidad

`Back to the plan/` es un archivo de procedencia, excluido de la carga operativa y de las búsquedas rutinarias. No se modifica ni se incorpora su contenido por bloques a documentos vigentes. Cuando una tarea precise un original metodológico, consulta exclusivamente el archivo pertinente identificado en la correspondencia de fuentes. Extrae la regla general y registra su procedencia; no copies contextos de aplicación, datos, instrucciones de ejecución o resultados ajenos a la construcción.

Las versiones anteriores no vuelven a ser vigentes por aparecer en una exportación. Las continuaciones de los maestros contienen solo estado y contenido actuales; conserva las versiones sustituidas en el archivo, sin anexar su texto al maestro nuevo.

Las fuentes metodológicas editables están en `producto/`. Las vistas Word y otros formatos derivados se regeneran desde ellas. Las herramientas de documentación solo leen las fuentes actuales y recursos de estilo; no consumen expedientes o controles antiguos como dependencia de producción.

Carlos revisa decisiones de producto y arquitectura, con 4–5 horas semanales. El asistente redacta y construye las piezas. Continúa el trabajo autorizado sin pedir confirmación de decisiones ya aceptadas. No añadas otros planes maestros.

## Trabajo por ramas y recuperación

Desde el repositorio inicial en GitHub, toda mejora posterior se desarrolla en una rama propia. `main` conserva la base estable; no se editan ni se publican mejoras directamente en ella. Una rama agrupa una mejora coherente, aunque requiera varias sesiones y commits. Al continuar, recuperar la rama de esa mejora en lugar de crear otra por cambio de sesión.

Antes de empezar otra mejora, comprobar rama, cambios locales y base remota. Partir de la base estable actualizada, preservando cualquier trabajo existente. Guardar avances coherentes en commits y subir la rama a GitHub para conservar también la copia remota. Mantener producto, derivados y maestros afectados consistentes en la misma rama; su separación funcional no cambia.

Si una mejora depende de otra todavía en revisión, se puede abrir una rama dependiente desde su commit publicado y dirigir su solicitud de integración a esa rama. Identificar la dependencia y el orden de integración. Esto permite revisar únicamente la segunda mejora sin anticipar la integración de la primera a `main`.

Preparar una solicitud de integración (pull request) cuando haya un resultado revisable, con alcance, revisión documental realizada y límites. Incorporar a `main` después de la revisión y autorización de Carlos para esa integración; una autorización ya concedida y suficiente no se solicita de nuevo. Una aprobación de análisis o de propuesta no acredita por sí sola implementación terminada.

Conservar hitos estables mediante etiquetas identificables. La etiqueta `base-fundacional-v0.1` señala el commit inicial `c56b0a171da2649cdc735986021f2d680ee4681d`. No mover ni sustituir etiquetas publicadas. Para deshacer una integración compartida, utilizar un commit de reversión que preserve el historial; no reescribirlo ni forzar una subida. Las ramas y etiquetas no respaldan los archivos excluidos de Git, incluido `Back to the plan/`.
