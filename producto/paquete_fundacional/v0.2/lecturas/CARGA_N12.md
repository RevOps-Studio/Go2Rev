# Go2Rev · Analizar economía y capacidad

Conjunto 0.2 · Compilación derivada; editar los originales identificados, no esta lectura.

Leer la entrada común CARGA_INICIO junto a la tarea. Esta carga reúne instrucción, contrato y recursos de la capacidad. Un enlace a un archivo adicional no acredita su lectura. Abrirlo cuando su condición o dependencia sea necesaria; si no está disponible, delimitar el uso dependiente.

## Archivos adicionales localizables

- producto/metodo/encargo_y_conocimiento/v0.1/03_contratos_y_diccionario.md
- producto/metodo/investigacion_y_diagnostic/v0.2/plantillas/06_intercambio_exploratorio.md
- producto/metodo/oferta_entrega_y_economia/v0.1/02_entrega_y_cobro.md
- producto/metodo/oferta_entrega_y_economia/v0.1/modelo/Go2Rev_modelo_economico_v0.1.xlsx
- producto/metodo/oferta_entrega_y_economia/v0.1/modelo/definicion_modelo.mjs
- producto/metodo/operacion_conversacional/v0.2/10_primera_pasada.md
- producto/metodo/operacion_conversacional/v0.2/12_nucleo_y_suficiencia.md

## N12 Analizar economía y capacidad

**Entrada.** Combinación K08–K11 con unidades, periodos y fundamentos.

**Primera pasada.** Conciliar partidas y recursos, calcular relaciones con dominio, localizar restricciones y comparar alternativas o umbrales.

**Núcleo de K12.** Perímetro y combinación; entradas y naturaleza; costes sin doble imputación; capacidad; caja; conclusión y límites.

**Cierre y ampliación.** Calcular cada bloque suficiente y mostrar lo ausente. Las relaciones adicionales de la variante deben quedar explícitas antes de concluir.

**Destino.** 01 Entregables/Economia. Aplicar fuente editable, vista e índice de la convención común.

