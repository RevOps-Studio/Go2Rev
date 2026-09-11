# Fórmulas generales y dominio

Versión 0.1 · Especificación editable de N12

Las relaciones siguientes son reglas del producto, sin parámetros de una empresa. En una prestación, toda entrada numérica requiere valor finito, unidad, periodo/población, procedencia y cobertura. Un desconocido se propaga a las magnitudes dependientes; cero se admite únicamente como valor sustentado. Un cociente exige denominador válido. No se ocultan errores sustituyéndolos por cero.

## Notación y alcance

`i` identifica una unidad de oferta; `r`, un recurso no intercambiable; `t`, un periodo o evento ordenado; `k`, una cohorte de adquisición. `q_i` es cantidad reconocida en el periodo; `p_i`, ingreso neto por esa unidad; `v_i`, coste variable pertinente por unidad; `F`, costes fijos pertinentes del mismo periodo; `M`, moneda homogénea. Las conversiones entre vendido, fabricado, entregado, facturable y reconocido deben estar documentadas. Si no coinciden, construir sus movimientos por evento antes de usar `q_i`.

Ingresos, costes y caja tienen bases distintas. El resultado aquí es **resultado económico del perímetro modelado**, con inclusiones declaradas; no se etiqueta automáticamente EBITDA, beneficio contable o renta fiscal. Impuestos recuperables/no recuperables, reconocimiento, depreciación, intereses y otras partidas materiales se resuelven con criterio pertinente, no por un porcentaje universal. Una conversión de moneda identifica tasa, fecha, fuente y sensibilidad; no se suman monedas antes de convertir.

## Precio y contribución

| Relación | Fórmula general | Dominio y límite |
|---|---|---|
| Descuentos sucesivos sobre precio de lista | `p = P × producto(1 − d_j) − D` | `P ≥ 0`, cada `0 ≤ d_j ≤ 1`, `D ≥ 0`; orden y base de D explícitos, `p ≥ 0`. No aplica si el contrato usa otra base |
| Comisión o tarifa porcentual | `c = a × b` | `a` tasa y `b` base contractual compatible; no asumir que b es siempre p |
| Coste por impulsor | `C = cantidad × tarifa` | Mismas unidades de impulsor y periodo; no omitir uno por estar vacío |
| Contribución unitaria | `m_i = p_i − v_i` | `v_i` incluye variables de entrega y comerciales pertinentes sin duplicación; m puede ser negativa |
| Margen de contribución | `m_i / p_i` | Solo `p_i > 0`; margen no equivale a recargo sobre coste |
| Ingreso del periodo | `R = suma(q_i × p_i)` | Cantidades no negativas y compatibles con reconocimiento. Abonos se reconcilian por separado o dentro de p, una vez |
| Contribución del periodo | `MC = suma(q_i × m_i)` | Misma cobertura de costes por cada unidad |
| Resultado del perímetro | `Π = MC − F` | Mezcla/rango en que v y F son válidos; incorporar costes por lote/escalón si no están incluidos |

Separar contribución antes de adquisición de contribución después de variables comerciales cuando ayude a decidir. Si el gasto de adquisición de una cohorte se incluye como coste del periodo, no volver a deducir su asignación unitaria. Si se distribuye entre unidades, verificar que cantidades por asignación reproducen el total pertinente y el mismo horizonte. Los intentos sin venta permanecen en el coste.

Una oferta de ingreso cero puede analizarse con sus costes y contribución negativa; no tiene margen sobre ingreso ni un precio aceptado positivo. Una devolución puede reducir ingresos y generar coste adicional; no tratar el mero retorno físico como recuperación de todo el ingreso/coste.

## Equilibrio y umbrales de precio

Con una unidad homogénea, `m > 0` y `F ≥ 0`, el volumen continuo de equilibrio es `q* = F / m`. Si la unidad es indivisible, el mínimo entero que cubre F es `techo(F/m)`. Confirmar que el volumen cae en el rango de costes y capacidad y que el calendario permite realizarlo. Equilibrio económico no demuestra demanda ni financiación.

Si `m = 0`, con F positivo no hay volumen que lo cubra; con F cero el resultado es cero para cualquier volumen admisible. Si `m < 0`, aumentar volumen deteriora el resultado; con F no negativo no existe equilibrio positivo que mejore la situación. El punto q=0 con F=0 no justifica actividad sostenible. No dividir por un margen nulo ni devolver un número negativo como objetivo de ventas.

Si una unidad tiene coste independiente del precio `c` y coste proporcional `a × p`, entonces `m(p) = p(1−a)−c`. Para cubrir F con cantidad q y resultado objetivo T:

