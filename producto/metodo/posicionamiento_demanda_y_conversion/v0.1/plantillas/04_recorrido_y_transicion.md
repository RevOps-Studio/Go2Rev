# Plantilla de recorrido y transición de compra

Vista generada · Corregir la [definición de campos](../../../esquema/v0.1/plantillas.json), no esta vista. ★ = campo de la plantilla principal: aplicar condición y momento; las piezas auxiliares pueden ser indispensables. Cabecera: identidad, versión, ámbito y K01, autor y fecha, ubicación, estado documental, receptor y uso. Registrar una vez por artefacto; los bloques remiten a ella. FUE, AF y otros registros con identidad propia conservan sus metadatos. La aceptación se localiza en DEC.


Versión 0.1 · K10 · Campos empresariales vacíos

Usar con [conversión y compra](../03_conversion_y_compra.md) y [variantes y traspasos](../05_variantes_y_traspasos.md). Definir solo etapas y ramas que representen decisiones o controles necesarios. Repetir el bloque de transición dentro de K10; no fija etapas, probabilidades ni número de contactos.

## Recorrido y objeto

<a id="k10-t04-b01"></a>

<!-- bloque: K10.T04.B01 -->
| Campo | Regla | Valor |
|---|---|---|
| ★ Referencia | K10/revisión, ubicación, autor, fecha y estado documental |  |
| ★ Encargo y uso | K01/revisión, ámbito, E/O y combinación K08/K09/K11/K12 |  |
| ★ Modo de compra | Directo, intermediado, autoservicio o combinación; relaciones que deben distinguirse |  |
| ★ Objeto de seguimiento | Cuenta, ocasión, pedido u otro objeto pertinente; identidad, relaciones y deduplicación |  |
| ★ Entrada | Señal/origen K09, significado, evidencia y frontera de tarea/coste N09–N10 |  |
| ★ Decisiones del comprador | K04: situación, riesgos, roles, autoridad y criterios; procesos paralelos o de terceros |  |
| ★ Definición de ocasión admitida | Qué justifica trabajar una decisión de compra, evidencia necesaria y siguiente decisión |  |
| ★ Oferta y compromisos | K08/revisión, condiciones, autoridad y cambios permitidos |  |
| ★ Aceptación, pedido e inicio | Eventos distintos y condiciones K11; no equiparar propuesta emitida, compra, entrega e ingreso |  |
| ★ Fundamento y carencias | AF/FUE internas/externas, comparabilidad, razonamiento, HUE/CON y efecto en el recorrido |  |

## Transición o rama — bloque repetible

<a id="k10-t04-b02"></a>

<!-- bloque: K10.T04.B02 -->
| Campo | Regla | Valor |
|---|---|---|
| ★ Localización y propósito | Sección estable, origen/destino y decisión o control que justifica la transición |  |
| ★ Condición de entrada | Información y estado necesarios; productor/campo/revisión |  |
| ★ Ajuste e intención | Condiciones de posibilidad de servir separadas de señales de voluntad/avance |  |
| ★ Evidencia de condición | Evento, material o confirmación, fuente, vigencia y responsable competente |  |
| ★ Resultado de evaluación | Cumplida, incumplida, desconocida o no aplica justificado; desconocido limita el paso dependiente |  |
| ★ Trabajo necesario | Acción, insumos y resultado; esfuerzo también si no se avanza |  |
| ★ Material requerido | Función, contenido, oferta/AF, destinatario, medio y criterio para N15 |  |
| ★ Riesgo u objeción | Cuestión de compra, explicación, evidencia o cambio de capacidad; no sustituir respuesta por presión |  |
| ★ Responsable y autoridad | Quién actúa, quién puede comprometer y respaldo ante indisponibilidad |  |
| ★ Asignación y respuesta | Criterio de asignación, acuse, origen del reloj, calendario/zona y plazo sustentado por capacidad |  |
| ★ Receptor y salida | Objeto/evidencia transmitidos, confirmación de recepción y condición de aceptación |  |
| ★ Rama sin avance | Devolución, información pendiente, pausa, rechazo o cierre; motivo y acción pertinente |  |
| ★ Seguimiento | Motivo útil, permiso, criterio temporal, condición de cese y reapertura; sin cadencia universal |  |
| ★ Actividad y carga | Cantidad de ejecuciones, recurso, consumo por ejecución/preparación y referencia de partida |  |
| ★ Observabilidad | Evento, unidad, identidad, fecha, fuente y decisión para N13; seguimiento incompleto visible |  |
| ★ Dependencia de preparación | Medio/CAP, comprobación requerida y efecto si no está disponible |  |

## Cierre, variantes y revisión

<a id="k10-t04-b03"></a>

<!-- bloque: K10.T04.B03 -->
| Campo | Regla | Valor |
|---|---|---|
| ★ Cierre comercial | Qué acredita aceptación, rechazo u otra salida y autoridad del comprador; preservar versión aceptada |  |
| ★ Traspaso a entrega | Referencia al bloque K11 de entrega/traspaso; condiciones pendientes, receptor y aceptación |  |
| ★ Particularidad de variante | Intermediario/cliente final separados o secuencia pedido/pago/confirmación; condición pertinente |  |
| ★ Excepción y conciliación | Quién resuelve conflicto de estado, duplicidad o condición no prevista antes de otro compromiso |  |
| ★ Economía exploratoria | Campos K10 E para N06/N12; actividad/coste/tiempo, dominio y desconocidos sin exigir compra observada |  |
| ★ Recepción y cambio | Consumidor/campo/revisión, disposición; premisa que exige CAM y revisión localizada |  |

La [plantilla K11 de entrega y traspaso](../../../oferta_entrega_y_economia/v0.1/plantillas/02_entrega_y_traspaso.md) conserva el contrato de cumplimiento. La [recepción y seguimiento](06_recepcion_y_seguimiento.md) desarrolla asignación y devoluciones comerciales sin duplicar ese contrato.

## Aplicabilidad de los bloques

Antes de emitir K10, completar el núcleo de [N10 Diseñar compra y traspasos](../../../operacion_conversacional/v0.3/10_primera_pasada.md). Las reglas CONTR, EVAL, USO y de variante de esta plantilla mantienen su momento de exigibilidad. Un bloque condicional se completa cuando afecte al resultado; documentar la condición que lo hace aplicable o su exclusión. Una ausencia material queda localizada y limita el uso dependiente. La cabecera común se registra una vez por artefacto.
