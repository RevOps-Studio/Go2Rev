# Go2Rev · N08 · Lectura inicial

Conjunto 0.5 · Compilación derivada, no fuente editable. El contenido expresamente incluido sustituye la apertura del original metodológico de esa versión; una sección no sustituye el resto del archivo. Las fuentes del encargo y del mercado requieren lectura efectiva.

## N08 · Definir oferta y precio

**Entrada:** K04/K05 y costes/capacidades de K11/K12.

**Salida:** K08; consumo por N06, N09, N10, N11, N12, N15.

**Cierre:** En exploración, guardar la representación en Diagnostic y mantener la economía en su fuente única; para uso concreto comprobar autoridad y preparación pertinentes.

**Destino:** 01 Entregables/Design. Mantener fuente, vista e índice.

<a id="fuente-678f0d744491"></a>

## Fuente: 01_oferta_y_precio.md

Procedencia: `producto/metodo/oferta_entrega_y_economia/v0.1/01_oferta_y_precio.md` · SHA256 `d1bc7879a4cdb6d41721a7366fba0e1dd4149d7a4874ee6024105c321cc5d529` · Incluye: sección Procedimiento de primera pasada íntegra.

## Procedimiento de primera pasada

Trabajar con la entrada común y aplicar [INV-01–20](../../../metodo/operacion_conversacional/v0.3/13_invariantes.md). Los identificadores de campos y bloques se localizan en la plantilla generada; la referencia posterior conserva el razonamiento y sus casos de aplicabilidad.

1. Recuperar comprador, alternativas y capacidades de entrega. Definir unidad ofrecida, destinatario, contenido, exclusiones y conformidad; distinguir quién compra, usa y paga.
2. Comparar configuración, métrica de precio y mecanismo de cobro. Triangular costes, alternativas comparables y valor, abriendo variantes y fórmulas cuando cambien la unidad o condición.
3. Proponer importe, rango o regla fundada; conciliar neto, descuentos, impuestos y condiciones con entrega/caja K11 y economía K12. Mantener localizadas las cuestiones especializadas.
4. Entregar K08 por combinación y uso. En E informar Diagnostic; antes de un compromiso O comprobar autoridad, disponibilidad y cobertura pertinentes.

**Bloques de salida:** K08.T01.B01. Su condición y momento gobiernan la exigibilidad; las piezas auxiliares se abren según la tarea.

<a id="fuente-4454a5374164"></a>

## Fuente: 01_oferta.md

Procedencia: `producto/metodo/oferta_entrega_y_economia/v0.1/plantillas/01_oferta.md` · SHA256 `a8394b5554457c3c40925eba7a176e6091c0973be07ce6d9954c984e9916fa9a` · Incluye: archivo íntegro.

# Plantilla · K08 Oferta y precio

Vista generada · Corregir la [definición de campos](../../../metodo/esquema/v0.1/plantillas.json), no esta vista. ★ = campo de la plantilla principal: aplicar condición y momento; las piezas auxiliares pueden ser indispensables. Cabecera: identidad, versión, ámbito y K01, autor y fecha, ubicación, estado documental, receptor y uso. Registrar una vez por artefacto; los bloques remiten a ella. FUE, AF y otros registros con identidad propia conservan sus metadatos. La aceptación se localiza en DEC.


Versión 0.1 · Campos sin contenido de prestación · [Instrucción](../../../metodo/oferta_entrega_y_economia/v0.1/01_oferta_y_precio.md)

Repetir los bloques pertinentes por configuración o compromiso; conservar IDs/revisión y agruparlos cuando facilite lectura. En uso, desconocido y no aplica siguen el diccionario común.

<a id="k08-t01-b01"></a>