`p_requerido = (c + (F + T)/q) / (1−a)`

Dominio: `q > 0`, `0 ≤ a < 1`, `c,F ≥ 0`, T definido en M por periodo. El libro limita T a no negativo; una decisión de pérdida admisible se modela explícitamente fuera de ese bloque. Si costes, respuesta, alcance o capacidad cambian con p o q, esta expresión solo vale localmente y hay que recomponer las relaciones. No constituye disposición a pagar ni tarifa aprobada.

Para un precio de lista P positivo, un único descuento sobre esa base y sin otros cambios, `d_máximo = 1 − p_requerido/P`. Si resulta negativo, el precio de lista no cubre el umbral; no se convierte en descuento cero que aparenta suficiencia. El umbral no autoriza descontar. Condiciones comerciales, evidencia y autoridad siguen siendo necesarias.

## Mezcla, lotes y escalones

Con cantidades diferentes por unidad, conservar el vector `q = (q_i)` y calcular `Π(q) = suma(q_i m_i) − F(q) − suma(C_lote(q))`, evitando restar partidas ya incluidas en v o F. No dividir suma de unidades heterogéneas para inventar un margen unitario común.

Si la mezcla es estable y todas las cantidades usan una unidad agregable, pesos `w_i ≥ 0`, `suma(w_i)=1`, dan `m_mezcla = suma(w_i m_i)`. Solo si m_mezcla es positivo puede usarse `F/m_mezcla`. Cambiar mezcla, intervalos de descuento o recurso escaso exige recalcular. Para paquetes de proporción fija puede definirse una unidad compuesta con cantidades `a_i` documentadas y contribución `suma(a_i m_i)`; no se asume que cualquier mezcla sea ese paquete.

Para lotes indivisibles de tamaño b positivo, `n_lotes = techo(q/b)` y `C_lote = n_lotes × coste_por_lote`, bajo el alcance de ese lote. Con q cero, n_lotes es cero, salvo preparación comprometida independiente que se cuenta aparte. Identificar si el excedente se almacena, se pierde o sirve después; no reconocer automáticamente ingreso por lo producido.

Con costes escalonados, definir cada intervalo de cantidad, coste y capacidad, sin solapamientos ni huecos inadvertidos. Resolver equilibrio dentro de cada tramo y comprobar fronteras y pertenencia del resultado al tramo; el salto de coste puede eliminar un equilibrio aparente. No sustituir ese trabajo por F constante. En el libro básico, introducir una configuración de tramo explícita y devolver límites a K12; la fórmula simple no automatiza la elección entre tramos.

## Capacidad por recurso y calendario

Para recurso r, disponibilidad total `A_r`, carga de otros compromisos `B_r`, carga propia fija `S_r` (preparación y otro trabajo no ligado a q, desglosados), y consumo por unidad `h_ri`:

`L_r(q) = S_r + suma(q_i × h_ri) + carga_por_lotes_r(q)`

`holgura_r = A_r − B_r − L_r(q)`

Todos usan la misma unidad de recurso y periodo; A,B,S,h no negativos. Si existe carga comercial, soporte o incidencias pertinente, incluirla una vez como preparación, carga por unidad, por lote o bloque identificado. Una fuente que solo cubre entrega deja la capacidad integral incompleta.

Una combinación incumple una restricción conocida si alguna holgura es negativa; aunque falten otros recursos, esa incompatibilidad permanece. Holguras no negativas con un recurso indispensable desconocido no demuestran factibilidad. Para una sola unidad con consumo h_r positivo y preparaciones fijas, la cota es `min_r((A_r−B_r−S_r)/h_r)` entre recursos completos, truncando al entero inferior si la unidad es indivisible. Si A−B−S es negativo, ni la preparación cabe. Un h_r cero conocido no limita por repetición, pero su preparación sí puede limitar; nunca dividir por cero.

Para conservar una mezcla representada q y preparación fija, sea `V_r = suma(q_i h_ri)`. Si `V_r > 0`, el factor radial máximo es `(A_r−B_r−S_r)/V_r`, sujeto a las demás restricciones. Este factor escala proporcionalmente las cantidades; no es número de clientes, demanda ni óptimo de mezcla. Con cargas por lote o escalón hay que resolver de nuevo para cada escala; no se extrapola el factor. Si todos los V son cero, el factor no tiene significado de capacidad comercial ilimitada.

La carga por periodo no resuelve precedencias, reservas, simultaneidad ni fechas. Construir calendario con inicios/fin, disponibilidad por franja y dependencias K11; un camino de trabajo acumulado solo da una cota inferior hasta incorporar esperas y restricciones. Capacidad liberada únicamente tiene valor económico adicional si existe uso alternativo factible y sustentado.

