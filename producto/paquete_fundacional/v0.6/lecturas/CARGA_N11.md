# Go2Rev · N11 · Lectura inicial

Conjunto 0.6 · Compilación derivada, no fuente editable. El contenido expresamente incluido sustituye la apertura del original metodológico de esa versión; una sección no sustituye el resto del archivo. Las fuentes del encargo y del mercado requieren lectura efectiva.

## N11 · Diseñar entrega y cobro

**Entrada:** Oferta, aceptación, recursos y restricciones.

**Salida:** K11; consumo por N06, N08, N10, N12, N13, N14, N15.

**Cierre:** Distinguir aceptación, entrega, reconocimiento y caja; completar variantes solo cuando cambien una obligación o relación material.

**Destino:** 01 Entregables/Design. Mantener fuente, vista e índice.

<a id="fuente-68c1371b7d07"></a>

## Fuente: 02_entrega_y_cobro.md

Procedencia: `producto/metodo/oferta_entrega_y_economia/v0.1/02_entrega_y_cobro.md` · SHA256 `9aefea1ab740c76d69575c3c16917849ae152801cbc6ad373c1d2e1ad8b4ca14` · Incluye: sección Procedimiento de primera pasada íntegra.

## Procedimiento de primera pasada

Trabajar con la entrada común y aplicar [INV-01–21](../../../metodo/operacion_conversacional/v0.4/13_invariantes.md). Los identificadores de campos y bloques se localizan en la plantilla generada; la referencia posterior conserva el razonamiento y sus casos de aplicabilidad.

1. Recuperar oferta, conformidad comprometida y recursos. Descomponer la unidad entregada en trabajo, insumos, responsables y dependencias materiales.
2. Diseñar aceptación, entrega, incidencias y recepción por el siguiente responsable. Abrir las variantes que cambien obligación, inventario, recurrencia, intermediación o servicio.
3. Precisar hitos de facturación, cobro y pago y su relación con el cumplimiento. Transmitir a K12 consumo de recursos, coste y eventos de caja con sus unidades y fundamento.
4. Entregar K11 con capacidad, condiciones y límites; resolver con K08/K10 cualquier promesa o transición incompatible antes de habilitar su uso.

**Bloques de salida:** K11.T02.B01. Su condición y momento gobiernan la exigibilidad; las piezas auxiliares se abren según la tarea.

<a id="fuente-ecbc667b76d6"></a>

## Fuente: 02_entrega_y_traspaso.md

Procedencia: `producto/metodo/oferta_entrega_y_economia/v0.1/plantillas/02_entrega_y_traspaso.md` · SHA256 `57f142550f10296e5f790dee9c6ff939f637ebdb7b76a6e0d103ff2e35751da9` · Incluye: archivo íntegro.

# Plantilla · K11 Cumplimiento y traspaso

Vista generada · Corregir la [definición de campos](../../../metodo/esquema/v0.1/plantillas.json), no esta vista. ★ = campo de la plantilla principal: aplicar condición y momento; las piezas auxiliares pueden ser indispensables. Cabecera: identidad, método y versión del paquete, versión, ámbito y K01, autor y fecha, ubicación, estado documental, receptor y uso. Registrar una vez por artefacto; los bloques remiten a ella. Las fuentes de trabajo identifican Go2Rev y la versión del paquete. FUE, AF y otros registros con identidad propia conservan sus metadatos. La aceptación se localiza en DEC.


Versión 0.1 · [Instrucción](../../../metodo/oferta_entrega_y_economia/v0.1/02_entrega_y_cobro.md)

Repetir el bloque de tarea o traspaso cuando cambie decisión, ejecutor o evidencia. No crear etapas sin función.

<a id="k11-t02-b01"></a>

