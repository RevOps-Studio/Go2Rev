# Actividad, cohortes, costes y capacidad comercial

Versión 0.1 · Salidas económicas de N09/N10 hacia N12

Estas relaciones generales permiten construir la parte comercial de K12. Se aplican junto a las [fórmulas de oferta, entrega y economía](../../oferta_entrega_y_economia/v0.1/04_formulas_y_dominio.md) y su [contrato](../../oferta_entrega_y_economia/v0.1/07_contratos_y_revision.md).

## Unidades, identidad y ventana

Antes de contar, definir objeto, evento, ámbito y ventana. Una persona no es necesariamente una cuenta; una cuenta puede tener varias unidades compradoras y ocasiones de compra; un acuerdo puede incluir varios pedidos o unidades de entrega. Documentar conversiones, relación con K08/K11 y fuente de cada identidad. No sumar contactos de una misma compra como compras diferentes ni inferir cuentas únicas a partir de impresiones o sesiones.

Una **cohorte** agrupa objetos con la misma regla de entrada, ventana, ámbito y criterio de seguimiento. K09/K10 conservan una sección localizable por revisión, sin añadir un tipo de registro maestro. Definir pertenencia, fecha de entrada/corte, duración observada y criterio de madurez. Distinguir población elegible, acceso disponible, intentos, objetos únicos expuestos, respuestas, ocasiones admitidas, acuerdos y nuevos clientes.

La misma persona puede generar varios eventos y varias personas compartir una ocasión. Deduplicar por el objeto que mide la magnitud, preservando eventos y reglas de enlace. Si no puede resolverse la identidad, declarar el alcance observado y la incertidumbre; no asumir que cada fila es un comprador diferente. Un nuevo episodio requiere una nueva decisión/ocasión según regla explícita, no simplemente otro intento.

Para medir un evento dentro de una duración w, cada objeto del denominador debe haber tenido el mismo tiempo pertinente para producirlo, o debe declararse la diferencia. Elegir cohorte madura o un tratamiento documentado del seguimiento incompleto. No excluir selectivamente las decisiones todavía abiertas y comparar los restantes como si representaran la cohorte completa. No ocurrir dentro de w no equivale a no ocurrir nunca.

## Conteos y tasas

| Relación | Fórmula o regla | Dominio y límite |
|---|---|---|
| Respuesta en una ventana | Objetos únicos con respuesta definida / objetos únicos expuestos o contactados bajo la regla | Denominador positivo y misma unidad/cohorte/ventana. Mensajes enviados no equivalen a exposición acreditada; nombrar la tasa según lo que se conoce |
| Avance entre conjuntos anidados | `r_j = n_j / n_(j−1)` | n_j es subconjunto del conjunto anterior, sin repetir objetos; ambos del mismo seguimiento. `0 ≤ r_j ≤ 1`. Si hay rutas que saltan etapas, separar ramas |
| Conversión acumulada | `n_final / n_inicial` | Cohorte y criterio de evento compatibles, denominador positivo. El producto de tasas equivale a este cociente solo si todos los conjuntos son anidados y compatibles |
| Conciliación de una población al corte | Total incluido = avanzó + cerró sin avanzar + pendiente + resultado desconocido | Disposiciones mutuamente excluyentes para ese paso y corte. No sumar estados históricos repetidos ni confundir desconocido con pendiente conocido |
| Resultado condicionado de una cadena | `n_final = n_inicial × producto(r_j)` | Relación de cantidades bajo tasas condicionales sustentadas y población compatible. Una proyección conserva naturaleza hipotética; no convierte tasas externas en resultado observado |
| Tiempo hasta un evento | Fecha/hora de evento menos origen, según calendario definido | Observaciones abiertas tienen seguimiento incompleto. La media de quienes cerraron no describe por sí sola el ciclo de todos los entrantes |

La actividad repetida se cuenta como actividad para esfuerzo/coste, aunque se deduplique la población para una tasa. Cuando hay retorno, no contar la reentrada como nueva adquisición por defecto. Una compra puede tener varias exposiciones; las contribuciones atribuidas a canales no son automáticamente aditivas ni demuestran causalidad.

