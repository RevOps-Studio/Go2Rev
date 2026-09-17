# Plantilla · Eventos de cobro y pago

Vista generada · Corregir la [definición de campos](../../../esquema/v0.1/plantillas.json), no esta vista. ★ = campo de la plantilla principal: aplicar condición y momento; las piezas auxiliares pueden ser indispensables. Cabecera: identidad, método y versión del paquete, versión, ámbito y K01, autor y fecha, ubicación, estado documental, receptor y uso. Registrar una vez por artefacto; los bloques remiten a ella. Las fuentes de trabajo identifican Go2Rev y la versión del paquete. FUE, AF y otros registros con identidad propia conservan sus metadatos. La aceptación se localiza en DEC.


Versión 0.1 · [Entrega y cobro](../02_entrega_y_cobro.md) · [Fórmulas](../04_formulas_y_dominio.md)

Repetir por obligación/evento. Mantener separados evento previsto, condición acordada y movimiento observado.

<a id="k12-t04-b01"></a>

<!-- bloque: K12.T04.B01 -->
| Campo | Regla | Valor |
|---|---|---|
| Cabecera | K11/K12, revisión, combinación, horizonte, moneda y escala |  |
| Saldo inicial | Importe, fecha, procedencia y disponibilidad efectiva |  |
| Reserva mínima | Regla/importe, horizonte y autoridad; no porcentaje universal |  |
| Evento | ID, obligación, contraparte y vínculo con oferta/tarea |  |
| Naturaleza | Cobro, pago, devolución, inversión, tributo o financiación pertinente |  |
| Importe y base | Valor o desconocido, moneda/impuestos y fórmula de la obligación |  |
| Condición | Qué habilita el evento y quién tiene autoridad |  |
| Fecha y orden | Fecha/regla, evento de origen, calendario y secuencia intradía |  |
| Fundamento | AF/FUE, naturaleza de afirmación, revisión y límites |  |
| Reconocimiento económico | Relación con ingreso/coste, inversión u otra clasificación |  |
| Financiación | Disponibilidad/condiciones acreditadas, vencimiento y pagos asociados |  |
| Incidencia | Retraso, disputa, impago/devolución y efecto sobre saldo/plazo |  |
| Movimiento observado | Comprobante/importe/fecha/aplicación solo cuando exista |  |
| Cobertura del calendario | Obligaciones incluidas, ausentes y conclusión que limitan |  |
| Resultado y brecha | Saldos, mínimo incluyendo inicio y financiación adicional necesaria |  |
| Consumo y revisión | Campos/revisiones consumidores, admisión/límite y CAM |  |

## Aplicabilidad de los bloques

Antes de emitir K12, completar el núcleo de [N12 Analizar economía y capacidad](../../../operacion_conversacional/v0.4/10_primera_pasada.md). Las reglas CONTR, EVAL, USO y de variante de esta plantilla mantienen su momento de exigibilidad. Un bloque condicional se completa cuando afecte al resultado; documentar la condición que lo hace aplicable o su exclusión. Una ausencia material queda localizada y limita el uso dependiente. La cabecera común se registra una vez por artefacto.