<!-- bloque: K08.T01.B01 -->
| Campo | Regla | Valor |
|---|---|---|
| ★ Cabecera | K08, K01, revisión, autor/fecha, ámbito, estado y ubicación |  |
| ★ Uso y combinación | E/O y K06/revisión/sección cuando exista; decisión solicitada |  |
| ★ Entradas | K02/K04/K05 y K06/K07/K11/K12 pertinentes, campos y versiones |  |
| ★ Recorrido | A/B; TRA/CAP y efecto en oferta |  |
| ★ Situación y alternativa | Necesidad, desencadenante, alternativa actual y fundamento |  |
| ★ Roles | Usuario, beneficiario, comprador, intermediario y pagador |  |
| ★ Unidades | Valor, venta, entrega, facturación y recurso; conversión y periodo |  |
| ★ Configuración | Contenido, módulos/dependencias, límites, opciones y razón de elección |  |
| ★ Compromiso | Entrega controlable, responsable, AF/DEC y condiciones |  |
| ★ Requisitos de entrada | Insumos, permisos y condición para iniciar |  |
| ★ Exclusiones y derechos | Frontera, uso/transferencia pertinente y condiciones |  |
| ★ Finalización | Criterio de conformidad, receptor y cierre |  |
| ★ Fundamento interno | Coste/capacidad/caja y AF; huecos |  |
| ★ Fundamento externo | Alternativa, unidad/alcance/periodo y AF/FUE leída |  |
| ★ Contraste y conclusión | Comparabilidad, mecanismo, AF derivada, implicación y refutación |  |
| ★ Compra y valor | Criterio K04 y evidencia/hipótesis de respuesta |  |
| ★ Mecanismo de precio | Base, contador/evento, regla, límites y discusión |  |
| ★ Importe o intervalo | Moneda, unidad, extremos sustentados o desconocido |  |
| ★ Precio neto | Descuentos/base/orden, comisiones, ajustes y no duplicación |  |
| ★ Condiciones económicas | Impuestos, vigencia, facturación, vencimientos y cobro |  |
| ★ Continuidad | Renovación, revisión, cancelación, devolución y soporte pertinentes |  |
| ★ Estado de propuesta | Referencia/hipótesis/condición autorizada/evidencia de respuesta, con rastro |  |
| ★ Alternativas y recomendación | Razón de preferencia, límites y condición contraria |  |
| ★ Autoridad | DEC para compromiso/excepción y alcance de autorización |  |
| ★ Consumo y revisión | Campo/revisión, receptor, uso, admisión/límite; CAM/disparador |  |

## Aplicabilidad de los bloques

Antes de emitir K08, completar el núcleo de [N08 Definir oferta y precio](../../../metodo/operacion_conversacional/v0.3/10_primera_pasada.md). Las reglas CONTR, EVAL, USO y de variante de esta plantilla mantienen su momento de exigibilidad. Un bloque condicional se completa cuando afecte al resultado; documentar la condición que lo hace aplicable o su exclusión. Una ausencia material queda localizada y limita el uso dependiente. La cabecera común se registra una vez por artefacto.


## Ampliar según la tarea

Abrir las secciones indicadas antes del uso dependiente; conservar el resto localizable.

| Condición | Lectura y sección |
|---|---|
| Al desarrollar una decisión, variante o excepción que los pasos breves no resuelven; antes de usar una fórmula o procedimiento especializado. | [01_oferta_y_precio](CARGA_N08_extension.md#fuente-678f0d744491): Referencia sustantiva pertinente a la pregunta |
| Antes de emitir el resultado a su consumidor; al cambiar entradas, ámbito o uso E/O. | [07_contratos_y_revision](CARGA_N08_extension.md#fuente-892fa843c581): Contrato K08 y relación de consumo afectada |
| Antes de calcular o interpretar una relación económica; abrir su fórmula, unidad y dominio. | [04_formulas_y_dominio](CARGA_N08_extension.md#fuente-32ef546a1f9b): Relación o variante activada |
| Cuando venta, entrega, intermediación o recurrencia cambien una relación material. | [05_variantes_de_oferta_y_operacion](CARGA_N08_extension.md#fuente-e24114bf6491): Relación o variante activada |
| Antes de comparar opciones, sensibilidad o umbrales. | [06_comparacion_y_umbrales](CARGA_N08_extension.md#fuente-7e01f29474a7): Relación o variante activada |
| Antes de utilizar o revisar el libro económico. | [08_guia_del_modelo](CARGA_N08_extension.md#fuente-5daea7cf4c58): Relación o variante activada |