Si se necesita atribución, acordar objeto, ventana, regla y tratamiento del solapamiento. Con atribución fraccionaria, los pesos por resultado no exceden la unidad y su parte sin atribuir permanece visible; una regla de reparto no acredita efecto incremental. Sin identidad/cobertura suficiente, mostrar rutas asistidas con su límite, sin sumar como nuevas ventas independientes. La relación con intermediario y la venta final se mantienen separadas.

## Trabajo por actividad y recurso

Para una cohorte k, actividad a y recurso r:

`H_(k,r) = S_(k,r) + suma_a(n_(k,a) × h_(a,r))`

S es preparación y carga no ligada a cada repetición; n es número de ejecuciones de actividad, incluidos intentos fallidos, ausencia de respuesta y devoluciones; h es consumo del recurso por ejecución. Todos usan el mismo periodo y unidad de recurso. Cada n, h y S requiere fuente/hipótesis o desconocido. Una actividad que no exige un recurso puede usar cero conocido justificado; un esfuerzo ausente no es cero.

Descomponer preparación, obtención de insumos, producción, emisión, atención, cualificación, propuesta, revisión, coordinación, traspaso y cierre pertinentes. Identificar cuándo un trabajo sirve a varias rutas y registrar su importe/carga una sola vez. El coste de una herramienta no elimina la supervisión o tratamiento de excepciones que realmente requiera.

Para disponibilidad A_r y otros compromisos B_r del mismo recurso/periodo, comprobar:

`suma_k(H_(k,r)) ≤ A_r − B_r`

La capacidad compartida incluye otras cargas de N11 y las tareas comerciales; la agregación se realiza en N12, sin sumar presupuestos de recursos no intercambiables. Si n depende de una tasa desconocida, mostrar la relación y el límite parcial. Un volumen de salida objetivo no determina por sí solo la actividad necesaria para conseguirlo.

Un compromiso de respuesta requiere además distribución temporal de entradas, carga por franja, competencias y respaldo. El promedio de horas disponibles en un mes no acredita atender un pico ni un plazo por objeto. Definir condición de admisión, cola, prioridad y escalado sin prometer respuesta inmediata universal. Si la carga prevista excede capacidad, recomendar reducir emisión, cambiar trabajo, habilitar recurso o limitar el compromiso; no aumentar oportunidades teóricas para justificar el coste.

## Coste de la cohorte y de su resultado

Construir C_k con partidas identificadas: trabajo valorado según el perímetro pertinente, terceros, medios, datos, incentivos y parte de preparación/recursos compartidos que corresponda. Cada partida conserva cantidad, tarifa, unidad, periodo, fuente, regla de reparto y vínculo con el [registro de costes de oferta, entrega y economía](../../oferta_entrega_y_economia/v0.1/plantillas/03_partidas_y_recursos.md). La suma tiene cobertura completa únicamente si representa todas las partidas materiales para ese uso.

Separar desembolso incremental, coste reconocido y valoración de recursos ya remunerados. Multiplicar horas por tarifa permite valorar esfuerzo si la tarifa es pertinente, pero no autoriza añadir ese valor al salario ya incluido en F. Una asignación a cohorte sirve para analizar rendimiento; su incorporación a resultado se reconcilia con la partida de origen. La preparación reutilizable conserva inversión, periodo de reconocimiento y regla de asignación; no se distribuye entre un volumen futuro inventado.

Para un resultado definido d y cantidad n_(k,d) positiva:

`coste_por_resultado_(k,d) = C_(k,d) / n_(k,d)`

El numerador debe cubrir el trabajo necesario hasta ese resultado y la población del denominador, incluidos intentos sin resultado. Nombrar coste por respuesta, ocasión admitida, acuerdo o cliente nuevo según el evento. Solo **CAC** si n cuenta clientes nuevos bajo una definición y ventana compatibles. Una renovación, una segunda compra o una cuenta ya cliente no se convierte en nueva adquisición. Si n es cero, el coste existe y el cociente no está definido; si n es desconocido, no se reemplaza por una hipótesis sin fundamento.