**Instrucción y contrato.** [Procedimiento](#fuente-1) · [Contrato](#fuente-2).

<a id="n13"></a>



<a id="fuente-1"></a>

## Fuente: producto/metodo/oferta_entrega_y_economia/v0.1/03_economia_y_capacidad.md

SHA256: 2b4b834f12a964a9d78e4b51806a8d66582c0f081c9de7176aed99c50b7b55d3

# N12 · Economía y capacidad

Versión 0.1 · Productor de K12

Empezar con la primera pasada de N12 (archivo adicional: producto/metodo/operacion_conversacional/v0.2/10_primera_pasada.md#n12) y aplicar núcleo y suficiencia (archivo adicional: producto/metodo/operacion_conversacional/v0.2/12_nucleo_y_suficiencia.md). El procedimiento y contrato siguientes gobiernan el análisis completo.

## Pregunta y perímetro

Determinar qué puede sostenerse bajo una combinación explícita, qué impide comprometerla y qué cambio merece consideración. Separar economía de la iniciativa, economía de prestar Go2Rev y desarrollo del producto.

Recibir K08 unidad/condiciones, K09 actividad y coste de toda la cohorte, K10 esfuerzo comercial y tiempos, K11 trabajo/cobro/pago y K02 recursos. E no exige K06 final. Si falta acceso o compra, calcular las partes sustentadas y declarar adquisición/venta incompletas; no emitir una conclusión integral de sostenibilidad con esa ausencia.

## Construcción del modelo

1. **Fijar contrato.** Definir combinación y revisiones, decisión, periodo/horizonte, moneda/escala, unidades y conversiones, alcance económico, tratamiento de impuestos, reconocimiento y exclusiones. Diferenciar unidad vendida, producida, entregada, reconocida y cobrada. Seleccionar las [variantes](#fuente-8) pertinentes y su resolución.
2. **Descomponer entradas.** Cada cantidad tiene campo, valor o desconocido, unidad, población/periodo, AF/FUE, naturaleza, transformación y uso admitido. Etiquetar rango solo con fundamento de límites. Un dato público sobre otro contexto puede informar una hipótesis; no adquiere naturaleza observada propia. Una conclusión del contraste puede exigir una nueva partida o restricción omitida por el cliente.
3. **Reconciliar partidas.** Usar el [registro de partidas y recursos](#fuente-3). Para cada partida identificar objeto de coste, impulsor, cantidad/tarifa, moneda, reconocimiento, pago, comportamiento en rango, cobertura e inclusión. Clasificar variable, fijo relevante, lote, escalón, inversión o ajuste sin imponer un comportamiento fuera de su rango. Identificar qué ya está incluido en otra partida y qué queda excluido de la suma.
4. **Distinguir decisiones económicas.** El coste incremental ayuda a decidir una unidad adicional con recursos ociosos; el resultado con fijos pertinentes ayuda a valorar sostenibilidad. Separar costes hundidos de compromisos futuros evitables y de asignaciones. Una asignación contable no es pago nuevo; un salario fijo sigue siendo coste del periodo aunque no incremente con una venta. Coste de oportunidad se muestra separado, con alternativa factible y fundamento, sin sumarlo también como desembolso.
5. **Calcular por relaciones.** Aplicar [fórmulas y dominio](#fuente-7), mostrando cantidad, tarifa, subtotales y resultado. Incluir preparación y todos los intentos de adquisición/venta con su cohorte; mantener idéntico coste total si se redistribuye por unidades. Evitar sumar CAC y las partidas que ya lo forman. Un CAC no observado no aparece como cifra histórica.
6. **Resolver capacidad.** Descomponer carga por recurso, lote, preparación y unidad, restar compromisos ajenos al ámbito y respetar calendarios. Comprobar escasez conocida antes de buscar una capacidad agregada. Con varias ofertas, usar vector de demanda/carga y restricciones compartidas. Una mezcla favorable en contribución puede incumplir el recurso escaso. Si falta un recurso indispensable, conservar el límite parcial; no sustituirlo por disponibilidad infinita.
7. **Resolver caja.** Construir eventos ordenados con importes y condiciones desde K11. Separar ingresos/costes reconocidos de cobros/pagos, inversión y financiación. Conciliar saldos por evento incluyendo el inicial; revisar mínimos antes de agregarlos por periodo. No financiar automáticamente un déficit con una línea no disponible. Un calendario o importe desconocido limita la necesidad de financiación que pueda afirmarse.
8. **Analizar cambio.** Usar [comparación y umbrales](#fuente-9). Cuestionar una premisa material y explicar alternativa, efecto conjunto y condición contraria. Mantener efectos sobre calidad, compra, coste, recurso y caja. No completar cifras para ordenar opciones si las ausencias pueden invertir ese orden.
9. **Devolver recomendación.** K12 identifica resultados calculables, parciales y no calculables; contribución, resultado pertinente, capacidad, caja, equilibrio/cruce cuando existan, restricciones, umbral, evidencia necesaria e implicaciones para N06/N08–N11. Un cálculo coherente no demuestra demanda, aceptación de precio ni ejecución.

## Suficiencia y gobierno

La cobertura se juzga para el compromiso. E puede servir para descartar una combinación por imposibilidad conocida, priorizar una pregunta o recomendar evidencia adicional con una economía parcial. Para O deben existir condiciones actuales suficientes de coste, recursos y caja; la comprobación de preparación corresponde a N14–N16 en su futura ejecución. La admisión documental de K12 no es autorización de gasto.

El consultor responde del modelo y razonamiento. Finanzas, operación y propietarios aportan datos exclusivos y confirman su significado; el patrocinador decide riesgo e inversión. Si un parámetro queda pendiente, identificar HUE, fuente alternativa, responsable y uso detenido. No exigir reconstruir toda la economía de una organización para una decisión acotada.

El modelo editable (archivo adicional: producto/metodo/oferta_entrega_y_economia/v0.1/modelo/Go2Rev_modelo_economico_v0.1.xlsx) implementa un núcleo explícito y extensiones de stock/recurrencia; su [guía](#fuente-10) delimita capacidades. Las fórmulas generales incluyen relaciones que pueden precisar adaptación documentada de la fuente de cálculo. No se denomina calculadora universal ni se presenta el resultado parcial como resultado contable completo.

## Revisión ante cambios

Una revisión de precio, unidad, mezcla, respuesta, esfuerzo, proveedor, capacidad, calidad, plazo o condición de pago obliga a localizar entradas dependientes, revisar sus transformaciones, recalcular lo afectado en la prestación y devolver consecuencias antes del siguiente compromiso. Registrar CAM con versiones y conservar DEC previas. No repetir nodos sin impacto. Un cambio de cantidad afecta también a lotes/escalones y, si altera respuesta o calendario, a adquisición y caja.


<a id="fuente-2"></a>

## Fuente: producto/metodo/oferta_entrega_y_economia/v0.1/07_contratos_y_revision.md

SHA256: d40278ad560106df4032b38bedf5347f484b4c4c163c88ef3ff584dbf95b1aa0

# Contratos y revisión de cambios

Versión 0.1 · K08/K11/K12

## Contrato común

Aplicar el diccionario encargo y conocimiento (archivo adicional: producto/metodo/encargo_y_conocimiento/v0.1/03_contratos_y_diccionario.md): FUE original localizable, AF con naturaleza/procedencia y razonamiento si es derivada, DEC con autoridad, HUE/SOL para carencias, CON solo para incompatibilidades comparables y CAM por impacto. No añadir taxonomías paralelas ni registros de cada frase.

Cada artefacto identifica K01, revisión, autor/fecha, ámbito, estado documental, entradas y ubicación; cada relación de consumo identifica campo, versión, consumidor, uso E/O, admisión/límite/devolución y corrección responsable. E y O no son niveles de evidencia. Los campos requeridos ausentes se declaran desconocidos; no aplica se justifica. Solo la plantilla sin utilizar conserva campos vacíos.

## Productores y campos consumibles

| Productor | Entrada para E | Campos de salida | Consumidores y recepción |
|---|---|---|---|
| N08 | K01/K02, situación K04 y alternativas K05 con su estado; restricciones disponibles K11/K12 | K08 unidad y conversiones, destinatarios, contenido/exclusiones, compromisos y fundamento, configuración, mecanismo/precio/condiciones, costes y recursos pendientes | N06 compara; N07 coherencia; N09/N10 comunican; N11 cumple; N12 calcula; N15 materializa. Rechazar economía sin unidad o comunicación que exceda evidencia/autoridad |
| N11 | K08 representable, K02 medios, K03 requisitos, K04 aceptación; representación de K10 cuando se necesite | K11 trabajo/precedencias, roles y disponibilidad, insumos, traspasos, conformidad, costes, eventos de cobro/pago, incidencias y cierre | N06 restricciones; N08 alcance; N10 condiciones de inicio; N12 carga/caja; N13 eventos; N14–N16 preparación. Limitar la promesa si falta un recurso o condición indispensable |
| N12 | Unidad K08; acceso K09 y compra K10 E con cohorte/esfuerzo; tareas/condiciones K11 y recursos K02 | K12 perímetro, fuentes editables, fórmulas/dominio, cobertura/ausencias, contribución/resultado, capacidad, caja, comparación/umbral y recomendación | N06 tesis; N08 precio/condiciones; N09–N11 límites; N13 magnitudes; N14 evidencia requerida. Un resultado parcial solo habilita una conclusión que no dependa de lo ausente |

Después de K06/DEC, añadir alcance habilitado, K07/K09/K10 de diseño y condiciones concretas. El diseño autorizado permanece distinto de preparación efectiva. Para O se requieren condiciones y observaciones pertinentes de N14–N16, además de suficiencia de las entradas. No crear un circuito que exija O para poder producir E.

## Intercambio con Diagnostic

Usar la combinación localizada por K06/revisión/sección y el intercambio de investigación y Diagnostic (archivo adicional: producto/metodo/investigacion_y_diagnostic/v0.2/plantillas/06_intercambio_exploratorio.md). N08/N11/N12 devuelven aquí sus productores sustantivos. N09/N10 mantienen el contrato existente y se desarrollan en posición, demanda y conversión; un dato aún no disponible conserva su efecto, sin sustituirlo por un supuesto arbitrario.

El orden es representación de oferta → acceso/compra y cumplimiento → economía de la misma combinación → revisión de pregunta o configuración → recomendación N06. Se pueden avanzar ramas independientes. No contar como dos ventas la operación con intermediario y la venta al usuario ni mezclar el precio de una oferta con los costes favorables de otra.

Cada conclusión que provenga del cruce externo/interno referencia las AF de ambos lados, comparabilidad, mecanismo y AF derivada. N08 recibe implicaciones para unidad/precio/condiciones; N11 para requisitos y recursos; N12 para parámetros, partidas nuevas, rango y horizonte. Una referencia externa sin original leído no entra como evidencia por figurar en el conjunto de investigación o estar conectada por MCP.

## Suficiencia y calidad por uso

| Dimensión | Revisión documental del contenido | Consecuencia de carencia en la prestación |
|---|---|---|
| Cobertura | Promesas enlazadas con tareas; partidas con costes; recursos completos; caja con obligaciones; variantes pertinentes resueltas | Limitar resultado, recomendación o compromiso dependiente |
| Fundamento | Valor, referencia y evidencia separados; transformaciones comparables y AF localizables | Tratar como hipótesis/desconocido, investigar o devolver |
| Razonamiento | Mecanismo de precio, alternativa, efecto conjunto, refutación y umbral | Completar análisis antes de recomendar |
| Coherencia | Misma combinación/unidad/periodo; costes una vez; fórmulas en dominio; recursos y fechas compatibles | Corregir productor y recalcular consumidores afectados |
| Utilidad | Entrega comprensible, editable, con siguiente decisión y responsable | Corregir representación; no trasladar el análisis pendiente al cliente |

No promediar estas dimensiones para compensar una imposibilidad. La revisión de construcción examina que las instrucciones y campos permiten resolverlas; no afirma haber observado su cumplimiento en una empresa.

## Cambios y autoridad

| Cambio material | Productor a revisar primero | Consumidores posibles según uso real |
|---|---|---|
| Unidad, alcance, descuento o condición de precio | N08; N11/N12 para su efecto | N06/N07/N09/N10/N15 |
| Recurso, proveedor, calidad, tiempo o aceptación | N11 y K02; después N12 | N06/N08/N10/N13–N16 |
| Coste, cohorte, mezcla, financiación o calendario | Productor del dato; después N12 | N06/N08–N11/N13/N14 |
| Hallazgo externo que cambia una premisa | N03–N05 y AF derivada | Campos afectados de N08/N11/N12 y tesis N06 |

Registrar CAM con campo y valor/condición anterior/nueva, motivo y fuente, versiones y efecto. Actualizar primero productor y después relaciones reales de consumo. Retirar el uso dependiente cuando una premisa indispensable deja de sostenerlo; no borrar eventos históricos. Si no hay impacto, explicar por qué sin rehacer todo el nodo.

El consultor revisa y recomienda; responsables exclusivos confirman condiciones propias; patrocinador autoriza inversión, precio y excepciones cuando le correspondan. K01 gobierna cambios de encargo. Una decisión interna no concede derechos externos ni convierte disponibilidad declarada en comprobada.


<a id="fuente-3"></a>

## Fuente: producto/metodo/oferta_entrega_y_economia/v0.1/plantillas/03_partidas_y_recursos.md

SHA256: 325c02c5c5c63750e93c7c855224b08fa9f376d8164c5e94f42124b2a933df97

# Plantilla · Partidas y recursos de K11/K12

Versión 0.1 · [Instrucción económica](#fuente-1)

Repetir por partida o recurso material. Un identificador local dentro de K11/K12 basta; FUE y AF conservan la procedencia.

| Campo | Regla | Valor |
|---|---|---|
| Cabecera y combinación | K11/K12, revisión, K01, periodo, moneda y ámbito | |
| Partida y objeto | ID, trabajo/insumo, unidad de oferta y responsable | |
| Cantidad y tarifa | Valor o desconocido de cada factor; unidades compatibles | |
| Fórmula e importe | Relación, dominio, transformación y moneda | |
| Fundamento por entrada | AF/FUE, naturaleza, periodo, campo y revisión | |
| Cobertura | Completa para uso delimitado o parcial; omisión y efecto | |
| Comportamiento | Variable/fijo/lote/escalón/inversión/ajuste y rango de validez | |
| Reconocimiento | Periodo y regla económica, con responsable competente si precisa | |
| Pago | Evento/fecha/regla, contraparte y condición | |
| Imputación | Incluida aquí o dentro de otra partida; referencia y conciliación | |
| Decisión incremental | Evitable/comprometida/hundida/asignada y fundamento | |
| Recurso | Identidad, rol/medio, unidad de disponibilidad y competencia | |
| Disponibilidad | Cantidad por calendario, fuente, CAP/TRA y límites | |
| Otros compromisos | Carga ya consumida fuera de la combinación | |
| Carga propia | Preparación, lote, unidad, comercial/soporte e incidencias | |
| Sustitución | Alternativa, equivalencia por comprobar y efecto en coste/calidad | |
| Restricción | Holgura/cota o desconocido; fecha y concurrencia pertinentes | |
| Coste de oportunidad | Uso alternativo factible, fundamento y presentación separada | |
| Revisión y consumo | Cambio, productor/receptor, uso y condición de admisión | |

## Aplicabilidad de los bloques

Antes de emitir K12, completar el núcleo de N12 Analizar economía y capacidad (archivo adicional: producto/metodo/operacion_conversacional/v0.2/10_primera_pasada.md). Las reglas CONTR, EVAL, USO y de variante de esta plantilla mantienen su momento de exigibilidad. Un bloque condicional se completa cuando afecte al resultado; documentar la condición que lo hace aplicable o su exclusión. Una ausencia material queda localizada y limita el uso dependiente. La cabecera común se registra una vez por artefacto.


<a id="fuente-4"></a>

## Fuente: producto/metodo/oferta_entrega_y_economia/v0.1/plantillas/04_eventos_de_caja.md

SHA256: 8d768452a7f4519b31a26a1cdd6a78b859c3af80a248da13f3de82cf8eb49d2d

# Plantilla · Eventos de cobro y pago

Versión 0.1 · Entrega y cobro (archivo adicional: producto/metodo/oferta_entrega_y_economia/v0.1/02_entrega_y_cobro.md) · [Fórmulas](#fuente-7)

Repetir por obligación/evento. Mantener separados evento previsto, condición acordada y movimiento observado.

| Campo | Regla | Valor |
|---|---|---|
| Cabecera | K11/K12, revisión, combinación, horizonte, moneda y escala | |
| Saldo inicial | Importe, fecha, procedencia y disponibilidad efectiva | |
| Reserva mínima | Regla/importe, horizonte y autoridad; no porcentaje universal | |
| Evento | ID, obligación, contraparte y vínculo con oferta/tarea | |
| Naturaleza | Cobro, pago, devolución, inversión, tributo o financiación pertinente | |
| Importe y base | Valor o desconocido, moneda/impuestos y fórmula de la obligación | |
| Condición | Qué habilita el evento y quién tiene autoridad | |
| Fecha y orden | Fecha/regla, evento de origen, calendario y secuencia intradía | |
| Fundamento | AF/FUE, naturaleza de afirmación, revisión y límites | |
| Reconocimiento económico | Relación con ingreso/coste, inversión u otra clasificación | |
| Financiación | Disponibilidad/condiciones acreditadas, vencimiento y pagos asociados | |
| Incidencia | Retraso, disputa, impago/devolución y efecto sobre saldo/plazo | |
| Movimiento observado | Comprobante/importe/fecha/aplicación solo cuando exista | |
| Cobertura del calendario | Obligaciones incluidas, ausentes y conclusión que limitan | |
| Resultado y brecha | Saldos, mínimo incluyendo inicio y financiación adicional necesaria | |
| Consumo y revisión | Campos/revisiones consumidores, admisión/límite y CAM | |

## Aplicabilidad de los bloques

Antes de emitir K12, completar el núcleo de N12 Analizar economía y capacidad (archivo adicional: producto/metodo/operacion_conversacional/v0.2/10_primera_pasada.md). Las reglas CONTR, EVAL, USO y de variante de esta plantilla mantienen su momento de exigibilidad. Un bloque condicional se completa cuando afecte al resultado; documentar la condición que lo hace aplicable o su exclusión. Una ausencia material queda localizada y limita el uso dependiente. La cabecera común se registra una vez por artefacto.


<a id="fuente-5"></a>

## Fuente: producto/metodo/oferta_entrega_y_economia/v0.1/plantillas/05_modelo_y_conclusion.md

SHA256: e84c9a2721790980ccffce8dbda179757dfa789b9a45726a27568b4bbd5dfd33

# Plantilla · K12 Modelo y conclusión

Versión 0.1 · [Instrucción](#fuente-1) · [Guía del libro](#fuente-10)

| Campo | Regla | Valor |
|---|---|---|
| Cabecera | K12, K01, revisión, autor/fecha, ámbito, estado y ubicación | |
| Pregunta y uso | Decisión y compromiso, E/O y límites | |
| Combinación | K06/revisión/sección; K08/K09/K10/K11 y campos compatibles | |
| Perímetro | Iniciativa, prestación de Go2Rev o desarrollo separados | |
| Unidades y conversión | Venta, producción, entrega, reconocimiento, facturación y cobro | |
| Periodo y moneda | Calendario, horizonte, escala, conversión y fuentes | |
| Base económica | Reconocimiento, impuestos, inclusiones/exclusiones y responsable | |
| Variantes pertinentes | Modelo de oferta/canal y relación resuelta, desconocida o no aplicable justificada | |
| Fuente editable | Archivo, revisión, hojas/celdas o secciones y motor empleado | |
| Parámetros | Valor/desconocido, unidad, AF/FUE y transformación por entrada material | |
| Cobertura de costes | Variables, comerciales/cohortes, fijos, lotes/escalones, inversión y no duplicación | |
| Capacidad | Recursos indispensables, cargas, disponibilidad/calendario y restricciones | |
| Caja | Eventos/fechas, saldo inicial, reserva, financiación y cobertura | |
| Fórmulas y dominio | Relaciones, supuestos de validez y dependencias | |
| Resultados | Contribución, resultado pertinente, equilibrio, capacidad y caja calculables | |
| No calculable o parcial | Entrada ausente/ inválida y magnitud/decisión limitada | |
| Contraste externo/interno | AF, comparabilidad, conclusión derivada y parámetro/relación afectada | |
| Comparación | Referencia a configuraciones y versiones, efectos y umbral | |
| Recomendación | Decisión propuesta, fundamento, restricciones y condición contraria | |
| Evidencia requerida | Pregunta, fuente/actuación pertinente, responsable, HUE/SOL o N14 | |
| Autoridad y disposición | DEC para inversión/riesgo/compromiso; revisión de consultor separada | |
| Consumo y revisión | Campo/versión/receptor/uso/admisión, disparador y CAM | |

## Aplicabilidad de los bloques

Antes de emitir K12, completar el núcleo de N12 Analizar economía y capacidad (archivo adicional: producto/metodo/operacion_conversacional/v0.2/10_primera_pasada.md). Las reglas CONTR, EVAL, USO y de variante de esta plantilla mantienen su momento de exigibilidad. Un bloque condicional se completa cuando afecte al resultado; documentar la condición que lo hace aplicable o su exclusión. Una ausencia material queda localizada y limita el uso dependiente. La cabecera común se registra una vez por artefacto.


<a id="fuente-6"></a>

## Fuente: producto/metodo/oferta_entrega_y_economia/v0.1/plantillas/06_comparacion.md

SHA256: 368c77040af5421997dec6a2091c80cb1436fa1bafe70f9fca7f1c19a85bc7c4

# Plantilla · Comparación y umbral

Versión 0.1 · [Instrucción](#fuente-9)

Repetir por alternativa material. No presupone un número de alternativas ni datos para poder redactar el método.

| Campo | Regla | Valor |
|---|---|---|
| Pregunta | Qué decisión podría cambiar y compromiso K01/K06 | |
| Referencia | Combinación, versiones y alternativa de mantener/no invertir pertinente | |
| Premisa cuestionada | AF interna y contraste externo o hallazgo nuevo | |
| Alternativa | Cambio de unidad, trabajo, recurso, alcance o condición | |
| Mecanismo | Por qué cambiarían coste, calidad, compra, capacidad o caja | |
| Comparabilidad | Mismo trabajo/horizonte/moneda; diferencias o conversiones | |
| Entradas afectadas | Campo, versión, fuente, valor/intervalo/desconocido y dominio | |
| Efectos conjuntos | Coste inicial/repetido, calidad, respuesta, recurso y calendario | |
| Desfavorable | Causa, límites sustentados, dependencias y evidencia contraria | |
| Fuente de cada cálculo | Libro/sección/revisión y parámetros conservados | |
| Diferencias | Contribución, resultado, capacidad y caja con alcance calculable | |
| Cruce o equilibrio | Fórmula, dominio, capacidad y resultado si calculable | |
| Umbral de decisión | Variable o condición que invertiría recomendación y fundamento | |
| Evidencia necesaria | Fuente/actuación, criterio de decisión y consumidor | |
| Recomendación | Preferencia, conflicto de criterios, límites o ausencia de orden concluyente | |
| DEC y revisión | Autoridad, disposición, disparador y versiones consumidoras | |

## Aplicabilidad de los bloques

Antes de emitir K12, completar el núcleo de N12 Analizar economía y capacidad (archivo adicional: producto/metodo/operacion_conversacional/v0.2/10_primera_pasada.md). Las reglas CONTR, EVAL, USO y de variante de esta plantilla mantienen su momento de exigibilidad. Un bloque condicional se completa cuando afecte al resultado; documentar la condición que lo hace aplicable o su exclusión. Una ausencia material queda localizada y limita el uso dependiente. La cabecera común se registra una vez por artefacto.


<a id="fuente-7"></a>

## Fuente: producto/metodo/oferta_entrega_y_economia/v0.1/04_formulas_y_dominio.md

SHA256: 2def2f551d8735ada9f424a4e421ece3b1f503b52d400a5c856807fe2b8731d9

# Fórmulas generales y dominio

Versión 0.1 · Especificación editable de N12

Las relaciones siguientes son reglas del producto, sin parámetros de una empresa. En una prestación, toda entrada numérica requiere valor finito, unidad, periodo/población, procedencia y cobertura. Un desconocido se propaga a las magnitudes dependientes; cero se admite únicamente como valor sustentado. Un cociente exige denominador válido. No se ocultan errores sustituyéndolos por cero.

## Notación y alcance

`i` identifica una unidad de oferta; `r`, un recurso no intercambiable; `t`, un periodo o evento ordenado; `k`, una cohorte de adquisición. `q_i` es cantidad reconocida en el periodo; `p_i`, ingreso neto por esa unidad; `v_i`, coste variable pertinente por unidad; `F`, costes fijos pertinentes del mismo periodo; `M`, moneda homogénea. Las conversiones entre vendido, fabricado, entregado, facturable y reconocido deben estar documentadas. Si no coinciden, construir sus movimientos por evento antes de usar `q_i`.

Ingresos, costes y caja tienen bases distintas. El resultado aquí es **resultado económico del perímetro modelado**, con inclusiones declaradas; no se etiqueta automáticamente EBITDA, beneficio contable o renta fiscal. Impuestos recuperables/no recuperables, reconocimiento, depreciación, intereses y otras partidas materiales se resuelven con criterio pertinente, no por un porcentaje universal. Una conversión de moneda identifica tasa, fecha, fuente y sensibilidad; no se suman monedas antes de convertir.

## Precio y contribución

| Relación | Fórmula general | Dominio y límite |
|---|---|---|
| Descuentos sucesivos sobre precio de lista | `p = P × producto(1 − d_j) − D` | `P ≥ 0`, cada `0 ≤ d_j ≤ 1`, `D ≥ 0`; orden y base de D explícitos, `p ≥ 0`. No aplica si el contrato usa otra base |
| Comisión o tarifa porcentual | `c = a × b` | `a` tasa y `b` base contractual compatible; no asumir que b es siempre p |
| Coste por impulsor | `C = cantidad × tarifa` | Mismas unidades de impulsor y periodo; no omitir uno por estar vacío |
| Contribución unitaria | `m_i = p_i − v_i` | `v_i` incluye variables de entrega y comerciales pertinentes sin duplicación; m puede ser negativa |
| Margen de contribución | `m_i / p_i` | Solo `p_i > 0`; margen no equivale a recargo sobre coste |
| Ingreso del periodo | `R = suma(q_i × p_i)` | Cantidades no negativas y compatibles con reconocimiento. Abonos se reconcilian por separado o dentro de p, una vez |
| Contribución del periodo | `MC = suma(q_i × m_i)` | Misma cobertura de costes por cada unidad |
| Resultado del perímetro | `Π = MC − F` | Mezcla/rango en que v y F son válidos; incorporar costes por lote/escalón si no están incluidos |

Separar contribución antes de adquisición de contribución después de variables comerciales cuando ayude a decidir. Si el gasto de adquisición de una cohorte se incluye como coste del periodo, no volver a deducir su asignación unitaria. Si se distribuye entre unidades, verificar que cantidades por asignación reproducen el total pertinente y el mismo horizonte. Los intentos sin venta permanecen en el coste.

Una oferta de ingreso cero puede analizarse con sus costes y contribución negativa; no tiene margen sobre ingreso ni un precio aceptado positivo. Una devolución puede reducir ingresos y generar coste adicional; no tratar el mero retorno físico como recuperación de todo el ingreso/coste.

## Equilibrio y umbrales de precio

Con una unidad homogénea, `m > 0` y `F ≥ 0`, el volumen continuo de equilibrio es `q* = F / m`. Si la unidad es indivisible, el mínimo entero que cubre F es `techo(F/m)`. Confirmar que el volumen cae en el rango de costes y capacidad y que el calendario permite realizarlo. Equilibrio económico no demuestra demanda ni financiación.

Si `m = 0`, con F positivo no hay volumen que lo cubra; con F cero el resultado es cero para cualquier volumen admisible. Si `m < 0`, aumentar volumen deteriora el resultado; con F no negativo no existe equilibrio positivo que mejore la situación. El punto q=0 con F=0 no justifica actividad sostenible. No dividir por un margen nulo ni devolver un número negativo como objetivo de ventas.

Si una unidad tiene coste independiente del precio `c` y coste proporcional `a × p`, entonces `m(p) = p(1−a)−c`. Para cubrir F con cantidad q y resultado objetivo T:

`p_requerido = (c + (F + T)/q) / (1−a)`

Dominio: `q > 0`, `0 ≤ a < 1`, `c,F ≥ 0`, T definido en M por periodo. El libro limita T a no negativo; una decisión de pérdida admisible se modela explícitamente fuera de ese bloque. Si costes, respuesta, alcance o capacidad cambian con p o q, esta expresión solo vale localmente y hay que recomponer las relaciones. No constituye disposición a pagar ni tarifa aprobada.

Para un precio de lista P positivo, un único descuento sobre esa base y sin otros cambios, `d_máximo = 1 − p_requerido/P`. Si resulta negativo, el precio de lista no cubre el umbral; no se convierte en descuento cero que aparenta suficiencia. El umbral no autoriza descontar. Condiciones comerciales, evidencia y autoridad siguen siendo necesarias.

## Mezcla, lotes y escalones

Con cantidades diferentes por unidad, conservar el vector `q = (q_i)` y calcular `Π(q) = suma(q_i m_i) − F(q) − suma(C_lote(q))`, evitando restar partidas ya incluidas en v o F. No dividir suma de unidades heterogéneas para inventar un margen unitario común.

Si la mezcla es estable y todas las cantidades usan una unidad agregable, pesos `w_i ≥ 0`, `suma(w_i)=1`, dan `m_mezcla = suma(w_i m_i)`. Solo si m_mezcla es positivo puede usarse `F/m_mezcla`. Cambiar mezcla, intervalos de descuento o recurso escaso exige recalcular. Para paquetes de proporción fija puede definirse una unidad compuesta con cantidades `a_i` documentadas y contribución `suma(a_i m_i)`; no se asume que cualquier mezcla sea ese paquete.

Para lotes indivisibles de tamaño b positivo, `n_lotes = techo(q/b)` y `C_lote = n_lotes × coste_por_lote`, bajo el alcance de ese lote. Con q cero, n_lotes es cero, salvo preparación comprometida independiente que se cuenta aparte. Identificar si el excedente se almacena, se pierde o sirve después; no reconocer automáticamente ingreso por lo producido.

Con costes escalonados, definir cada intervalo de cantidad, coste y capacidad, sin solapamientos ni huecos inadvertidos. Resolver equilibrio dentro de cada tramo y comprobar fronteras y pertenencia del resultado al tramo; el salto de coste puede eliminar un equilibrio aparente. No sustituir ese trabajo por F constante. En el libro básico, introducir una configuración de tramo explícita y devolver límites a K12; la fórmula simple no automatiza la elección entre tramos.

## Capacidad por recurso y calendario

Para recurso r, disponibilidad total `A_r`, carga de otros compromisos `B_r`, carga propia fija `S_r` (preparación y otro trabajo no ligado a q, desglosados), y consumo por unidad `h_ri`:

`L_r(q) = S_r + suma(q_i × h_ri) + carga_por_lotes_r(q)`

`holgura_r = A_r − B_r − L_r(q)`

Todos usan la misma unidad de recurso y periodo; A,B,S,h no negativos. Si existe carga comercial, soporte o incidencias pertinente, incluirla una vez como preparación, carga por unidad, por lote o bloque identificado. Una fuente que solo cubre entrega deja la capacidad integral incompleta.

Una combinación incumple una restricción conocida si alguna holgura es negativa; aunque falten otros recursos, esa incompatibilidad permanece. Holguras no negativas con un recurso indispensable desconocido no demuestran factibilidad. Para una sola unidad con consumo h_r positivo y preparaciones fijas, la cota es `min_r((A_r−B_r−S_r)/h_r)` entre recursos completos, truncando al entero inferior si la unidad es indivisible. Si A−B−S es negativo, ni la preparación cabe. Un h_r cero conocido no limita por repetición, pero su preparación sí puede limitar; nunca dividir por cero.

Para conservar una mezcla representada q y preparación fija, sea `V_r = suma(q_i h_ri)`. Si `V_r > 0`, el factor radial máximo es `(A_r−B_r−S_r)/V_r`, sujeto a las demás restricciones. Este factor escala proporcionalmente las cantidades; no es número de clientes, demanda ni óptimo de mezcla. Con cargas por lote o escalón hay que resolver de nuevo para cada escala; no se extrapola el factor. Si todos los V son cero, el factor no tiene significado de capacidad comercial ilimitada.

La carga por periodo no resuelve precedencias, reservas, simultaneidad ni fechas. Construir calendario con inicios/fin, disponibilidad por franja y dependencias K11; un camino de trabajo acumulado solo da una cota inferior hasta incorporar esperas y restricciones. Capacidad liberada únicamente tiene valor económico adicional si existe uso alternativo factible y sustentado.

## Caja por eventos

Para eventos ordenados por fecha y secuencia, cobros C_t y pagos P_t no negativos:

`flujo_t = C_t − P_t` · `saldo_t = saldo_(t−1) + flujo_t`

`saldo_mínimo = min(saldo_inicial, todos los saldos_t)`

Para una reserva mínima constante R documentada, la brecha adicional es `max(0, R − saldo_mínimo)`. Incluye financiación ya comprometida solo cuando su disponibilidad, fecha y condiciones estén sustentadas. La brecha es necesidad bajo ese calendario, no financiación conseguida. Si la reserva varía, usar `max_t(0, R_t−saldo_t)` incluyendo el inicio.

No compensar movimientos de un mismo día si su orden importa para financiar un pago. Si no se conoce ese orden, limitar la cota intradía o modelar la condición desfavorable con fundamento. Factura, ingreso reconocido y cobro no se copian como tres entradas de caja. Un pago de inventario precede posiblemente a su consumo; inversión, devolución, impuestos y financiación mantienen su clasificación y no duplican costes en resultado.

Con flujos o fechas materiales desconocidos, los saldos parciales se pueden mostrar con su alcance; no se concluye mínimo completo ni cobertura suficiente. La caja agregada mensual puede ocultar el déficit anterior a un cobro.

## Inventario y recurrencia

Stock utilizable por artículo, unidad, ubicación y corte:

`stock_final = stock_inicial + recepciones_utilizables + devoluciones_reintegrables − salidas − pérdidas`

No sumar devoluciones bloqueadas o pendientes de inspección a stock disponible. Un saldo negativo identifica una incompatibilidad; no se recorta a cero para ocultarla. Saldo final no negativo no demuestra disponibilidad en cada fecha: repetir movimiento por evento cuando importe secuencia. Compras, recepciones, consumo, reconocimiento del coste, pago y valoración son relaciones distintas. Documentar método de valoración pertinente; no inferirlo del saldo de unidades.

Base activa de recurrencia con movimientos compatibles:

`activos_finales = activos_iniciales + altas − bajas`

`ingreso_recurrente = exposición_facturable × precio_por_unidad_de_exposición`

Las bajas no pueden exceder la base inicial más las altas del mismo perímetro. La exposición facturable utiliza fechas y regla de prorrateo/uso contractual; no se sustituye por media de apertura y cierre sin fundamento. Si cobro y reconocimiento difieren, hacer la transformación explícita. Implantación, expansión y consumo variable se separan cuando usan otra unidad. Renovaciones no duplican altas de clientes que permanecen activos. Separar pérdida de clientes, contracción y expansión de ingreso.

Para cohorte de n nuevos clientes realmente atribuidos y coste total de adquirirlos A_k, `CAC_k = A_k/n` solo con n positivo, población y ventana compatibles y cobertura de intentos sin venta. Con n cero el cociente no existe; el coste sigue existiendo. Para una hipótesis futura con tasas sustentadas, identificarla como tal y recalcular denominador y coste juntos. No asignar probabilidad por etapa.

Valor futuro de contribución por cohorte, si hay fundamento suficiente: `V_k = suma_t(s_t × m_t / (1+d)^t) − costes_iniciales_pertinentes`, donde s es supervivencia compatible, m contribución por superviviente y periodo, d tasa por ese mismo periodo y horizonte acotado. No usar perpetuidad ni la simplificación ARPA/churn por defecto. Sin supervivencia, costes o horizonte defendibles, el valor futuro permanece no calculable. El libro no calcula CAC ni valor futuro automáticamente: recibe sus componentes con cobertura desde N09/N10 y conserva estas reglas.

## Comparación algebraica

Entre dos configuraciones de una misma unidad, `ΔΠ(q)=q(m_B−m_A)−(F_B−F_A)`. Si `m_B≠m_A`, el punto de cruce es `(F_B−F_A)/(m_B−m_A)`; confirmar signo, dominio, capacidad y dirección de preferencia. Si contribuciones iguales, la diferencia depende de fijos; si ambos términos coinciden, el resultado modelado coincide sin demostrar equivalencia de calidad o riesgo.

Inversión o caja inicial adicional no se resta otra vez si ya está reconocida dentro del resultado comparado. Para recuperación de un desembolso adicional usar los flujos incrementales fechados y el primer momento en que su acumulado cubre ese desembolso, sin asumir ahorro constante. Recuperación no es valor actual ni criterio universal de inversión.


<a id="fuente-8"></a>

## Fuente: producto/metodo/oferta_entrega_y_economia/v0.1/05_variantes_de_oferta_y_operacion.md

SHA256: db09e4cbbe510cab6165dd86c712949a3ac9ec387e4120860b667a0488da0dd2

# Variantes de oferta y operación

Versión 0.1 · Reglas combinables de N08/N11/N12

La futura prestación selecciona variantes por su unidad y recorrido; A/B describe origen de la iniciativa, no su modelo económico. Estas reglas desarrollan el alcance metodológico y precisan qué puede calcular el libro. Cuando una relación específica cambie el cálculo, debe materializarse en la fuente editable antes de concluir sobre ella. No basta marcar una casilla de aplicabilidad.

| Variante | Oferta y precio K08 | Cumplimiento K11 | Economía K12 y resolución |
|---|---|---|---|
| Servicio o proyecto | Alcance y finalización, entregas, límites de cambios, hitos y derechos; comparar precio por proyecto, tiempo u otra unidad pertinente | Preparación, trabajo por rol, revisiones, insumos del cliente, dependencias, aceptación, soporte y cierre | Costes y horas por rol sin doble imputación salarial; precio fijo no implica esfuerzo fijo. Libro: unidad de proyecto y cargas descompuestas. Agenda, hitos y trabajo por lote se documentan fuera de su agregado |
| Producto físico | Referencia/configuración, unidad comercial y embalaje, cantidades, disponibilidad y precio de canal pertinente | Compra/fabricación, lote mínimo, plazos, stock utilizable, expedición, transporte, conformidad, devolución, garantía y reposición | Separar unidades compradas/producidas/entregadas/vendidas, coste de consumo y pago. Libro: stock por corte, costes unitarios y caja por eventos. Añadir secuencia por artículo/ubicación y valoración explícita cuando sean materiales |
| Licencia o acceso recurrente | Unidad de derecho/uso, periodo, límites, altas, renovación, revisión de precio y cancelación | Activación, acceso, soporte, medición del consumo, incidencias, cierre y exportación/devolución pertinente | Implantación separada; base activa, exposición facturable, cohortes, contracción/expansión y caja. Libro: movimiento de base y exposición introducida con fundamento; no estima abandono ni valor futuro |
| Consumo medido | Contador, evento medible, tramos, mínimos, máximos y ajustes | Medición, conciliación, disponibilidad, disputa de uso, comunicación y facturación | Cantidad por tarifa/tramo y capacidad ligada al consumo; factura/ingreso/caja con sus reglas. Tramos se descomponen en entradas y fórmulas explícitas; el núcleo lineal no decide el tramo |
| Distribución o intermediación | Separar cliente contractual, canal, usuario y pagador; precio de transferencia, recomendado final si existe, comisiones/descuentos y obligaciones de cada parte | Incorporación del intermediario, pedido, entrega/stock, servicio al usuario, evidencia de venta final si es necesaria, devoluciones y liquidación | Distinguir compra del canal y venta final, base de comisión, quién soporta inventario/crédito y costes de habilitar el canal. Libro: ingreso neto propio y coste una vez; el volumen final no se suma como segunda venta propia |
| Autoservicio | Oferta comprensible, unidad, total y condiciones disponibles en el momento de compra | Selección, pago/fracaso, confirmación, entrega/activación, ayuda, cancelación/devolución y conciliación | Tasas de cobro y fallos, soporte y reembolsos, tiempos de liquidación, capacidad de atención y suministro. Libro: coste e ingreso neto y eventos; no infiere conversión por disponer de página/pago |
| Combinación de ofertas | Compatibilidad y dependencia de unidades, mínimos, paquetes y límites de sustitución | Recursos compartidos, preparaciones conjuntas, precedencias y concurrencia | Vector de cantidades y restricciones; solo agregar unidades con conversión explícita. Libro: mezcla de unidades y carga por recurso. Escalones/lotes requieren descomposición y revisión del rango |

## Cómo decidir la adaptación

1. Identificar la relación que no representa el modelo lineal: reconocimiento diferido, devolución, lote, restricción temporal, precio por tramo, interdependencia de productos u otra condición material.
2. Describir entradas, unidad, fuente y evento; redactar la fórmula o regla correspondiente con dominio y desconocidos. Relacionarla con las fórmulas generales y los campos K08/K11 que la producen.
3. Incorporar el cálculo en una sección/hoja editable de K12, con resultado propio y enlace a su consumidor. Conservar el dato original y la transformación. No pegar un resultado opaco ni duplicar el mismo ingreso/coste al integrarlo.
4. Revisar simbólicamente unidades, cobertura, dependencias, casos de dominio y reconocimiento/caja.
5. Limitar la conclusión si la adaptación material falta. Explicar qué puede decidirse con lo disponible y qué requiere completar antes del compromiso.

No se presupone un sistema contable completo, planificación industrial, asesoría fiscal o un optimizador de producción dentro de Go2Rev. La metodología debe representar las relaciones que decidan su iniciativa acotada y derivar a la competencia pertinente aquello que exceda el servicio. Esa frontera no permite omitir un coste o impedimento material y mantener una recomendación integral.


<a id="fuente-9"></a>

## Fuente: producto/metodo/oferta_entrega_y_economia/v0.1/06_comparacion_y_umbrales.md

SHA256: 949e8527adfa5c3523047d766212e4b9e681b2291bc09cee03f088f1da129e24

# Comparación, incertidumbre y umbrales

Versión 0.1 · Razonamiento de N08/N11/N12 para N06

## Construir una comparación útil

Comenzar por una pregunta que pueda modificar la decisión: unidad/alcance, coste de servir, precio, preparación reutilizable, recurso que ejecuta, suministro, canal, cobro o calendario. Utilizar información interna y contraste externo en ambas direcciones. Una alternativa externa puede revelar una configuración no contemplada; su aparente eficiencia necesita mecanismo y condiciones propias antes de recomendarla.

1. **Fijar referencia y compromiso.** Definir combinación, versión, alternativa de no invertir/mantener cuando sea pertinente, misma moneda, horizonte y significado de resultados. No tratar todo coste histórico como evitable ni capacidad disponible como demanda.
2. **Explicar la alternativa.** Identificar trabajo que cambia, quién puede hacerlo, calidad que debe conservarse, coste inicial y repetido, acceso, tiempo, obligaciones y caja. Si cambia la unidad, documentar comparación por trabajo/resultado pertinente; no forzar igual número de unidades heterogéneas.
3. **Aislar y conectar.** Examinar qué provoca la premisa y luego sus efectos conjuntos. Si se modifica precio, conservar posible efecto sobre respuesta y esfuerzo comercial como hipótesis o desconocido. Si se reduce respuesta, recalcular coste por adquisición incluyendo todos los intentos. Si se automatiza o externaliza trabajo, incluir preparación, control, fallos, soporte y derechos pertinentes.
4. **Seleccionar desfavorable defendible.** Vincular la variación con una causa, fuente o intervalo razonado. No imponer porcentajes, pesos probabilísticos ni una cuota de escenarios. Mantener dependencias: menor calidad puede elevar retrabajo, devoluciones y plazo; un lote más barato puede exigir caja y almacenamiento antes de vender.
5. **Mostrar diferencias y restricciones.** Comparar contribución, resultado pertinente, recurso limitante, tiempos y caja. Usar equilibrio o cruce únicamente en su dominio. La preferencia puede ser parcial: una opción mejora coste y empeora liquidez; explicitar decisión y condición, sin ocultarla en una puntuación total.
6. **Encontrar umbral.** Expresar la variable que invertiría la recomendación, la fórmula/regla y el intervalo en que vale. Un umbral numérico requiere parámetros; si faltan, conservar relación simbólica, consecuencia y evidencia necesaria. Un umbral de disponibilidad o derecho puede ser una condición verificable sin cifra.
7. **Recomendar.** Proponer mantener, adaptar, completar información, limitar, aplazar o descartar dentro de K01/K06. Separar recomendación del consultor y DEC. La evidencia necesaria se entrega a investigación o N14 según requiera lectura o actuación futura.

## Evidencia y suficiencia

| Afirmación que se desea sostener | Evidencia pertinente que hay que obtener en una prestación | Límite de otras fuentes |
|---|---|---|
| Menor esfuerzo con calidad equivalente | Trabajo descompuesto, condiciones y observación apropiada de ejecución/calidad | Una tarifa publicada o promesa de herramienta no acredita ahorro propio |
| Precio asumible para el comprador | Respuesta comercial pertinente, unidad y condiciones compatibles | Presupuesto declarado, comparación de precios o opinión no acreditan transacción |
| Menor coste de suministro | Oferta/condición vigente, cantidad, calidad, plazo, acceso y coste completo | Catálogo o referencia de otro ámbito no acredita condición contratada |
| Capacidad disponible | Recursos, competencia, calendario y compromisos efectivos | Organigrama, nombre de proveedor o cálculo agregado no acreditan reserva |
| Caja suficiente | Importe/evento/fecha y condiciones de financiación realmente disponibles | Rentabilidad, facturación o autorización de buscar crédito no son liquidez |

Registrar AF derivada con premisas, relación, explicación contraria y uso permitido. Si un desconocido puede invertir el orden y no cabe acotar su efecto, no hay recomendación económica concluyente entre esas opciones. Se puede recomendar la siguiente obtención de evidencia o una salida limitada. No convertir ausencia de conclusión en obligación de construir.

## Representación y conservación

La [plantilla de comparación](#fuente-6) conserva entradas, relaciones y resultados por versión, cuando se use en una prestación. El libro calcula una combinación por versión; no contiene escenarios rellenados ni una comparación simultánea automática. Cada alternativa necesita su propia fuente de parámetros y cálculo conservada en la prestación; los resultados comparados deben ser localizables y vigentes. Cambiar una premisa invalida la comparación dependiente hasta actualizarla.

 No se ejecutan comparaciones empresariales ni pruebas


<a id="fuente-10"></a>

## Fuente: producto/metodo/oferta_entrega_y_economia/v0.1/08_guia_del_modelo.md

SHA256: 21fa32a4a01baf59d648f0cc01ee081db38356b4a31ca59d2b3913e8f8bc62c9

# Guía del modelo económico editable

Versión 0.1 · Uso futuro del libro vacío (archivo adicional: producto/metodo/oferta_entrega_y_economia/v0.1/modelo/Go2Rev_modelo_economico_v0.1.xlsx)

## Contrato de uso

El libro es una representación de cálculo de K12 para **una combinación y revisión**, con un periodo económico y calendarios explícitos. Se acompaña de la [plantilla de modelo y conclusión](#fuente-5). El contrato contiene naturaleza de entradas, unidades, procedencia, inclusiones, límites, hipótesis y decisión; el libro no reemplaza ese razonamiento.

Las celdas amarillas de entrada permanecen vacías en el producto. Los números se incorporarán únicamente a una copia de prestación, con AF/FUE y revisión. Una referencia por fila debe desglosar qué AF sustenta cada entrada material; no basta una fuente genérica para toda la fila. El asistente prepara esos enlaces y cálculos. La cobertura Completa significa que se han representado todas las partidas o recursos pertinentes para el uso delimitado, no que sus valores sean observados ni que el negocio sea viable. Debe explicarse en K12.

Una celda de entrada desconocida se mantiene vacía en el libro y se identifica como desconocida/HUE en K12. Las fórmulas devuelven No calculable o conservan vacía una fila no utilizada; no sustituyen la ausencia por cero. Un cero conocido se introduce como número con fundamento. Los textos No calculable, Revisar entradas y Calculable expresan condiciones del cálculo, no evidencia ni autorización. Las fórmulas no pueden detectar por sí solas una partida omitida del alcance.

El libro no contiene macros, conexiones, datos externos ni una integración obligatoria. Se dirige a un motor compatible con XLSX y funciones escalares comunes. Se ha revisado el documento y recalculado el formato vacío con el motor documental; **no se ha verificado su comportamiento con parámetros en Excel u otro motor de prestación**. Esa comprobación se realizará en el medio efectivo de la prestación. Una exportación correcta y una fórmula visible no la sustituyen.

## Qué calcula y cómo se conecta

| Hoja | Entradas y significado | Resultados y dominio |
|---|---|---|
| Economia | E5/E6 combinación y periodo; J5/J6 moneda/escala/base; J7 contrato; E7 cobertura. Filas 26–37: ID/unidad, cantidad reconocida, ingreso neto unitario, variables de entrega y comerciales, cobertura y AF. Filas 44–51: fijos pertinentes desglosados | Ingresos y contribución por unidad y periodo, fijos y resultado del perímetro, margen sobre ingreso positivo. No es un estado contable completo. Las filas de coste fijo no vuelven a incluir las cantidades ya asignadas a variables |
| Umbrales | D5 unidad/rango/revisión, parámetros D8:D16 y AF de cada uno en E. Cantidad objetivo, coste no proporcional, tasa proporcional, fijos, resultado objetivo, precio neto/lista e indivisibilidad | Precio requerido, contribución al precio considerado, equilibrio y descuento máximo. Una unidad homogénea y rango estable. Bloque independiente: los parámetros deben referir la misma configuración; no se supone que sean la suma de las ofertas de Economia |
| Capacidad | Recursos C14:F21/K14:M21: disponibilidad total, otros compromisos y carga propia fija; unidad, AF y cobertura. Tareas C27:D58/F27:G58/I27:J58: recurso, oferta, conversión y consumo. E6 cobertura del conjunto | Recupera cantidad por ID de Economia y multiplica por conversión y consumo de recurso. Suma tareas por recurso, añade carga fija, obtiene holgura y factor radial. Una incompatibilidad conocida se conserva aunque falten otros recursos; holguras parciales no acreditan factibilidad total |
| Caja | E5/E6 horizonte, E7 saldo inicial, I5 reserva, I6 cobertura, I7 fundamentos/moneda. Eventos contiguos en filas 16–47: ID, fecha, secuencia, cobro/pago, AF, condición y clasificación | Flujo y saldo por evento; mínimo incluido el saldo inicial, saldo final y brecha adicional de financiación. No deriva cobros de ingreso ni obtiene financiación automáticamente |
| Existencias | E5/I5 cortes. Filas 11–26: artículo/ubicación, unidad, saldo inicial, recepciones/devoluciones utilizables, salidas, pérdidas y AF/cobertura | Movimiento de unidades y saldo final por artículo/unidad/ubicación. Saldo negativo visible. No calcula valoración ni demuestra disponibilidad en una fecha intermedia |
| Recurrencia | E5/J5 periodo. Filas 11–26: cohorte/oferta, unidad de exposición, base inicial/altas/bajas, exposición reconocida, precio, variable unitario y AF/cobertura | Base final, ingreso y contribución de exposición. La exposición procede de fechas/condiciones y su transformación a reconocimiento, no del promedio automático de clientes |

No sumar stocks ni clientes/cohortes que se solapen. En Recurrencia, la base se expresa en entidades completas cuando esa sea la unidad; la exposición puede ser fraccionaria si la regla contractual lo admite. Declarar unidad y condición en AF. En Existencias, identificar ubicación dentro de la clave para no mezclar stock inaccesible.

## Secuencia de preparación durante una prestación

1. Conservar el libro vacío del producto. Crear la fuente de K12 de la prestación y registrar su revisión, combinación y ubicación. Resolver antes el contrato de unidades, periodo, moneda y reconocimiento.
2. Descomponer costes y recursos con K11 y las plantillas; incorporar el contraste de investigación y Diagnostic. Recibir K09/K10 con toda la cohorte comercial, aun cuando haya intentos sin venta. Si falta su cobertura, conservar la contribución o resultado que dependa de ellos como parcial/no calculable.
3. Introducir en Economia cantidades y tarifas netas con transformaciones explícitas. Si no hay fijos pertinentes, representar una partida documentada de importe cero. La cobertura no se marca completa por llenar todas las filas.
4. Cuando corresponda, construir el movimiento de Existencias o Recurrencia. Para integrar recurrencia, enlazar exposición reconocida con cantidad de Economia y precio con ingreso unitario; descomponer su variable en entrega/comercial sin deducir de nuevo los totales. No sumar el ingreso de ambas hojas. Separar implantación o consumo si utilizan otra unidad. Los enlaces son explícitos en la copia de prestación, conservando AF/celdas y dominio; no hay importación automática de una fila indeterminada.
5. En Capacidad, cada tarea usa un ID de oferta de Economia y recurso definido. La conversión expresa unidades de trabajo por unidad reconocida; el consumo, unidades de recurso por unidad de trabajo. Ambos requieren fuente y dominio. Si la carga no guarda relación lineal con cantidad reconocida, descomponer la parte fija y los lotes/escalones o construir la relación adicional antes de utilizar su capacidad. Una producción anticipada con reconocimiento cero no se modela mediante una conversión infinita.
6. Incluir cada recurso indispensable con carga comercial, entrega, soporte y condiciones de calendario pertinentes. Una cobertura completa sin tareas variables representa carga variable cero conocida para ese recurso; debe justificarse. El factor de escala conserva mezcla, conversiones y carga fija, y deja de servir ante lotes/escalones o nueva preparación. Cabe en el periodo modelado no significa cita disponible, fecha prometible ni demanda comprobada.
7. En Caja, usar filas contiguas ordenadas por fecha y secuencia creciente dentro de fecha. Registrar cero conocido en el lado sin movimiento; un campo vacío significa importe desconocido. Incluir todas las obligaciones pertinentes, su moneda homogénea y clasificación. Un evento incompleto impide afirmar saldos posteriores completos. La financiación no disponible se expresa como brecha, no como cobro.
8. Usar Umbrales solo para una unidad homogénea con costes dentro de rango; referenciar las fuentes de sus parámetros, preferentemente por enlace cuando correspondan a celdas existentes. La tasa proporcional no puede contarse otra vez dentro del coste independiente. Un descuento máximo negativo señala precio de lista insuficiente.
9. Registrar resultados parciales, incompatibilidades y conclusión en K12; comparar configuraciones según la [instrucción de comparación](#fuente-9). Cada fuente calculada conserva parámetros y revisión; el libro no presenta comparaciones simultáneas ni capturas como si se actualizaran solas. Un cambio obliga a actualizar las fuentes y la comparación dependiente.

## Límites y extensión

Las áreas reservadas contienen doce ofertas, ocho partidas fijas, ocho recursos, treinta y dos tareas, treinta y dos eventos de caja y dieciséis filas por relación auxiliar. Son límites de esta disposición del archivo, **no cuotas de la metodología ni máximos del servicio**. Una fila fuera de esos rangos no entra en los cálculos actuales.

Para ampliar en una prestación: insertar filas dentro del bloque, extender fórmulas y validaciones y actualizar todos los rangos acotados de sumas, conteos, búsquedas y referencias entre hojas. En ofertas, revisar también las búsquedas de Capacidad; en tareas/recursos, la agregación cruzada; en caja, continuidad del saldo y resumen final. Revisar primera/última fila, identificación única, dominio y enlace a resultados. La extensión no es automática. La comprobación de comportamiento se sitúa en la etapa de la prestación autorizada, dentro de la preparación autorizada de ese medio.

El núcleo no optimiza mezcla, planifica fechas, elige tramos ni valora inventario. Tampoco infiere adquisición, abandono, aceptación de precio o valor futuro. Las [fórmulas generales](#fuente-7) y [variantes](#fuente-8) establecen cómo resolver las relaciones adicionales pertinentes. Si falta una adaptación material, la conclusión dependiente permanece limitada.

Las fuentes generales son esta especificación y la definición editable del libro (archivo adicional: producto/metodo/oferta_entrega_y_economia/v0.1/modelo/definicion_modelo.mjs), ambas dentro del producto. El generador documental utiliza esas fuentes actuales. No requiere originales históricos ni el archivo de referencia visual para regenerar el libro.
