# Go2Rev · N13 · Extensión por pregunta

Conjunto 0.4 · Compilación derivada, no fuente editable. El contenido expresamente incluido sustituye la apertura del original metodológico de esa versión; una sección no sustituye el resto del archivo. Las fuentes del encargo y del mercado requieren lectura efectiva.

Esta colección conserva archivos completos. Usar el índice de condiciones de la carga inicial y leer las secciones pertinentes; su presencia no acredita que se hayan consumido.

<a id="fuente-4692cc11a61d"></a>

## Fuente: 01_medicion_y_revision.md

Procedencia: `producto/metodo/medicion_preparacion_y_transferencia/v0.1/01_medicion_y_revision.md` · SHA256 `509df7814b0e3c36f524e68c3b0a2f4210e90870e1278134191262c8a610f95f` · Incluye: archivo íntegro.

# N13 · Medición y revisión para decidir

Versión 0.1 · Productor de K13

Empezar con la [primera pasada de N13](../../../metodo/operacion_conversacional/v0.3/10_primera_pasada.md#n13) y aplicar [núcleo y suficiencia](../../../metodo/operacion_conversacional/v0.3/12_nucleo_y_suficiencia.md). El procedimiento y contrato siguientes gobiernan el análisis completo.


<!-- procedimiento:inicio -->
## Procedimiento de primera pasada

Trabajar con la entrada común y aplicar [INV-01–20](../../../metodo/operacion_conversacional/v0.3/13_invariantes.md). Los identificadores de campos y bloques se localizan en la plantilla generada; la referencia posterior conserva el razonamiento y sus casos de aplicabilidad.

1. Partir de una decisión que necesita información y de los eventos K09–K12. Precisar objeto, identidad, fecha y unidad de análisis.
2. Definir captura, fuente, responsable, cálculo y corte de cada medida. Abrir relaciones y excepciones si hay agregación, duplicados, faltantes o transición entre sistemas.
3. Diseñar revisión e interpretación: condición, autoridad y acción ante el resultado. Abrir la ficha de revisión para vincular medida y decisión.
4. Entregar K13 a N15 para instrumentar y a N16 para comprobar contenido y funcionamiento pertinentes; mantener límites de cobertura y trazabilidad hasta el original.

**Bloques de salida:** K13.T01.B01. Su condición y momento gobiernan la exigibilidad; las piezas auxiliares se abren según la tarea.
<!-- procedimiento:fin -->

## Referencia sustantiva y condiciones de ampliación


## Pregunta y entradas

Determinar qué información permitiría mantener, ajustar, detener o reabrir una decisión, quién puede actuar y con qué oportunidad. Recibir objetivos/compromisos K01, hipótesis y condiciones K06, eventos K09–K11, magnitudes/umbrales K12 y fuentes/capacidades K02. Incorporar K07/K08 cuando la medida dependa de una versión de mensaje u oferta.

En A, comprobar que las definiciones y poblaciones del origen se transfieren al destino antes de reutilizar una línea base. En B, la ausencia de historial no impide diseñar observación; la línea base se conserva desconocida hasta obtenerla. Medición puede iniciarse para un protocolo de Diagnostic sin exigir Design completo.

## Construir el sistema de medidas

1. **Partir de la decisión.** Identificar compromiso, responsable, alternativas y tiempo en que la información sería útil. Explicar qué cambio de evidencia podría alterar la decisión. Eliminar medidas sin uso; conservar las necesarias para proteger calidad, capacidad o caja aunque no sean indicadores comerciales destacados.
2. **Reconstruir el mecanismo.** Conectar actividad del proveedor, señal del comprador, compra, cumplimiento y caja pertinentes. Separar resultados, condiciones y restricciones. Una medida anterior en el tiempo no es predictora solo por llamarla anticipada: la relación causal o predictiva conserva fundamento e incertidumbre.
3. **Definir el evento.** Describir qué sucede, en qué objeto, cómo se reconoce, fuente que lo acredita y cuándo ocurre. Diferenciar fecha del hecho, registro, recepción y corte. Emisión, aceptación, conformidad, facturación y cobro conservan eventos distintos.
4. **Definir identidad y cálculo.** Fijar unidad, población, inclusión/exclusión, deduplicación, ventana/cohorte, numerador/denominador y dominio. Aplicar las [reglas de cohortes de posición, demanda y conversión](../../../metodo/posicionamiento_demanda_y_conversion/v0.1/04_costes_cohortes_y_capacidad.md). Repeticiones cuentan para esfuerzo, pero no se convierten en nuevos compradores o pedidos.
5. **Resolver procedencia y disponibilidad.** Para cada entrada, identificar fuente, campo, acceso, calidad, responsable y transformación. Una medida derivada puede combinar varias fuentes; su cálculo tiene una definición vigente y una regla de conciliación. Designar una fuente de referencia no convierte sus datos en ciertos ni elimina discrepancias documentadas.
6. **Separar observación, referencia, objetivo y umbral.** La observación procede del proceso; una referencia externa tiene comparabilidad; el objetivo expresa aspiración/compromiso; el umbral determina una acción. Derivar este último de K12, condición de servicio, riesgo o pregunta de aprendizaje. Sin fundamento cuantitativo, formular condición cualitativa observable o relación simbólica; no inventar línea base, porcentaje de alerta ni intervalo.
7. **Diseñar captura y revisión proporcionadas.** Definir quién registra/calcula, quién interpreta/decide, latencia admisible y evento o periodo de revisión. Ajustar al tiempo de maduración y al plazo para actuar. Elegir medio suficiente manual o automatizado y valorar su mantenimiento en K12. No exigir reuniones, dashboard, North Star ni número fijo de métricas por rol.
8. **Entregar instrumentación y decisiones.** N15 recibe campo, fuente, transformación, acceso, presentación y tratamiento de errores. N16 recibe la trazabilidad a comprobar. N14 recibe lo que precise obtención adicional de evidencia. Cada medida entrega a N17 una instrucción de consulta y de actuación ante cambio.

## Reglas de cálculo e interpretación

| Magnitud | Relación general | Dominio y lectura |
|---|---|---|
| Conteo de eventos u objetos | Cardinalidad del conjunto definido al corte | Distinguir eventos repetidos y objetos únicos. Una fuente sin cobertura no acredita conteo total |
| Tasa de evento | Objetos elegibles con evento / objetos elegibles observados bajo la misma regla | Denominador positivo, identidad compatible y seguimiento pertinente; no contar desconocidos como ausencia de evento |
| Tasa agregada entre grupos disjuntos comparables | Suma de numeradores / suma de denominadores | No media simple de porcentajes. Si poblaciones, ventanas o definiciones difieren, mantener separado |
| Duración observada | Tiempo de fin menos origen según calendario | Separar espera y trabajo si la decisión lo requiere; los abiertos tienen seguimiento incompleto |
| Variación absoluta | Valor actual menos referencia comparable | Ambos conocidos, misma unidad/definición y periodo comparable; conservar signo e interpretación |
| Variación relativa | Diferencia dividida por referencia | Denominador con significado y no nulo; si cero, falta o cambio de signo impide interpretación, usar diferencia y explicación |
| Contribución, caja y carga | Fórmulas vigentes K12 con sus entradas | No redefinirlas en un reporte. Pedido, ingreso reconocido y efectivo cobrado conservan unidades y fechas propias |

La cobertura del dato es una condición del cálculo. Separar universo elegible conocido, observaciones disponibles, registros inválidos, pendientes y ausencia de acceso. Cero observado requiere un periodo/población con captura pertinente; una extracción vacía o fallida no se convierte automáticamente en cero de negocio. Si solo puede calcularse una parte, nombrar el subconjunto y limitar la conclusión.

Una comparación temporal puede cambiar por composición, estacionalidad, precio, oferta, canal o captura. Mostrar esos cambios antes de atribuir el efecto a una actuación. Muestras escasas y cohortes inmaduras no sostienen una tasa estable por repetir la lectura. La atribución comercial mantiene las reglas de posición, demanda y conversión; reparto de crédito no demuestra efecto incremental.

## Captura y corrección de datos

El diseño especifica origen → extracción/recepción → transformación → medida → decisión. Conserva localizador y revisión de la definición. Define unidades, calendario/zona, claves de relación, validaciones pertinentes y tratamiento de duplicados, eventos tardíos y estados contradictorios. No exige una arquitectura técnica nueva: puede resolverse con archivo y conciliación manual si cumple la tarea.

Si llega un dato tarde o se corrige una fuente, conservar el valor publicado al corte y emitir una revisión identificada. No sobrescribir el hecho original ni mezclar cálculos de definiciones incompatibles. Una redefinición puede requerir recalcular la serie desde datos aptos o marcar una discontinuidad; no empalmar series como si fueran equivalentes.

Ante fallo de captura, identificar tramo y datos afectados, detener solo decisiones que dependan de ellos y activar alternativa suficiente. Distinguir reparación técnica, corrección de dato y revisión de hipótesis de negocio. Los accesos y permisos se verifican para el dato necesario; una conexión activa no acredita cobertura ni exactitud.

## Revisión que termina en una decisión

El asistente prepara una lectura con ámbito/corte, qué cambió, calidad del dato, explicación sustentada, explicación contraria, efecto sobre K06–K12 y alternativas de acción. El decisor resuelve dentro de K01/DEC. Puede mantener la decisión cuando el dato aún no permita cambiarla, dejando condición y momento pertinente de revisión; no forzar una decisión nueva en cada reunión.

La [plantilla de revisión](../../../metodo/medicion_preparacion_y_transferencia/v0.1/plantillas/02_revision_y_decision.md) conserva responsable, acción, dependencia y condición de comprobación posterior. Un reporte entregado no acredita acción realizada. Si el umbral cambia, registrar motivo y autoridad antes de usarlo; no modificarlo retrospectivamente para presentar cumplimiento.

K13 es suficiente para diseño cuando evento/cálculo, fuente, dominio, responsable y decisión son ejecutables o sus carencias tienen efecto explícito. Para declarar captura disponible y uso comprobado se necesita evidencia de N15/N16 en la prestación. Cambios de oferta, recorrido, fuente, unidad, definición o umbral revisan K13 y sus consumidores mediante CAM.


## Correspondencia mínima con un CRM o registro

Diseñar únicamente los objetos necesarios para las decisiones: cuenta/unidad compradora, persona/rol, oportunidad o pedido, interacción/evento y entrega/cobro cuando proceda. Para cada objeto precisar identidad estable, relación con otros objetos, fuente de referencia, propietario, estados permitidos y evento que cambia el estado. Definir deduplicación, fecha del hecho y registro, campos obligatorios por transición, tratamiento de desconocidos, corrección y permisos.

N15 recibe una correspondencia entre ese contrato y los objetos, campos, relaciones y automatizaciones reales del medio elegido. Registrar qué queda manual, qué no se puede representar y su consecuencia. N16 comprueba captura, transición, conciliación y acceso del alcance configurado; N17 recibe instrucciones de uso y mantenimiento. Un archivo compartido puede ser suficiente si conserva estas funciones; no se impone un CRM ni una plataforma propia.


<a id="fuente-6b7560f1965b"></a>

## Fuente: 07_contratos_y_revision.md

Procedencia: `producto/metodo/medicion_preparacion_y_transferencia/v0.1/07_contratos_y_revision.md` · SHA256 `5ccd47f6d2445dfe69d3023246befc775bae6652958603b1b10656f383856f37` · Incluye: archivo íntegro.

# Contratos y revisión de preparación y transferencia

Versión 0.1 · K13–K17

## Semántica y responsabilidad

Aplicar el [diccionario común encargo y conocimiento](../../../metodo/encargo_y_conocimiento/v0.1/03_contratos_y_diccionario.md): K por productor, FUE/AF para conocimiento y originales, DEC para autoridad, HUE/SOL/CON para carencias y CAM para cambios. Los bloques de medida, protocolo, pieza y observación son secciones localizables de K13–K17; no crean registros maestros ni taxonomías de procedencia paralelos.

Cada artefacto identifica K01, revisión, ámbito, autor/fecha, estado documental y ubicación. Cada campo material consumido identifica productor, revisión, naturaleza/fundamento, unidad/periodo cuando proceda y límite. La recepción es admitido, admitido con límites o devuelto con razón, productor y corrección requerida. No exige revisar todo un nodo para consumir un campo suficiente.

E y O indican uso, no verdad o permiso. Un protocolo E puede preparar una obtención necesaria para Diagnostic antes de K06 final. O requiere condiciones de preparación pertinentes; no se asigna por aprobar el diseño. El asistente redacta y analiza; consultor responde de calidad; patrocinador decide compromisos; operador/propietario confirman condiciones exclusivas y realizan las acciones que les corresponden.

## Productores y recepción

| Productor | Entradas pertinentes | Salida consumible | Condición de recepción |
|---|---|---|---|
| N13 | K01/K06 decisiones, K09–K11 eventos, K12 magnitudes, K02 fuentes/CAP | K13 definición de evento/medida, población/corte, cálculo/dominio, fuente, captura, responsable, umbral/decisión y revisión | N14/N15 pueden preparar desde definición y carencias explícitas; uso de una cifra exige cobertura y fundamento pertinentes |
| N14 | K01 obligaciones/autoridad, K06 o pregunta exploratoria, campos disponibles K07–K13, CAP | K14 inventario de obligaciones/piezas, dependencia, recurso, protocolo previo, secuencia, límites y criterio de fin | N15 recibe contenido y medio necesarios; N16 recibe criterio/procedimiento; recursos nominales no habilitan ejecución |
| N15 | K14 y contenidos K07–K13, medio/permiso | K15 pieza/fuente/vista, guía por tarea, configuración aplicada o pendiente, versión y evidencia de preparación material | N16 puede comprobar lo producido en su ámbito; una instrucción de configuración no sustituye su aplicación |
| N16 | K14 criterios previos, K15, entradas/operador/receptor/medios efectivos | K16 cobertura y resultado con original, contexto, ayuda, defecto, corrección y límites por versión | N17 recibe preparación acreditada o parcial; fallo vuelve al productor causal. Ausencia de observación no es cumplimiento |
| N17 | K01 condiciones/salida, K06/DEC, entregas y K13–K16 pertinentes | K17 índice actual, estado/fundamento, recepción, pendientes, continuidad, acceso y finalización del soporte | Receptor puede localizar y usar lo comprometido o recibe limitación expresa; cierre Diagnostic no exige construcción posterior |

## Intercambios con los componentes construidos

| Origen | Tratamiento en preparación y transferencia | Devolución cuando cambie la conclusión |
|---|---|---|
| encargo y conocimiento K01/K02 | Condiciones contractuales, fuentes, autoridad y disponibilidad se conservan por campo | N01 si cambia alcance/compromiso; N02 si cambia fuente, capacidad o carencia |
| investigación y Diagnostic N03–N06 | Investigación externa y contraste siguen siendo sustantivos; N14 prepara solo la obtención que falta | AF/FUE y razonamiento al analista productor; N06 revisa tesis/salida, no recibe un aprobado genérico de N16 |
| oferta, entrega y economía N08/N11/N12 | Piezas respetan oferta/entrega, unidades, dominio, carga y caja; N13 no inventa otra fórmula | Corregir productor y consumidores; no rellenar un dato económico ausente desde un protocolo |
| posición, demanda y conversión N07/N09/N10 | Mensajes, eventos, transiciones, cohortes y variantes determinan material/captura/cobertura | Cambios de comprador, señal, condición, coste o trabajo vuelven al nodo pertinente |

El [intercambio exploratorio](../../../metodo/investigacion_y_diagnostic/v0.2/06_contratos_y_economia_exploratoria.md) y los [consumidores posición, demanda y conversión](../../../metodo/posicionamiento_demanda_y_conversion/v0.1/06_contratos_y_revision.md) quedan desarrollados por estas instrucciones. La secuencia local pregunta → protocolo → piezas/medidas → comprobación pertinente → actuación autorizada → análisis evita exigir el cierre que precisamente se busca fundamentar. No necesita todo K07–K17 operativo para un protocolo acotado.

Las observaciones comerciales o de investigación se conservan en FUE/AF con protocolo y contexto; el productor de la pregunta interpreta su significado. K16 evalúa preparación de tareas y no sustituye N03–N06/N12. Ambas salidas pueden compartir soporte original sin duplicar ni ampliar su autoridad.

## Estados que no se intercambian

| Eje | Distinciones | Regla |
|---|---|---|
| Edición | Borrador, revisado, sustituido | Revisión documental identifica autor/cobertura; no prueba uso |
| Protocolo | Diseñado, preparado para ejecutar, ejecutado; no ejecutado/diferido con causa | Disponibilidad real y rastro sustentan los estados pertinentes |
| Evaluación de criterio | Cumplido, incumplido, inconcluyente, no ejecutado | Siempre vinculado a criterio, evidencia, contexto y versión; no aplica requiere razón de cobertura |
| Conocimiento | Observación, declaración, inferencia, hipótesis | La procedencia interna/externa/derivada permanece separada |
| Decisión/recepción | Autoridad y condiciones según DEC/K01 | No cambia la evidencia ni borra el pendiente aceptado |
| Preparación/entrega | Diseñada, preparada, comprobada; real observada en ámbito propio; parcial/condicionada cuando proceda | No ascenso automático por archivo completo, aprobación o una actuación favorable |

## Calidad y revisión ante cambios

Revisar cobertura de obligaciones/variantes, fundamento, razonamiento, coherencia entre contenidos/medios/recursos y utilidad para quien decide/actúa. Una incoherencia interna requiere corrección; la coherencia interna sola no demuestra calidad, verdad de premisas o preparación. No promediar criterios para compensar un compromiso imposible ni añadir gobierno por cada archivo.

| Cambio | Primera revisión | Consumidores materiales posibles |
|---|---|---|
| Fuente, definición, unidad, población o corte | Productor del dato y N13 | K12, K14/K15, interpretación K16 y decisiones dependientes |
| Criterio o alcance de protocolo | N14 y K01/DEC si cambia compromiso | K15, cobertura K16, conclusión N06/N17 |
| Promesa, oferta, transición o entrega | N07–N11 pertinente | K12/K13, inventario K14, piezas K15 y cobertura K16 |
| Medio, configuración, operador o disponibilidad | K02/N15 y dueño de recurso | K14/K16, capacidad K12 y continuidad K17 |
| Defecto observado o ayuda esencial | Productor causal | Piezas y cobertura dependientes; conservar observación original |
| Recepción, soporte o derechos de uso | K01/DEC y N17 | Alcance entregado, accesos y responsabilidades posteriores |

Registrar CAM con motivo/fuente, campo, versiones anterior/nueva, consumidores y disposición. Actualizar primero productor, luego dependientes. Justificar qué observaciones conservan validez y qué uso queda retirado hasta nueva comprobación. Una corrección de texto sin efecto de comportamiento no obliga a repetir el recorrido completo; una condición indispensable cambiada sí exige revisar su cobertura. No cambiar criterios retrospectivamente ni borrar fallos.

La [plantilla de decisiones/cambios encargo y conocimiento](../../../metodo/encargo_y_conocimiento/v0.1/plantillas/06_decisiones_y_cambios.md) mantiene el registro común. operación conversacional integra entrada global y capacidades del entorno; paquete de implementación identifica el paquete y su guía de implementación.


<a id="fuente-867a7f99cd43"></a>

## Fuente: 02_revision_y_decision.md

Procedencia: `producto/metodo/medicion_preparacion_y_transferencia/v0.1/plantillas/02_revision_y_decision.md` · SHA256 `9382b65d27328e5c49a562631505bde9be124cf71b6a8863d3568b39c6491671` · Incluye: archivo íntegro.

# Plantilla de revisión y decisión

Vista generada · Corregir la [definición de campos](../../../metodo/esquema/v0.1/plantillas.json), no esta vista. ★ = campo de la plantilla principal: aplicar condición y momento; las piezas auxiliares pueden ser indispensables. Cabecera: identidad, versión, ámbito y K01, autor y fecha, ubicación, estado documental, receptor y uso. Registrar una vez por artefacto; los bloques remiten a ella. FUE, AF y otros registros con identidad propia conservan sus metadatos. La aceptación se localiza en DEC.


Versión 0.1 · Sección K13 con referencias AF/DEC · Campos empresariales vacíos

Usar con [medición y revisión](../../../metodo/medicion_preparacion_y_transferencia/v0.1/01_medicion_y_revision.md). El asistente prepara análisis y recomendación; la autoridad correspondiente decide. Puede agruparse con las medidas y el registro común de decisiones, sin crear un acta maestra adicional.

<a id="k13-t02-b01"></a>

<!-- bloque: K13.T02.B01 -->
| Campo | Regla | Valor |
|---|---|---|
| Referencia | K13/sección/revisión, autor, fecha y estado documental |  |
| Ámbito y motivo | K01/revisión, población/recorrido y decisión que justifica la lectura |  |
| Corte y definiciones | Fecha/ventana, medida/revisión y naturaleza de los datos |  |
| Fuentes y cobertura | AF/FUE, disponibilidad, completitud y cambios de captura/definición |  |
| Observación | Qué se conoce bajo esas definiciones; separar resultado parcial, pendiente y desconocido |  |
| Comparación | Referencia compatible, diferencia y límite; no empalmar series incompatibles |  |
| Umbral pertinente | Criterio previo, fundamento, autoridad y condición de aplicación |  |
| Explicación sustentada | Premisas, mecanismo y razonamiento que conecta datos con decisión |  |
| Explicación contraria | Otras causas compatibles, cambios simultáneos y evidencia en contra |  |
| Efecto en el sistema | Campos/revisiones K06–K12 u otros que dependen del hallazgo |  |
| Alternativas de acción | Mantener, ajustar, detener, reabrir u obtener evidencia; consecuencias y recursos |  |
| Recomendación | Motivo, límites y condición que la cambiaría; sin forzar una acción nueva por cada revisión |  |
| Decisión | Referencia DEC, autoridad, disposición y compromiso realmente habilitado |  |
| Acción y receptor | Responsable, entrada/salida, lugar de registro, disponibilidad y recepción |  |
| Condición posterior | Cuándo comprobar efecto/cumplimiento, con qué evidencia y qué ocurrirá si no llega |  |
| Pendientes | HUE/CON, motivo, alcance limitado y productor de corrección/obtención |  |
| Cambio y conservación | CAM si procede; datos publicados al corte y revisión posterior separados |  |

La emisión del reporte no significa que la acción se haya realizado. Conservar la decisión en el [registro común](../../../metodo/encargo_y_conocimiento/v0.1/plantillas/06_decisiones_y_cambios.md) y referenciarla aquí.

## Aplicabilidad de los bloques

Antes de emitir K13, completar el núcleo de [N13 Instrumentar para decidir](../../../metodo/operacion_conversacional/v0.3/10_primera_pasada.md). Las reglas CONTR, EVAL, USO y de variante de esta plantilla mantienen su momento de exigibilidad. Un bloque condicional se completa cuando afecte al resultado; documentar la condición que lo hace aplicable o su exclusión. Una ausencia material queda localizada y limita el uso dependiente. La cabecera común se registra una vez por artefacto.
