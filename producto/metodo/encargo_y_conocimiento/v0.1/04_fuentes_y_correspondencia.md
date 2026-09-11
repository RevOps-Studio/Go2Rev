# Fuentes y correspondencia del componente

Versión 0.1 · 11 de septiembre de 2026 · Registro de diseño de FND02

La autoridad de producto corresponde a los maestros vigentes y a la [arquitectura v0.2](../../../arquitectura/v0.2/01_arquitectura_metodologica.md). Este archivo documenta la procedencia y las adaptaciones de N01/N02. No contiene tareas ni decisiones de una prestación, y no es otro plan maestro.

## Lectura pertinente

Se han consultado físicamente los siete originales identificados abajo. La inspección local de sus archivos y huellas permite fijar la versión leída; no es una nueva recuperación del proyecto ni una verificación remota. Las comprobaciones de integridad del conjunto RevOS/GTM permanecen en Evidencias y no se repiten para construir este componente.

Raíz de procedencia: `Back to the plan/fuentes/Go2Rev_snapshot_migracion_v0.2_2026-09-10/`.

- **G**: `workspace/outputs/work01-20260910/metodo/` dentro de esa raíz.
- **R**: `referencia_corte_v0.1/Go2Rev_snapshot_pre_migracion_v0.1_2026-09-10/20_referencias/RevOS_4.4.0/fuente/`.
- **T**: mismo prefijo de referencias, con `GTM_Planner_0.3.0/fuente/`. Versión asociada a la procedencia local del commit `c03068ce187d264caa6f5e9fc172d46907ccbcca`.

| ID de fuente de diseño | Archivo y lectura realizada en esta construcción | Uso preciso |
|---|---|---|
| G01 | G `instrucciones_minimas_v0.7.md`, §§ Diagnostic: D0, D1, D3 y regla de salida; se delimitó la lectura al contenido metodológico pertinente | Encuadre, inventario por afirmación y salida de evaluación |
| G02 | G `formato_expediente_y_kit_v0.1.md`, § Evaluación y decisión, campos de encargo, afirmación, pregunta y decisión | Esqueleto conceptual de trazabilidad; nueva semántica y plantillas propias |
| R01 | R `skills/client-intake-form/SKILL.md`, completo | Aprovechar material disponible, separar captura e interpretación y detectar discrepancias |
| R02 | R `skills/brief-intake/SKILL.md`, completo, incluidos proceso y plantilla | Lectura transversal, mapa de carencias y revisión de coherencia |
| R03 | R `skills/knowledge-base-builder/SKILL.md`, completo, incluidos todos los campos de plantilla | Cruce de materiales, tensiones y derivaciones; esta lectura amplía la cobertura parcial registrada para la arquitectura |
| T01 | T `skills/intake/SKILL.md`, completo | Entrada conversacional, no repetir preguntas y relacionar huecos con siguiente decisión |
| T02 | T `skills/intake/references/snapshot-template.md`, completo | Familias de información de contexto, oferta, compra, medios, objetivos y restricciones |

Las instrucciones de los originales pertenecen a sus productos y versiones. Se extraen conceptos pertinentes sin convertir esas instrucciones en reglas de Go2Rev. Los documentos binarios de RevOS y otros componentes no leídos no se incorporan a FND02 ni se les atribuye equivalencia. Ninguna carencia de originales bloquea el diseño propio de este componente.

## Conservar, adaptar, completar y retirar

| Decisión de construcción | Procedencia | Resultado en Go2Rev |
|---|---|---|
| Conservar encuadre y valor de una salida de evaluación | G01/G02 | N01 y K01 distinguen pregunta, entrega controlable y decisión; la evaluación tiene contenido recibible aunque no continúe el trabajo |
| Completar el contrato de salida | G01 y promesa vigente del Producto | Consecuencias por salida, honorarios/devengo, trabajo no ejecutado, gastos autorizados, saldo y reanudación antes de contratar; sin tarifa ni cláusula universal |
| Conservar lectura previa y selección de preguntas | R01/R02/T01 | N02 extrae primero, asigna productor al hueco y solicita material preciso con alternativa |
| Adaptar la captura y completar su trazabilidad | G02/R01 | Solicitud, recepción, fuente y afirmación son objetos distintos; se conserva versión/localizador de materiales usados |
| Conservar análisis transversal y completar razonamiento | R02/R03 | Contrastar promesa/entrega, comprador/compra, esfuerzo/coste y objetivo/restricción; explicar mecanismo, alternativas y refutación |
| Adaptar el significado de observación | R03 | Los patrones explicativos y causas inferidas se registran como inferencia o hipótesis; observación se limita a lo efectivamente accesible |
| Retirar prioridades automáticas de fuente | R02/R03/T01 | Pertinencia, método, ámbito, periodo, independencia y coherencia determinan soporte por afirmación y uso; la autoridad decide compromisos |
| Adaptar el conocimiento consolidado | R03/T02 | K02 es índice razonado con perfil y originales localizables; una síntesis no sustituye al original |
| Retirar dependencias de formulario completo, conectores y confirmación por pieza | R01/R02/R03/T01 | Los campos indispensables se exigen para el uso concreto; el trabajo reversible autorizado continúa por conversación |
| Retirar conversión automática de carencia en valor supuesto | R01/R02/R03 | Un desconocido permanece desconocido cuando no hay derivación defendible; una hipótesis necesita razonamiento y límite de uso |
| Retirar extensión, puntuación o medición de activos como requisito general | R02/R03 | Profundidad y selección se juzgan por las decisiones; las métricas de activos se obtienen solo cuando sean pertinentes y accesibles |
| Completar rutas A y B | Producto y arquitectura N01/N02; G01 como antecedente de transferencia | TRA compara condiciones de origen/destino; CAP separa intención, representación, disponibilidad y habilitación |
| Completar contratos de consumidores y cambio | Arquitectura 02/04; G02 como antecedente de registro | Recepción por campo y uso, versiones de premisas y propagación por impacto material, sin nueva estructura de maestros |

La arquitectura conserva su mapa de diecisiete nodos y la relación con los once pasos de origen. FND02 desarrolla N01/N02 y la semántica compartida necesaria para sus consumidores. No reduce ni sustituye los nodos posteriores, ni acredita su implementación.

## Cobertura de la revisión documental

La revisión del componente corresponde al asistente que lo redacta; no se presenta como revisión independiente. Examina contenido y archivos generales, sin ejecutar una prestación ni probar la metodología.

| Dimensión | Contenido revisable |
|---|---|
| Cobertura | Instrucciones N01/N02, contratos K01/K02, seis plantillas, guía de entrada y procedencia |
| Fundamento | Cada adaptación indica original leído o contrato de arquitectura; los límites de lectura permanecen explícitos |
| Análisis | Selección por decisión, causalidad y alternativas, reconciliación, transferencia A, capacidades B y suficiencia por uso |
| Coherencia | Autoridad separada de evidencia, recepción separada de resolución, E/O separados de obligatoriedad contractual, revisión por campos |
| Integridad y legibilidad | Enlaces locales, estructura de tablas, campos de valor vacíos, secuencia de lectura por tarea y vocabulario común |

Los resultados y el estado de cierre documental se conservan en el maestro de Evidencias vigente. Las instrucciones no dependen operativamente de los originales aquí identificados. La aplicación y las pruebas de la metodología permanecen posteriores a la construcción fundacional completa.
