# Guía del modelo económico editable

Libro y guía v0.2 · Uso futuro del [libro vacío](modelo/Go2Rev_modelo_economico_v0.2.xlsx)

## Contrato de uso

El libro es una representación de cálculo de K12 para **una combinación y revisión**, con un periodo económico y calendarios explícitos. Se acompaña de la [plantilla de modelo y conclusión](plantillas/05_modelo_y_conclusion.md). El contrato contiene naturaleza de entradas, unidades, procedencia, inclusiones, límites, hipótesis y decisión; el libro no reemplaza ese razonamiento.

Las celdas amarillas de entrada permanecen vacías en el producto. Los números se incorporarán únicamente a una copia de prestación, con AF/FUE y revisión. Una referencia por fila debe desglosar qué AF sustenta cada entrada material; no basta una fuente genérica para toda la fila. El asistente prepara esos enlaces y cálculos. La cobertura Completa significa que se han representado todas las partidas o recursos pertinentes para el uso delimitado, no que sus valores sean observados ni que el negocio sea viable. Debe explicarse en K12.

Una celda de entrada desconocida se mantiene vacía en el libro y se identifica como desconocida/HUE en K12. Las fórmulas devuelven No calculable o conservan vacía una fila no utilizada; no sustituyen la ausencia por cero. Un cero conocido se introduce como número con fundamento. Los textos No calculable, Revisar entradas y Calculable expresan condiciones del cálculo, no evidencia ni autorización. Las fórmulas no pueden detectar por sí solas una partida omitida del alcance.

El libro no contiene macros, conexiones, datos externos ni una integración obligatoria. Se dirige a un motor compatible con XLSX y funciones escalares comunes. Su generador escribe fórmulas y solicita recálculo al abrir; no calcula resultados. Abrir y recalcular la copia de trabajo en el motor efectivo de la prestación antes de interpretar resultados. Una exportación correcta y una fórmula visible no sustituyen esa comprobación.

## Orientación dentro del libro

La hoja **Guia** explica preparación, significado de las entradas, cobertura, relaciones, comparación y conservación. Se añade a las seis hojas de cálculo existentes y no alimenta sus fórmulas. Los ceros numéricos se muestran como 0,00 según la configuración regional; los vacíos siguen representando ausencia de dato. Los avisos de estado tienen formato condicional y las explicaciones aparecen en celdas de fondo azul claro.

| Dónde leer | Qué ayuda a resolver |
|---|---|
| Economia G11:G15 | Identidad, periodo, moneda, contrato y condición pendiente de cada resumen |
| Economia O26:O37 y J44:J51 | Identificación, entradas, dominio y cobertura de ofertas y fijos |
| Umbrales G20:G23 | Parámetros y dominio de cada relación |
| Capacidad G8/G10, O14:O21 y L27:L58 | Factibilidad, factor de escala y condiciones de recursos y tareas |
| Caja G9:G11 y N16:N47 | Condiciones de saldos/brecha y continuidad de cada evento |
| Existencias N11:N26 y Recurrencia Q11:Q26 | Identidad, cortes, unidades, movimientos y cobertura de cada fila |

La explicación muestra la primera condición pendiente; resolverla puede revelar otra. Las fórmulas de negocio y sus estados siguen gobernando el resultado. Una referencia AF escrita no acredita por sí sola evidencia suficiente, y una explicación favorable no detecta partidas omitidas ni concede autorización. La cobertura completa del perímetro E7 es necesaria para el resultado agregado; debe justificarse, incluso cuando existan resultados parciales calculables.

Caja, Existencias y Recurrencia muestran en E4 la combinación de Economia. Mantienen su propio horizonte, cortes o periodo: conciliar su correspondencia en K12, sin exigir fechas idénticas. Caja incorpora en M16:M47 una lista de clasificación general; si se elige Otra documentada, explicar su regla. La clasificación no asigna automáticamente tratamiento contable, moneda ni obligaciones.

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
9. Registrar resultados parciales, incompatibilidades y conclusión en K12; comparar configuraciones según la [instrucción de comparación](06_comparacion_y_umbrales.md). Cada fuente calculada conserva parámetros y revisión; el libro no presenta comparaciones simultáneas ni capturas como si se actualizaran solas. Un cambio obliga a actualizar las fuentes y la comparación dependiente.

## Límites y extensión

Las áreas reservadas contienen doce ofertas, ocho partidas fijas, ocho recursos, treinta y dos tareas, treinta y dos eventos de caja y dieciséis filas por relación auxiliar. Son límites de esta disposición del archivo, **no cuotas de la metodología ni máximos del servicio**. Una fila fuera de esos rangos no entra en los cálculos actuales.

Para ampliar en una prestación: insertar filas dentro del bloque, extender fórmulas y validaciones y actualizar todos los rangos acotados de sumas, conteos, búsquedas y referencias entre hojas. En ofertas, revisar también las búsquedas de Capacidad; en tareas/recursos, la agregación cruzada; en caja, continuidad del saldo y resumen final. Revisar primera/última fila, identificación única, dominio y enlace a resultados. La extensión no es automática. La comprobación de comportamiento se sitúa en la etapa de la prestación autorizada, dentro de la preparación autorizada de ese medio.

El núcleo no optimiza mezcla, planifica fechas, elige tramos ni valora inventario. Tampoco infiere adquisición, abandono, aceptación de precio o valor futuro. Las [fórmulas generales](04_formulas_y_dominio.md) y [variantes](05_variantes_de_oferta_y_operacion.md) establecen cómo resolver las relaciones adicionales pertinentes. Si falta una adaptación material, la conclusión dependiente permanece limitada.

Las fuentes generales son esta especificación y la [definición editable del libro](modelo/definicion_modelo.json), ambas dentro del producto. La [herramienta de generación](../../../../herramientas/modelo_economico/LEEME.md) utiliza esa definición actual con Python y openpyxl. No requiere originales históricos ni un libro anterior para regenerar el original vacío.
