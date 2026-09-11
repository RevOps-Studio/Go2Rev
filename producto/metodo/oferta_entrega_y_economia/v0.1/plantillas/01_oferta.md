# Plantilla · K08 Oferta y precio

Vista generada · Corregir la [definición de campos](../../../esquema/v0.1/plantillas.json), no esta vista. ★ = campo de la plantilla principal: aplicar condición y momento; las piezas auxiliares pueden ser indispensables. Cabecera: identidad, versión, ámbito y K01, autor y fecha, ubicación, estado documental, receptor y uso. Registrar una vez por artefacto; los bloques remiten a ella. FUE, AF y otros registros con identidad propia conservan sus metadatos. La aceptación se localiza en DEC.


Versión 0.1 · Campos sin contenido de prestación · [Instrucción](../01_oferta_y_precio.md)

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

Antes de emitir K08, completar el núcleo de [N08 Definir oferta y precio](../../../operacion_conversacional/v0.3/10_primera_pasada.md). Las reglas CONTR, EVAL, USO y de variante de esta plantilla mantienen su momento de exigibilidad. Un bloque condicional se completa cuando afecte al resultado; documentar la condición que lo hace aplicable o su exclusión. Una ausencia material queda localizada y limita el uso dependiente. La cabecera común se registra una vez por artefacto.
