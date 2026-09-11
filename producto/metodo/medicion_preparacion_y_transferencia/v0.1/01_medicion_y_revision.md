# N13 · Medición y revisión para decidir

Versión 0.1 · Productor de K13

Empezar con la [primera pasada de N13](../../operacion_conversacional/v0.3/10_primera_pasada.md#n13) y aplicar [núcleo y suficiencia](../../operacion_conversacional/v0.3/12_nucleo_y_suficiencia.md). El procedimiento y contrato siguientes gobiernan el análisis completo.


<!-- procedimiento:inicio -->
## Procedimiento de primera pasada

Trabajar con la entrada común y aplicar [INV-01–20](../../operacion_conversacional/v0.3/13_invariantes.md). Los identificadores de campos y bloques se localizan en la plantilla generada; la referencia posterior conserva el razonamiento y sus casos de aplicabilidad.

1. Partir de una decisión que necesita información y de los eventos K09–K12. Precisar objeto, identidad, fecha y unidad de análisis.
2. Definir captura, fuente, responsable, cálculo y corte de cada medida. Abrir relaciones y excepciones si hay agregación, duplicados, faltantes o transición entre sistemas.
3. Diseñar revisión e interpretación: condición, autoridad y acción ante el resultado. Abrir la ficha de revisión para vincular medida y decisión.
4. Entregar K13 a N15 para instrumentar y a N16 para comprobar contenido y funcionamiento pertinentes; mantener límites de cobertura y trazabilidad hasta el original.

**Bloques de salida:** K13.T01.B01. Su condición y momento gobiernan la exigibilidad; las piezas auxiliares se abren según la tarea.
<!-- procedimiento:fin -->

## Referencia sustantiva y condiciones de ampliación


## Pregunta y entradas

Determinar qué información permitiría mantener, ajustar, detener o reabrir una decisión, quién puede actuar y con qué oportunidad. Recibir objetivos/compromisos K01, hipótesis y condiciones K06, eventos K09–K11, magnitudes/umbrales K12 y fuentes/capacidades K02. Incorporar K07/K08 cuando la medida dependa de una versión de mensaje u oferta.

En A, comprobar que las definiciones y poblaciones del origen se transfieren al destino antes de reutilizar una línea base. En B, la ausencia de historial no impide diseñar observación; la línea base se conserva desconocida hasta obtenerla. Medición puede iniciarse para un protocolo de Diagnostic sin exigir Design completo.

## Construir el sistema de medidas

1. **Partir de la decisión.** Identificar compromiso, responsable, alternativas y tiempo en que la información sería útil. Explicar qué cambio de evidencia podría alterar la decisión. Eliminar medidas sin uso; conservar las necesarias para proteger calidad, capacidad o caja aunque no sean indicadores comerciales destacados.
2. **Reconstruir el mecanismo.** Conectar actividad del proveedor, señal del comprador, compra, cumplimiento y caja pertinentes. Separar resultados, condiciones y restricciones. Una medida anterior en el tiempo no es predictora solo por llamarla anticipada: la relación causal o predictiva conserva fundamento e incertidumbre.
3. **Definir el evento.** Describir qué sucede, en qué objeto, cómo se reconoce, fuente que lo acredita y cuándo ocurre. Diferenciar fecha del hecho, registro, recepción y corte. Emisión, aceptación, conformidad, facturación y cobro conservan eventos distintos.
4. **Definir identidad y cálculo.** Fijar unidad, población, inclusión/exclusión, deduplicación, ventana/cohorte, numerador/denominador y dominio. Aplicar las [reglas de cohortes de posición, demanda y conversión](../../posicionamiento_demanda_y_conversion/v0.1/04_costes_cohortes_y_capacidad.md). Repeticiones cuentan para esfuerzo, pero no se convierten en nuevos compradores o pedidos.
5. **Resolver procedencia y disponibilidad.** Para cada entrada, identificar fuente, campo, acceso, calidad, responsable y transformación. Una medida derivada puede combinar varias fuentes; su cálculo tiene una definición vigente y una regla de conciliación. Designar una fuente de referencia no convierte sus datos en ciertos ni elimina discrepancias documentadas.
6. **Separar observación, referencia, objetivo y umbral.** La observación procede del proceso; una referencia externa tiene comparabilidad; el objetivo expresa aspiración/compromiso; el umbral determina una acción. Derivar este último de K12, condición de servicio, riesgo o pregunta de aprendizaje. Sin fundamento cuantitativo, formular condición cualitativa observable o relación simbólica; no inventar línea base, porcentaje de alerta ni intervalo.
7. **Diseñar captura y revisión proporcionadas.** Definir quién registra/calcula, quién interpreta/decide, latencia admisible y evento o periodo de revisión. Ajustar al tiempo de maduración y al plazo para actuar. Elegir medio suficiente manual o automatizado y valorar su mantenimiento en K12. No exigir reuniones, dashboard, North Star ni número fijo de métricas por rol.
8. **Entregar instrumentación y decisiones.** N15 recibe campo, fuente, transformación, acceso, presentación y tratamiento de errores. N16 recibe la trazabilidad a comprobar. N14 recibe lo que precise obtención adicional de evidencia. Cada medida entrega a N17 una instrucción de consulta y de actuación ante cambio.

## Reglas de cálculo e interpretación

| Magnitud | Relación general | Dominio y lectura |
|---|---|---|
| Conteo de eventos u objetos | Cardinalidad del conjunto definido al corte | Distinguir eventos repetidos y objetos únicos. Una fuente sin cobertura no acredita conteo total |
| Tasa de evento | Objetos elegibles con evento / objetos elegibles observados bajo la misma regla | Denominador positivo, identidad compatible y seguimiento pertinente; no contar desconocidos como ausencia de evento |
| Tasa agregada entre grupos disjuntos comparables | Suma de numeradores / suma de denominadores | No media simple de porcentajes. Si poblaciones, ventanas o definiciones difieren, mantener separado |
| Duración observada | Tiempo de fin menos origen según calendario | Separar espera y trabajo si la decisión lo requiere; los abiertos tienen seguimiento incompleto |
| Variación absoluta | Valor actual menos referencia comparable | Ambos conocidos, misma unidad/definición y periodo comparable; conservar signo e interpretación |
| Variación relativa | Diferencia dividida por referencia | Denominador con significado y no nulo; si cero, falta o cambio de signo impide interpretación, usar diferencia y explicación |
| Contribución, caja y carga | Fórmulas vigentes K12 con sus entradas | No redefinirlas en un reporte. Pedido, ingreso reconocido y efectivo cobrado conservan unidades y fechas propias |

La cobertura del dato es una condición del cálculo. Separar universo elegible conocido, observaciones disponibles, registros inválidos, pendientes y ausencia de acceso. Cero observado requiere un periodo/población con captura pertinente; una extracción vacía o fallida no se convierte automáticamente en cero de negocio. Si solo puede calcularse una parte, nombrar el subconjunto y limitar la conclusión.

Una comparación temporal puede cambiar por composición, estacionalidad, precio, oferta, canal o captura. Mostrar esos cambios antes de atribuir el efecto a una actuación. Muestras escasas y cohortes inmaduras no sostienen una tasa estable por repetir la lectura. La atribución comercial mantiene las reglas de posición, demanda y conversión; reparto de crédito no demuestra efecto incremental.

## Captura y corrección de datos

El diseño especifica origen → extracción/recepción → transformación → medida → decisión. Conserva localizador y revisión de la definición. Define unidades, calendario/zona, claves de relación, validaciones pertinentes y tratamiento de duplicados, eventos tardíos y estados contradictorios. No exige una arquitectura técnica nueva: puede resolverse con archivo y conciliación manual si cumple la tarea.

Si llega un dato tarde o se corrige una fuente, conservar el valor publicado al corte y emitir una revisión identificada. No sobrescribir el hecho original ni mezclar cálculos de definiciones incompatibles. Una redefinición puede requerir recalcular la serie desde datos aptos o marcar una discontinuidad; no empalmar series como si fueran equivalentes.

Ante fallo de captura, identificar tramo y datos afectados, detener solo decisiones que dependan de ellos y activar alternativa suficiente. Distinguir reparación técnica, corrección de dato y revisión de hipótesis de negocio. Los accesos y permisos se verifican para el dato necesario; una conexión activa no acredita cobertura ni exactitud.

## Revisión que termina en una decisión

El asistente prepara una lectura con ámbito/corte, qué cambió, calidad del dato, explicación sustentada, explicación contraria, efecto sobre K06–K12 y alternativas de acción. El decisor resuelve dentro de K01/DEC. Puede mantener la decisión cuando el dato aún no permita cambiarla, dejando condición y momento pertinente de revisión; no forzar una decisión nueva en cada reunión.

La [plantilla de revisión](plantillas/02_revision_y_decision.md) conserva responsable, acción, dependencia y condición de comprobación posterior. Un reporte entregado no acredita acción realizada. Si el umbral cambia, registrar motivo y autoridad antes de usarlo; no modificarlo retrospectivamente para presentar cumplimiento.

K13 es suficiente para diseño cuando evento/cálculo, fuente, dominio, responsable y decisión son ejecutables o sus carencias tienen efecto explícito. Para declarar captura disponible y uso comprobado se necesita evidencia de N15/N16 en la prestación. Cambios de oferta, recorrido, fuente, unidad, definición o umbral revisan K13 y sus consumidores mediante CAM.


## Correspondencia mínima con un CRM o registro

Diseñar únicamente los objetos necesarios para las decisiones: cuenta/unidad compradora, persona/rol, oportunidad o pedido, interacción/evento y entrega/cobro cuando proceda. Para cada objeto precisar identidad estable, relación con otros objetos, fuente de referencia, propietario, estados permitidos y evento que cambia el estado. Definir deduplicación, fecha del hecho y registro, campos obligatorios por transición, tratamiento de desconocidos, corrección y permisos.

N15 recibe una correspondencia entre ese contrato y los objetos, campos, relaciones y automatizaciones reales del medio elegido. Registrar qué queda manual, qué no se puede representar y su consecuencia. N16 comprueba captura, transición, conciliación y acceso del alcance configurado; N17 recibe instrucciones de uso y mantenimiento. Un archivo compartido puede ser suficiente si conserva estas funciones; no se impone un CRM ni una plataforma propia.
