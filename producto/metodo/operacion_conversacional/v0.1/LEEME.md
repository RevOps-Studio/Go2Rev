# Operación conversacional y capacidades del entorno

Versión 0.1 · FND07 · Capa común de N01–N17 · Construcción fundacional

Este componente contiene la entrada reutilizable de Go2Rev y las instrucciones para seleccionar tareas, leer fuentes, trabajar con las capacidades disponibles y conservar continuidad. Aplica los contratos de los componentes metodológicos construidos. No añade nodos, planes maestros ni un sistema propio de ejecución.

## Archivos y uso

| Necesidad | Archivo |
|---|---|
| Dar al asistente las instrucciones comunes de operación | [ENTRADA_GO2REV](ENTRADA_GO2REV.md) |
| Entender cómo dirigir una prestación por conversación | [Guía del consultor](01_guia_del_consultor.md) |
| Localizar la instrucción, entradas y salida de una tarea | [Rutas y lectura selectiva](02_rutas_y_lectura.md) |
| Determinar qué permite el entorno y qué alternativa basta | [Capacidades y alternativas](03_capacidades_y_alternativas.md) |
| Preparar el uso en un entorno o el traslado solicitado | [Adaptación del entorno](04_adaptacion_del_entorno.md) |
| Reanudar, guardar cambios y conservar decisiones | [Continuidad y cambios](05_continuidad_y_cambios.md) |
| Revisar la recepción y los límites de esta capa común | [Contrato y revisión](06_contrato_y_revision.md) |
| Consultar la procedencia del diseño | [Fuentes y correspondencia](07_fuentes_y_correspondencia.md) |

Las [capacidades del entorno](plantillas/01_capacidad_del_entorno.md), [continuidad de tarea](plantillas/02_continuidad_de_tarea.md) y [traspaso de contexto](plantillas/03_traspaso_de_contexto.md) son plantillas vacías, agrupables con CAP/K02/K17. No requieren registros adicionales cuando esos campos ya existen.

## Alcance de la entrada común

La entrada se proporciona al asistente junto con acceso a las instrucciones actuales del producto y, en una futura prestación, al ámbito y materiales autorizados de ese encargo. El [mapa de lectura](02_rutas_y_lectura.md) enlaza N01–N17 con sus productores reales. El asistente abre la instrucción sustantiva pertinente y sus contratos; el índice no la sustituye.

Un entorno puede incorporar la entrada como instrucciones de trabajo, documento de referencia o recurso equivalente. La adaptación conserva texto, versión y enlaces resolubles; no presupone instalación, ejecución automática o compatibilidad con un producto concreto. El consultor puede usar las mismas guías directamente si trabaja sin LLM.

La neutralidad de proveedor se construye mediante reglas y contratos comunes. No significa que cualquier entorno disponga de las mismas capacidades o produzca idéntico texto. La lectura, cálculo, escritura, investigación y actuaciones se declaran con su disponibilidad y límites reales; su comportamiento se comprobará después de completar la construcción y para el uso correspondiente.

## Construcción y futura prestación

Durante la construcción se redactan y revisan estas instrucciones, sin crear registros empresariales cumplimentados, conectar servicios ni ejecutar recorridos o pruebas de la metodología. Plan mantiene el desarrollo; Producto, la definición; Evidencias, decisiones y revisión documental. Estos tres maestros no se convierten en dependencias de una futura prestación.

El [paquete fundacional](../../../paquete_fundacional/v0.1/LEEME.md) fija alcance, componentes, guía de implementación y versión del conjunto. La [guía del consultor](01_guia_del_consultor.md) explica cómo dirigir el trabajo cuando exista el ámbito autorizado pertinente.