## Caja por eventos

Para eventos ordenados por fecha y secuencia, cobros C_t y pagos P_t no negativos:

`flujo_t = C_t − P_t` · `saldo_t = saldo_(t−1) + flujo_t`

`saldo_mínimo = min(saldo_inicial, todos los saldos_t)`

Para una reserva mínima constante R documentada, la brecha adicional es `max(0, R − saldo_mínimo)`. Incluye financiación ya comprometida solo cuando su disponibilidad, fecha y condiciones estén sustentadas. La brecha es necesidad bajo ese calendario, no financiación conseguida. Si la reserva varía, usar `max_t(0, R_t−saldo_t)` incluyendo el inicio.

No compensar movimientos de un mismo día si su orden importa para financiar un pago. Si no se conoce ese orden, limitar la cota intradía o modelar la condición desfavorable con fundamento. Factura, ingreso reconocido y cobro no se copian como tres entradas de caja. Un pago de inventario precede posiblemente a su consumo; inversión, devolución, impuestos y financiación mantienen su clasificación y no duplican costes en resultado.

Con flujos o fechas materiales desconocidos, los saldos parciales se pueden mostrar con su alcance; no se concluye mínimo completo ni cobertura suficiente. La caja agregada mensual puede ocultar el déficit anterior a un cobro.

## Inventario y recurrencia

Stock utilizable por artículo, unidad, ubicación y corte:

`stock_final = stock_inicial + recepciones_utilizables + devoluciones_reintegrables − salidas − pérdidas`

No sumar devoluciones bloqueadas o pendientes de inspección a stock disponible. Un saldo negativo identifica una incompatibilidad; no se recorta a cero para ocultarla. Saldo final no negativo no demuestra disponibilidad en cada fecha: repetir movimiento por evento cuando importe secuencia. Compras, recepciones, consumo, reconocimiento del coste, pago y valoración son relaciones distintas. Documentar método de valoración pertinente; no inferirlo del saldo de unidades.

Base activa de recurrencia con movimientos compatibles:

`activos_finales = activos_iniciales + altas − bajas`

`ingreso_recurrente = exposición_facturable × precio_por_unidad_de_exposición`

Las bajas no pueden exceder la base inicial más las altas del mismo perímetro. La exposición facturable utiliza fechas y regla de prorrateo/uso contractual; no se sustituye por media de apertura y cierre sin fundamento. Si cobro y reconocimiento difieren, hacer la transformación explícita. Implantación, expansión y consumo variable se separan cuando usan otra unidad. Renovaciones no duplican altas de clientes que permanecen activos. Separar pérdida de clientes, contracción y expansión de ingreso.

Para cohorte de n nuevos clientes realmente atribuidos y coste total de adquirirlos A_k, `CAC_k = A_k/n` solo con n positivo, población y ventana compatibles y cobertura de intentos sin venta. Con n cero el cociente no existe; el coste sigue existiendo. Para una hipótesis futura con tasas sustentadas, identificarla como tal y recalcular denominador y coste juntos. No asignar probabilidad por etapa.

Valor futuro de contribución por cohorte, si hay fundamento suficiente: `V_k = suma_t(s_t × m_t / (1+d)^t) − costes_iniciales_pertinentes`, donde s es supervivencia compatible, m contribución por superviviente y periodo, d tasa por ese mismo periodo y horizonte acotado. No usar perpetuidad ni la simplificación ARPA/churn por defecto. Sin supervivencia, costes o horizonte defendibles, el valor futuro permanece no calculable. El libro no calcula CAC ni valor futuro automáticamente: recibe sus componentes con cobertura desde N09/N10 y conserva estas reglas.

## Comparación algebraica

Entre dos configuraciones de una misma unidad, `ΔΠ(q)=q(m_B−m_A)−(F_B−F_A)`. Si `m_B≠m_A`, el punto de cruce es `(F_B−F_A)/(m_B−m_A)`; confirmar signo, dominio, capacidad y dirección de preferencia. Si contribuciones iguales, la diferencia depende de fijos; si ambos términos coinciden, el resultado modelado coincide sin demostrar equivalencia de calidad o riesgo.

Inversión o caja inicial adicional no se resta otra vez si ya está reconocida dentro del resultado comparado. Para recuperación de un desembolso adicional usar los flujos incrementales fechados y el primer momento en que su acumulado cubre ese desembolso, sin asumir ahorro constante. Recuperación no es valor actual ni criterio universal de inversión.