No comparar costes por resultado con definiciones distintas ni trasladar un coste por contacto a un coste por venta. Un intervalo requiere fundamento de extremos y dependencias; combinar el mejor coste con la mejor conversión de contextos diferentes no crea una hipótesis defendible.

## Entrega de partidas a K12

| Tratamiento económico | Condición | Cómo evitar doble imputación |
|---|---|---|
| Coste del periodo o de una cohorte fijada | Su importe y reconocimiento están definidos para el alcance; distinguir comportamiento frente a actividad y frente a cantidad vendida | Entregar total y partidas; no añadir también su coste por resultado como variable. Solo entra en F constante si realmente permanece fijo en el rango modelado |
| Variable por unidad vendida/entregada | Existe relación sustentada con esa unidad, población y rango | Entregar regla y unidad; no volver a restar las partidas ya incluidas. Conciliar asignación × cantidades con el total pertinente |
| Dependiente de intentos, respuesta o tramos | El coste cambia con actividad y no puede expresarse como variable de venta constante ni fijo del rango | Entregar función/cantidad por impulsor; N12 añade la relación explícita antes de concluir. No forzarla dentro del núcleo lineal |
| Recurso/coste compartido | Varias rutas o tareas consumen el mismo recurso o partida | Conservar una partida y una carga fuente; desglosar atribución para análisis sin sumarla otra vez al total |

La [plantilla de actividad/coste](plantillas/05_actividad_coste_y_cohorte.md) entrega unidad, población, cohorte, impulsor, esfuerzo, reconocimiento y pago por partida. N12 decide su representación según el dominio, no según el nombre comercial del canal. N09 y N10 conservan la frontera de tarea y el mismo identificador de partida cuando comparten una referencia.

En el [libro de oferta, entrega y economía](../../oferta_entrega_y_economia/v0.1/08_guia_del_modelo.md), la columna de variable comercial por unidad no es un lugar para introducir CAC sin reconciliar. Las cargas que no sean proporcionales a cantidad reconocida se descomponen o requieren una relación adicional; los cobros/pagos se llevan a eventos con fecha y condición. Si falta conversión, puede calcularse una actividad comprometida y su coste con cobertura propia, manteniendo desconocido el coste por compra.

## Expectativas, sensibilidad y recomendación

Una expectativa ponderada solo se produce si su decisión la necesita y existe fundamento para la probabilidad, horizonte y magnitud condicionada. Para ocasiones distintas, el valor esperado puede expresarse como suma de probabilidad de compra dentro del horizonte por importe esperado condicionado a esa compra. Versiones alternativas de una misma propuesta no son compras independientes; resolver exclusividad y composición antes de sumar. La fecha de cierre, ingreso reconocido y caja son magnitudes distintas. Una etiqueta de etapa no fundamenta ninguna de ellas.

Para analizar una premisa, conservar mecanismo y efectos conjuntos: cambiar respuesta afecta intentos por resultado y carga comercial; cambiar precio puede alterar respuesta/alcance; cambiar canal puede añadir preparación, comisión y demora de cobro. No mantener un CAC favorable mientras se reduce el denominador sin revisar el numerador. Derivar umbrales desde K12: coste/actividad admisible, capacidad por recurso o condición de respuesta que haría viable la combinación dentro de su dominio. Sin parámetros suficientes, conservar la relación simbólica.

N06 recibe resultados calculables, parciales y no calculables, su efecto en la tesis y la pregunta decisiva. La cobertura comercial incompleta impide una recomendación integral que dependa de ella, pero no oculta una incompatibilidad conocida. El compromiso de obtener nueva evidencia se formula para N03–N05 si basta investigación o para N14 si requiere actuación; ejecutar esos protocolos es propia de la prestación autorizada.