<!-- bloque: K11.T02.B01 -->
| Campo | Regla | Valor |
|---|---|---|
| ★ Cabecera | K11, K01, revisión, ámbito, autor/fecha, estado y ubicación |  |
| ★ Uso y entradas | E/O, combinación, K02/K03/K04/K08/K10/K12 y versiones |  |
| ★ Unidad y compromiso | Entrega K08 y criterio de conformidad |  |
| ★ Tarea | ID local estable, acción y salida observable |  |
| ★ Entrada y condición | Insumos, permisos, fuente y condición de inicio |  |
| ★ Precedencia y calendario | Dependencias, esfuerzo activo, espera, fecha/regla y concurrencia |  |
| ★ Naturaleza del trabajo | Preparación común, lote, repetición, control, incidencia o continuidad |  |
| ★ Recursos | Rol/medio, unidad de consumo y disponibilidad con CAP/TRA |  |
| ★ Ejecutor y autoridad | Quién realiza y quién decide excepción |  |
| ★ Receptor y evidencia | Quién recibe, qué comprueba y rastro de finalización |  |
| ★ Proveedor | Condiciones, acceso, plazo, alternativa y efecto de ausencia |  |
| ★ Partidas | Relación con coste y momento de pago, sin duplicación |  |
| ★ Incidencia | Disparador, contención, corrección, coste/plazo y autoridad |  |
| ★ Inicio y aceptación | Diferencia entre acuerdo, inicio, entrega y conformidad |  |
| ★ Traspaso | ID, emisor/receptor, oferta/revisión, cantidad/unidad y condiciones |  |
| ★ Contenido transferido | Alcance/exclusiones, evidencias, insumos y pendientes |  |
| ★ Siguiente acción | Responsable, condición y medio |  |
| ★ Recepción | Evidencia y fecha solo cuando ocurra |  |
| ★ Facturación y cobro | Evento/regla, obligación y referencia al bloque de caja |  |
| ★ Continuidad y cierre | Soporte, garantía, renovación, cancelación y límite pertinentes |  |
| ★ Suficiencia | Recursos o condiciones desconocidos y compromiso afectado |  |
| ★ Consumo y cambio | Receptor/campo/revisión/uso, admisión/límite y CAM |  |

## Aplicabilidad de los bloques

Antes de emitir K11, completar el núcleo de [N11 Diseñar entrega y cobro](../../../metodo/operacion_conversacional/v0.4/10_primera_pasada.md). Las reglas CONTR, EVAL, USO y de variante de esta plantilla mantienen su momento de exigibilidad. Un bloque condicional se completa cuando afecte al resultado; documentar la condición que lo hace aplicable o su exclusión. Una ausencia material queda localizada y limita el uso dependiente. La cabecera común se registra una vez por artefacto.


## Ampliar según la tarea

Abrir las secciones indicadas antes del uso dependiente; conservar el resto localizable.

| Condición | Lectura y sección |
|---|---|
| Al desarrollar una decisión, variante o excepción que los pasos breves no resuelven; antes de usar una fórmula o procedimiento especializado. | [02_entrega_y_cobro](CARGA_N11_extension.md#fuente-68c1371b7d07): Referencia sustantiva pertinente a la pregunta |
| Antes de emitir el resultado a su consumidor; al cambiar entradas, ámbito o uso E/O. | [07_contratos_y_revision](CARGA_N11_extension.md#fuente-892fa843c581): Contrato K11 y relación de consumo afectada |
| Antes de calcular o interpretar una relación económica; abrir su fórmula, unidad y dominio. | [04_formulas_y_dominio](CARGA_N11_extension.md#fuente-32ef546a1f9b): Relación o variante activada |
| Cuando venta, entrega, intermediación o recurrencia cambien una relación material. | [05_variantes_de_oferta_y_operacion](CARGA_N11_extension.md#fuente-e24114bf6491): Relación o variante activada |
| Antes de comparar opciones, sensibilidad o umbrales. | [06_comparacion_y_umbrales](CARGA_N11_extension.md#fuente-7e01f29474a7): Relación o variante activada |
| Antes de utilizar o revisar el libro económico. | [08_guia_del_modelo](CARGA_N11_extension.md#fuente-5daea7cf4c58): Relación o variante activada |
