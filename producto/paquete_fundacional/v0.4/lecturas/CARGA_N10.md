# Go2Rev · N10 · Lectura inicial

Conjunto 0.4 · Compilación derivada, no fuente editable. El contenido expresamente incluido sustituye la apertura del original metodológico de esa versión; una sección no sustituye el resto del archivo. Las fuentes del encargo y del mercado requieren lectura efectiva.

## N10 · Diseñar compra y traspasos

**Entrada:** K04, oferta, acceso y condiciones de entrega/caja.

**Salida:** K10; consumo por N06, N11, N12, N13, N14, N15.

**Cierre:** Ajustar cadencia a ventana de compra, permiso y capacidad; antes de automatizar comprobar sus eventos, excepciones y autoridad.

**Destino:** 01 Entregables/Design. Mantener fuente, vista e índice.

<a id="fuente-9b29bf28bbeb"></a>

## Fuente: 03_conversion_y_compra.md

Procedencia: `producto/metodo/posicionamiento_demanda_y_conversion/v0.1/03_conversion_y_compra.md` · SHA256 `ae62b04ac345a4a28262e470df45c3f2f2d31db06549c4aaade5184da879b6ff` · Incluye: sección Procedimiento de primera pasada íntegra.

## Procedimiento de primera pasada

Trabajar con la entrada común y aplicar [INV-01–20](../../../metodo/operacion_conversacional/v0.3/13_invariantes.md). Los identificadores de campos y bloques se localizan en la plantilla generada; la referencia posterior conserva el razonamiento y sus casos de aplicabilidad.

1. Recuperar compra K04, oferta K08, ruta K09 y condiciones K11/K12. Representar objeto de trabajo, decisiones del comprador, estados y eventos observables.
2. Definir para cada transición el criterio discriminante, acción, responsable, información y receptor. Separar pertinencia e intención; incorporar retorno, excepción y cierre.
3. Abrir recepción/seguimiento para fijar cadencia conforme a ventana de compra, permiso y capacidad. Abrir costes y cohortes antes de valorar el recorrido.
4. Entregar K10 con evidencia de evento, traspasos, condiciones económicas y límites. Para automatizar, transmitir a N14/N15 eventos, excepciones y autoridad y fijar la comprobación pertinente.

**Bloques de salida:** K10.T04.B01, K10.T04.B02, K10.T04.B03. Su condición y momento gobiernan la exigibilidad; las piezas auxiliares se abren según la tarea.

<a id="fuente-358a812e5694"></a>

## Fuente: 04_recorrido_y_transicion.md

Procedencia: `producto/metodo/posicionamiento_demanda_y_conversion/v0.1/plantillas/04_recorrido_y_transicion.md` · SHA256 `7c4098654baf47f7a751614196d538922c9a1e0edec26d661c130d67534b1db3` · Incluye: archivo íntegro.

# Plantilla de recorrido y transición de compra

Vista generada · Corregir la [definición de campos](../../../metodo/esquema/v0.1/plantillas.json), no esta vista. ★ = campo de la plantilla principal: aplicar condición y momento; las piezas auxiliares pueden ser indispensables. Cabecera: identidad, versión, ámbito y K01, autor y fecha, ubicación, estado documental, receptor y uso. Registrar una vez por artefacto; los bloques remiten a ella. FUE, AF y otros registros con identidad propia conservan sus metadatos. La aceptación se localiza en DEC.


Versión 0.1 · K10 · Campos empresariales vacíos

Usar con [conversión y compra](../../../metodo/posicionamiento_demanda_y_conversion/v0.1/03_conversion_y_compra.md) y [variantes y traspasos](../../../metodo/posicionamiento_demanda_y_conversion/v0.1/05_variantes_y_traspasos.md). Definir solo etapas y ramas que representen decisiones o controles necesarios. Repetir el bloque de transición dentro de K10; no fija etapas, probabilidades ni número de contactos.

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

La [plantilla K11 de entrega y traspaso](../../../metodo/oferta_entrega_y_economia/v0.1/plantillas/02_entrega_y_traspaso.md) conserva el contrato de cumplimiento. La [recepción y seguimiento](../../../metodo/posicionamiento_demanda_y_conversion/v0.1/plantillas/06_recepcion_y_seguimiento.md) desarrolla asignación y devoluciones comerciales sin duplicar ese contrato.

## Aplicabilidad de los bloques

Antes de emitir K10, completar el núcleo de [N10 Diseñar compra y traspasos](../../../metodo/operacion_conversacional/v0.3/10_primera_pasada.md). Las reglas CONTR, EVAL, USO y de variante de esta plantilla mantienen su momento de exigibilidad. Un bloque condicional se completa cuando afecte al resultado; documentar la condición que lo hace aplicable o su exclusión. Una ausencia material queda localizada y limita el uso dependiente. La cabecera común se registra una vez por artefacto.


## Ampliar según la tarea

Abrir las secciones indicadas antes del uso dependiente; conservar el resto localizable.

| Condición | Lectura y sección |
|---|---|
| Al desarrollar una decisión, variante o excepción que los pasos breves no resuelven; antes de usar una fórmula o procedimiento especializado. | [03_conversion_y_compra](CARGA_N10_extension.md#fuente-9b29bf28bbeb): Referencia sustantiva pertinente a la pregunta |
| Antes de emitir el resultado a su consumidor; al cambiar entradas, ámbito o uso E/O. | [06_contratos_y_revision](CARGA_N10_extension.md#fuente-e4a708b3f956): Contrato K10 y relación de consumo afectada |
| Al definir recepción, retorno y cadencia de seguimiento. | [06_recepcion_y_seguimiento](CARGA_N10_extension.md#fuente-abdb7e967668): Bloques aplicables de la plantilla |
| Antes de estimar costes o rendimiento del mecanismo o recorrido. | [04_costes_cohortes_y_capacidad](CARGA_N10_extension.md#fuente-827a7d4c8fdf): Variante pertinente |
| Cuando cambien canal, intermediación, forma de compra o traspaso. | [05_variantes_y_traspasos](CARGA_N10_extension.md#fuente-0b3a6a4e08a4): Variante pertinente |
