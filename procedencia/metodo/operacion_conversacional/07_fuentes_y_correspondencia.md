# Procedencia y correspondencia de FND07

Versión 0.1 · Lectura por capacidad · 11 de septiembre de 2026

## Fuentes vigentes utilizadas

La [arquitectura y gobernanza](../../../producto/arquitectura/v0.2/04_dependencias_y_gobernanza.md) establece dependencias por campo, suficiencia, autoridad, operación conversacional y neutralidad de LLM. La [especificación de construcción](../../arquitectura/06_construccion_y_revision.md) exige entrada y guías completas sin ejecutar el método durante su construcción.

La entrada enlaza las fuentes metodológicas vigentes de FND02–FND06 mediante el [mapa de rutas](../../../producto/metodo/operacion_conversacional/v0.2/02_rutas_y_lectura.md). Reutiliza el diccionario común, intercambio exploratorio, cruce externo/interno, rutina de fuentes/acceso, fórmulas y dominios, contratos de productores y protocolos de preparación/transferencia. Estos componentes conservan sus versiones y autoría; FND07 integra su uso, sin reemplazarlos por una compilación.

La [correspondencia de arquitectura](../../arquitectura/05_reutilizacion_y_fuentes.md) mantiene disponibilidad física, procedencia y registro de ausencias. Se leen únicamente los originales pertinentes identificados allí. La presencia de binarios u otros componentes no leídos no acredita reutilización; no se recrean desde resúmenes ni se convierten en dependencias operativas.

Raíz del consolidado: `Back to the plan/fuentes/Go2Rev_snapshot_migracion_v0.2_2026-09-10/`.

**G** = `workspace/outputs/work01-20260910/metodo/` dentro de esa raíz.

**R** = `referencia_corte_v0.1/Go2Rev_snapshot_pre_migracion_v0.1_2026-09-10/20_referencias/RevOS_4.4.0/fuente/`.

**T** = mismo prefijo, bajo `GTM_Planner_0.3.0/fuente/`, de procedencia local correspondiente al commit `c03068ce187d264caa6f5e9fc172d46907ccbcca`. No se repite recuperación ni verificación del remoto.

## Originales leídos para esta capacidad

| Original y lectura efectiva | Conservar / adaptar | Completar / retirar en Go2Rev |
|---|---|---|
| G `instrucciones_minimas_v0.7.md`, líneas 39–48 y 79–86: inicio/reanudación, análisis, cambio y cierre | Entrada humana situada, recuperación suficiente, análisis más allá del brief, capacidades y continuidad con límites | Construir una entrada nueva desde N01–N17 y sus fuentes actuales. Retirar taxonomías y reglas históricas sustituidas, rutinas de ejecución durante construcción y restauración del original como entrada vigente |
| G `formato_expediente_y_kit_v0.1.md`, líneas 1–18 y desde 27 al final: evaluación, registro/traspaso y transferencia | Relación afirmación/fuente/decisión, desconocidos, autoridad de inicio separada de preparación y conservación de contexto | Adaptar a AF/FUE/DEC/CAP/CAM y K actuales; retirar estructura comercial obligatoria y campos empresariales precargados. No incorporar el formato histórico como plantilla activa |
| R `skills/revos-orchestrator/SKILL.md`, completo | Selección de capacidad por dependencias, entradas y carencias; impacto efectivo sobre consumidores | Completar producción autorizada, lectura por tarea y persistencia. Retirar confirmación por cada avance/cambio, maestros propios de RevOS, contadores de revisiones y conversión automática de ausencia en supuesto |
| R `skills/revos-orchestrator/references/grafo-dependencias.md`, completo | Dependencias distintas del orden de presentación, descendencia transitiva y fuente frente a vista | Aplicar el grafo aceptado Go2Rev y sus contratos E/O. Retirar tiers, 28 nodos, asignación de modelos y checkpoints universales del original. No sustituir N01–N17 por ese grafo |
| R `skills/revos-orchestrator/references/convenciones.md`, líneas 70–87, 101–119 y desde 133 al final: captura, versionado/estado y registro de artefactos | Captura frente a interpretación, lectura antes de pedir, identidad de artefactos y procedencia | Completar original/localizador, cobertura y revisión de datos materiales. Retirar nomenclatura propia, edición de datos sin revisión cuando sustentan decisiones, propagación diferida por etiqueta, conversión automática de resúmenes en supuestos y migración al reabrir |
| R `skills/cambio/SKILL.md`, completo | Campo y origen del cambio, efecto sobre valor/argumento, productor antes de consumidor y conservación de versiones | Aplicar CAM por consecuencia real y autoridad vigente. Retirar aprobación por propagación, dos contadores, bloqueos globales y tolerancia automática a inconsistencias transitorias de datos críticos |
| T `skills/intake/SKILL.md`, completo; no nueva lectura de la plantilla externa referenciada | Conversación adaptativa, fuentes antes de preguntas, declaración frente a inferencia, desconocidos y actualización de lo existente | Completar entrada para todas las capacidades, sin captura universal ni herramienta obligatoria. Retirar jerarquía factual automática por fuente, escala global de confianza, aprobación por paso y despacho de agentes |

Estos `SKILL.md` son originales metodológicos de referencia. Sus instrucciones no activan plugins, agentes, permisos o flujos en Go2Rev. Las reglas de plataforma que mencionan no se adoptan como condiciones universales. La precedencia vigente es la del mandato fundacional y los contratos de producto actuales.

El diseño nuevo de capacidades por acción, alternativas suficientes, persistencia verificable, edición concurrente, resultados ambiguos y traslado delimitado es elaboración de Go2Rev. La neutralidad se expresa como invariantes de contrato, no como equivalencia de resultados o funcionamiento ya comprobado entre plataformas.

## Correspondencia con lo construido

| Necesidad del producto | Resolución |
|---|---|
| Entrada reutilizable para el asistente | ENTRADA_GO2REV: mandato, tarea, lectura, análisis, autoridad, producción y cierre |
| Uso comprensible para el consultor | 01: petición en lenguaje natural, resultado revisable, decisiones propias y recepción |
| Acceso real a instrucciones N01–N17 | 02: rutas, productores, campos y lecturas condicionales; no sustituye instrucciones sustantivas |
| Medios y alternativas con límites | 03 y plantilla 01: acción, disponibilidad, autoridad, resultado y recepción |
| Preparación en distintos entornos y traslado solicitado | 04 y plantilla 03: método/encargo separados, localizadores, transformaciones y protocolo posterior por capacidad |
| Continuidad y cambio sin reinicio | 05 y plantilla 02: fuente/revisión, persistencia, conflicto, interrupción y CAM |
| Contrato e integración revisables | 06: entradas/salidas, invariantes, recepción y límite de revisión documental |

La revisión examina cobertura del mapa, coherencia de instrucciones, integridad de enlaces y campos vacíos. No se ejecuta el método, no se comparan respuestas de proveedores ni se instalan conexiones. El cierre documental y el trabajo pendiente se registran en Evidencias y Plan, respectivamente.
