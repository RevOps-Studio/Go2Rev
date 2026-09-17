# Plantilla de actividad, coste y cohorte

Vista generada · Corregir la [definición de campos](../../../esquema/v0.1/plantillas.json), no esta vista. ★ = campo de la plantilla principal: aplicar condición y momento; las piezas auxiliares pueden ser indispensables. Cabecera: identidad, método y versión del paquete, versión, ámbito y K01, autor y fecha, ubicación, estado documental, receptor y uso. Registrar una vez por artefacto; los bloques remiten a ella. Las fuentes de trabajo identifican Go2Rev y la versión del paquete. FUE, AF y otros registros con identidad propia conservan sus metadatos. La aceptación se localiza en DEC.


Versión 0.1 · Campos K09/K10 para K12/K13 · Campos empresariales vacíos

Usar con [costes, cohortes y capacidad](../04_costes_cohortes_y_capacidad.md). Este bloque vincula trabajo comercial y población a las [partidas y recursos de K12](../../../oferta_entrega_y_economia/v0.1/plantillas/03_partidas_y_recursos.md). Referenciar la misma partida fuente: el reparto para analizar una ruta no crea un coste adicional.

## Perímetro de población y medida

<a id="k09-t05-b01"></a>

<!-- bloque: K09.T05.B01 -->
| Campo | Regla | Valor |
|---|---|---|
| Referencia | K09/K10, sección/revisión, autor, fecha y estado |  |
| Encargo y uso | K01/revisión, E/O y combinación; moneda, impuestos, periodo y unidad económica |  |
| Cohorte | Regla de inclusión, origen de entrada y corte; identificar sin crear otro maestro |  |
| Unidad e identidad | Persona, cuenta, ocasión, pedido o unidad vendida; enlace entre objetos y deduplicación |  |
| Observación | Ventana, fecha del evento, tiempo de seguimiento y tratamiento de entradas inmaduras |  |
| Población al corte | Definiciones mutuamente excluyentes de avance, cierre sin avance, pendiente y resultado desconocido |  |
| Resultado medido | Evento, condición, fuente y unidad; adquisición nueva distinta de renovación o segunda compra |  |
| Numerador y denominador | Definiciones, cobertura y compatibilidad; rutas que saltan pasos se separan |  |
| Naturaleza y fundamento | AF/FUE por cantidad/tasa/tiempo; observado, inferido, hipotético o desconocido |  |
| Transferibilidad | Origen/destino, comparabilidad, sesgo, límites y razonamiento para cada dato externo o histórico |  |
| Solapamiento y atribución | Ventana, regla, identidad y parte sin atribuir; atribuir no demuestra causalidad |  |

## Actividad y recurso — bloque repetible

<a id="k09-t05-b02"></a>

<!-- bloque: K09.T05.B02 -->
| Campo | Regla | Valor |
|---|---|---|
| Actividad y frontera | Preparación o tarea repetida; K09/K10 productor y consumidor, evitando doble registro |  |
| Impulsor | Qué genera trabajo: preparación, intentos, exposiciones, respuestas, revisiones u otro evento definido |  |
| Cantidad de ejecuciones | Todas las ejecuciones pertinentes, incluso sin resultado; fuente/hipótesis y periodo |  |
| Recurso | Unidad no intercambiable, competencia y CAP; utilizar únicamente recursos y disponibilidad asignados al encargo; referencia común con K11/K12 |  |
| Restricción y respuesta | Cuello de botella, capacidad por habilitar o límite de emisión/compromiso |  |

## Partida y representación económica — bloque repetible

<a id="k09-t05-b03"></a>

<!-- bloque: K09.T05.B03 -->
| Campo | Regla | Valor |
|---|---|---|
| Partida fuente | Identificador/localización/revisión de K12; conservar una sola contabilización |  |
| Componentes y cobertura | Trabajo, terceros, medios, datos, incentivos u otros costes pertinentes; ausencias materiales visibles |  |
| Cantidad y tarifa | Referencia de fuente, unidad, moneda/impuestos y regla de cálculo de la partida |  |
| Perímetro de coste | Incremental, reconocido o valoración de recurso ya remunerado; relación con salario/coste común |  |
| Compartición | Rutas y tareas consumidoras, regla de reparto y conciliación con total de origen |  |
| Reconocimiento y pago | Periodo de reconocimiento separado de fecha/condición de pago; enlace a evento de caja |  |
| Comportamiento | Fijo en rango, variable por unidad o función de actividad/tramo; dominio que lo justifica |  |
| Representación K12 | Total del periodo, variable por unidad sustentado o relación adicional; no introducir CAC automáticamente como variable |  |
| Conciliación | Cómo el total de partidas se conserva sin sumar de nuevo coste por resultado o atribuciones |  |
| Relación coste/resultado | C hasta resultado definido dividido por su cantidad positiva compatible; cero o desconocido no autorizan cociente |  |

## Conclusión y entrega

<a id="k09-t05-b04"></a>

<!-- bloque: K09.T05.B04 -->
| Campo | Regla | Valor |
|---|---|---|
| Resultado utilizable | Calculable, parcial o no calculable; límite y decisión que permite |  |
| Dependencia sensible | Premisa, efectos conjuntos y umbral sustentado o relación simbólica; no inventar extremos |  |
| Carencia material | HUE/CON, productor y qué compromiso queda limitado |  |
| Consumidores y revisión | N06/N12/N13 pertinentes, campo/revisión, recepción y condición CAM |  |

La fórmula vacía expresa una relación general.

## Aplicabilidad de los bloques

Antes de emitir K09, completar el núcleo de [N09 Elegir rutas de demanda](../../../operacion_conversacional/v0.4/10_primera_pasada.md). Las reglas CONTR, EVAL, USO y de variante de esta plantilla mantienen su momento de exigibilidad. Un bloque condicional se completa cuando afecte al resultado; documentar la condición que lo hace aplicable o su exclusión. Una ausencia material queda localizada y limita el uso dependiente. La cabecera común se registra una vez por artefacto.
