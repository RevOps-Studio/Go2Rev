# N12 · Economía y capacidad

Versión 0.1 · Productor de K12

Empezar con la [primera pasada de N12](../../operacion_conversacional/v0.2/10_primera_pasada.md#n12) y aplicar [núcleo y suficiencia](../../operacion_conversacional/v0.2/12_nucleo_y_suficiencia.md). El procedimiento y contrato siguientes gobiernan el análisis completo.

## Pregunta y perímetro

Determinar qué puede sostenerse bajo una combinación explícita, qué impide comprometerla y qué cambio merece consideración. Separar economía de la iniciativa, economía de prestar Go2Rev y desarrollo del producto.

Recibir K08 unidad/condiciones, K09 actividad y coste de toda la cohorte, K10 esfuerzo comercial y tiempos, K11 trabajo/cobro/pago y K02 recursos. E no exige K06 final. Si falta acceso o compra, calcular las partes sustentadas y declarar adquisición/venta incompletas; no emitir una conclusión integral de sostenibilidad con esa ausencia.

## Construcción del modelo

1. **Fijar contrato.** Definir combinación y revisiones, decisión, periodo/horizonte, moneda/escala, unidades y conversiones, alcance económico, tratamiento de impuestos, reconocimiento y exclusiones. Diferenciar unidad vendida, producida, entregada, reconocida y cobrada. Seleccionar las [variantes](05_variantes_de_oferta_y_operacion.md) pertinentes y su resolución.
2. **Descomponer entradas.** Cada cantidad tiene campo, valor o desconocido, unidad, población/periodo, AF/FUE, naturaleza, transformación y uso admitido. Etiquetar rango solo con fundamento de límites. Un dato público sobre otro contexto puede informar una hipótesis; no adquiere naturaleza observada propia. Una conclusión del contraste puede exigir una nueva partida o restricción omitida por el cliente.
3. **Reconciliar partidas.** Usar el [registro de partidas y recursos](plantillas/03_partidas_y_recursos.md). Para cada partida identificar objeto de coste, impulsor, cantidad/tarifa, moneda, reconocimiento, pago, comportamiento en rango, cobertura e inclusión. Clasificar variable, fijo relevante, lote, escalón, inversión o ajuste sin imponer un comportamiento fuera de su rango. Identificar qué ya está incluido en otra partida y qué queda excluido de la suma.
4. **Distinguir decisiones económicas.** El coste incremental ayuda a decidir una unidad adicional con recursos ociosos; el resultado con fijos pertinentes ayuda a valorar sostenibilidad. Separar costes hundidos de compromisos futuros evitables y de asignaciones. Una asignación contable no es pago nuevo; un salario fijo sigue siendo coste del periodo aunque no incremente con una venta. Coste de oportunidad se muestra separado, con alternativa factible y fundamento, sin sumarlo también como desembolso.
5. **Calcular por relaciones.** Aplicar [fórmulas y dominio](04_formulas_y_dominio.md), mostrando cantidad, tarifa, subtotales y resultado. Incluir preparación y todos los intentos de adquisición/venta con su cohorte; mantener idéntico coste total si se redistribuye por unidades. Evitar sumar CAC y las partidas que ya lo forman. Un CAC no observado no aparece como cifra histórica.
6. **Resolver capacidad.** Descomponer carga por recurso, lote, preparación y unidad, restar compromisos ajenos al ámbito y respetar calendarios. Comprobar escasez conocida antes de buscar una capacidad agregada. Con varias ofertas, usar vector de demanda/carga y restricciones compartidas. Una mezcla favorable en contribución puede incumplir el recurso escaso. Si falta un recurso indispensable, conservar el límite parcial; no sustituirlo por disponibilidad infinita.
7. **Resolver caja.** Construir eventos ordenados con importes y condiciones desde K11. Separar ingresos/costes reconocidos de cobros/pagos, inversión y financiación. Conciliar saldos por evento incluyendo el inicial; revisar mínimos antes de agregarlos por periodo. No financiar automáticamente un déficit con una línea no disponible. Un calendario o importe desconocido limita la necesidad de financiación que pueda afirmarse.
8. **Analizar cambio.** Usar [comparación y umbrales](06_comparacion_y_umbrales.md). Cuestionar una premisa material y explicar alternativa, efecto conjunto y condición contraria. Mantener efectos sobre calidad, compra, coste, recurso y caja. No completar cifras para ordenar opciones si las ausencias pueden invertir ese orden.
9. **Devolver recomendación.** K12 identifica resultados calculables, parciales y no calculables; contribución, resultado pertinente, capacidad, caja, equilibrio/cruce cuando existan, restricciones, umbral, evidencia necesaria e implicaciones para N06/N08–N11. Un cálculo coherente no demuestra demanda, aceptación de precio ni ejecución.

## Suficiencia y gobierno

La cobertura se juzga para el compromiso. E puede servir para descartar una combinación por imposibilidad conocida, priorizar una pregunta o recomendar evidencia adicional con una economía parcial. Para O deben existir condiciones actuales suficientes de coste, recursos y caja; la comprobación de preparación corresponde a N14–N16 en su futura ejecución. La admisión documental de K12 no es autorización de gasto.

El consultor responde del modelo y razonamiento. Finanzas, operación y propietarios aportan datos exclusivos y confirman su significado; el patrocinador decide riesgo e inversión. Si un parámetro queda pendiente, identificar HUE, fuente alternativa, responsable y uso detenido. No exigir reconstruir toda la economía de una organización para una decisión acotada.

El [modelo editable](modelo/Go2Rev_modelo_economico_v0.1.xlsx) implementa un núcleo explícito y extensiones de stock/recurrencia; su [guía](08_guia_del_modelo.md) delimita capacidades. Las fórmulas generales incluyen relaciones que pueden precisar adaptación documentada de la fuente de cálculo. No se denomina calculadora universal ni se presenta el resultado parcial como resultado contable completo.

## Revisión ante cambios

Una revisión de precio, unidad, mezcla, respuesta, esfuerzo, proveedor, capacidad, calidad, plazo o condición de pago obliga a localizar entradas dependientes, revisar sus transformaciones, recalcular lo afectado en la prestación y devolver consecuencias antes del siguiente compromiso. Registrar CAM con versiones y conservar DEC previas. No repetir nodos sin impacto. Un cambio de cantidad afecta también a lotes/escalones y, si altera respuesta o calendario, a adquisición y caja.
