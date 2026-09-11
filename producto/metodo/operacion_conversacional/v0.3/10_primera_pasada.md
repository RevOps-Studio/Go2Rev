# Primera pasada y núcleo por resultado

Versión 0.3 · Vista generada de rutas, procedimientos y definición de campos.

Editar los pasos en la instrucción sustantiva, las interfaces en rutas_de_lectura.json y los campos en esquema/v0.1/plantillas.json. La estrella identifica campos de la plantilla principal del resultado; su exigibilidad depende de la condición y momento del bloque/campo. Las piezas auxiliares se activan por la tarea y pueden ser indispensables. Núcleo no significa rellenar todo al abrir la sesión.

<a id="n01"></a>

## N01 · Delimitar encargo y salida

**Entrada:** Mandato y decisión que debe informar Diagnostic.

**Salida:** K01; consumo por N02, N03, N04, N05, N06, N07, N08, N09, N10, N11, N12, N13, N14, N15, N16, N17.

**Cierre:** Durante la redacción conservar pendientes; antes de contratar completar CONTR y antes de evaluar completar EVAL.

**Destino:** 00 Sistema. Mantener fuente, vista e índice.

**Núcleo localizado en la plantilla principal:**
- [Identidad y vigencia](../../encargo_y_conocimiento/v0.1/plantillas/01_encargo.md#k01-t01-b01) · K01.T01.B01
- [Mandato y unidad de encargo](../../encargo_y_conocimiento/v0.1/plantillas/01_encargo.md#k01-t01-b02) · K01.T01.B02
- [Entrega y acompañamiento · Bloque repetible por entrega comprometida](../../encargo_y_conocimiento/v0.1/plantillas/01_encargo.md#k01-t01-b03) · K01.T01.B03
- [Evaluación recibible aunque no continúe la construcción](../../encargo_y_conocimiento/v0.1/plantillas/01_encargo.md#k01-t01-b04) · K01.T01.B04
- [Consecuencias previstas · Todas las salidas admisibles antes de contratar](../../encargo_y_conocimiento/v0.1/plantillas/01_encargo.md#k01-t01-b05) · K01.T01.B05
- [Condiciones económicas · CONTR en todos los campos aplicables](../../encargo_y_conocimiento/v0.1/plantillas/01_encargo.md#k01-t01-b06) · K01.T01.B06
- [Roles, recursos y permisos · Bloque repetible por dependencia material](../../encargo_y_conocimiento/v0.1/plantillas/01_encargo.md#k01-t01-b07) · K01.T01.B07
- [Entrega de K01 y revisión](../../encargo_y_conocimiento/v0.1/plantillas/01_encargo.md#k01-t01-b08) · K01.T01.B08

[Pasos e instrucción](../../encargo_y_conocimiento/v0.1/01_encargo_y_salida.md) · [Contrato completo](../../encargo_y_conocimiento/v0.1/03_contratos_y_diccionario.md)

<a id="n02"></a>

## N02 · Convertir originales en conocimiento

**Entrada:** K01 y originales disponibles.

**Salida:** K02; consumo por N03, N04, N05, N06, N07, N08, N09, N10, N11, N12, N13, N14, N15, N16, N17.

**Cierre:** Cerrar la primera pasada cuando el consumidor pueda identificar qué sabe, qué debe investigar y qué impide su decisión.

**Destino:** 00 Sistema y 02 Anexos. Mantener fuente, vista e índice.

**Núcleo localizado en la plantilla principal:**
- [Índice y perfil de K02](../../encargo_y_conocimiento/v0.1/plantillas/03_conocimiento.md#k02-t03-b01) · K02.T03.B01
- [Fuente FUE · Bloque repetible](../../encargo_y_conocimiento/v0.1/plantillas/03_conocimiento.md#k02-t03-b02) · K02.T03.B02
- [Afirmación AF · Bloque repetible](../../encargo_y_conocimiento/v0.1/plantillas/03_conocimiento.md#k02-t03-b03) · K02.T03.B03
- [Derivación · Obligatoria si AF es inferencia o hipótesis](../../encargo_y_conocimiento/v0.1/plantillas/03_conocimiento.md#k02-t03-b04) · K02.T03.B04
- [Contradicción CON · Bloque repetible](../../encargo_y_conocimiento/v0.1/plantillas/03_conocimiento.md#k02-t03-b05) · K02.T03.B05
- [Hueco HUE · Bloque repetible](../../encargo_y_conocimiento/v0.1/plantillas/03_conocimiento.md#k02-t03-b06) · K02.T03.B06

[Pasos e instrucción](../../encargo_y_conocimiento/v0.1/02_conocimiento_y_solicitud.md) · [Contrato completo](../../encargo_y_conocimiento/v0.1/03_contratos_y_diccionario.md)

<a id="n03"></a>

## N03 · Delimitar mercado y acceso

**Entrada:** Pregunta K01, representación K02 y fuentes externas.

**Salida:** K03; consumo por N04, N05, N06, N09, N11, N12.

**Cierre:** Añadir detalle geográfico o sectorial cuando cambie acceso, entrega, economía o selección; detener la búsqueda por el criterio registrado.

**Destino:** 01 Entregables/Diagnostic. Mantener fuente, vista e índice.

**Núcleo localizado en la plantilla principal:**
- [Definición y estructura](../../investigacion_y_diagnostic/v0.2/plantillas/02_mercado_y_acceso.md#k03-t02-b01) · K03.T02.B01
- [Acceso y condición de entrada · Bloque repetible por factor material](../../investigacion_y_diagnostic/v0.2/plantillas/02_mercado_y_acceso.md#k03-t02-b02) · K03.T02.B02
- [Magnitud · Bloque repetible cuando informe una decisión](../../investigacion_y_diagnostic/v0.2/plantillas/02_mercado_y_acceso.md#k03-t02-b03) · K03.T02.B03
- [Recomendación y recepción](../../investigacion_y_diagnostic/v0.2/plantillas/02_mercado_y_acceso.md#k03-t02-b04) · K03.T02.B04

[Pasos e instrucción](../../investigacion_y_diagnostic/v0.2/02_mercado_y_acceso.md) · [Contrato completo](../../investigacion_y_diagnostic/v0.2/06_contratos_y_economia_exploratoria.md)

<a id="n04"></a>

## N04 · Entender comprador y compra

**Entrada:** K02/K03 y evidencia de procesos y alternativas.

**Salida:** K04; consumo por N05, N06, N07, N08, N09, N10.

**Cierre:** Una conversación exploratoria puede delimitar una hipótesis; la representatividad o conducta real requieren evidencia adicional pertinente.

**Destino:** 01 Entregables/Diagnostic. Mantener fuente, vista e índice.

**Núcleo localizado en la plantilla principal:**
- [Segmento y situación · Bloque repetible](../../investigacion_y_diagnostic/v0.2/plantillas/03_comprador_y_compra.md#k04-t03-b01) · K04.T03.B01
- [Función en la compra · Bloque repetible](../../investigacion_y_diagnostic/v0.2/plantillas/03_comprador_y_compra.md#k04-t03-b02) · K04.T03.B02
- [Transición de compra · Bloque repetible](../../investigacion_y_diagnostic/v0.2/plantillas/03_comprador_y_compra.md#k04-t03-b03) · K04.T03.B03
- [Comparación y foco recomendado](../../investigacion_y_diagnostic/v0.2/plantillas/03_comprador_y_compra.md#k04-t03-b04) · K04.T03.B04

[Pasos e instrucción](../../investigacion_y_diagnostic/v0.2/03_comprador_y_compra.md) · [Contrato completo](../../investigacion_y_diagnostic/v0.2/06_contratos_y_economia_exploratoria.md)

<a id="n05"></a>

## N05 · Comparar alternativas

**Entrada:** Situación K04, mercado K03 y capacidades K02.

**Salida:** K05; consumo por N06, N07, N08.

**Cierre:** Cerrar con diferencias defendibles o ausencia de diferenciación bajo la cobertura; no inventar una ventaja para terminar.

**Destino:** 01 Entregables/Diagnostic. Mantener fuente, vista e índice.

**Núcleo localizado en la plantilla principal:**
- [Universo y comparación](../../investigacion_y_diagnostic/v0.2/plantillas/04_alternativas_y_diferenciacion.md#k05-t04-b01) · K05.T04.B01
- [Alternativa · Bloque repetible](../../investigacion_y_diagnostic/v0.2/plantillas/04_alternativas_y_diferenciacion.md#k05-t04-b02) · K05.T04.B02
- [Hipótesis de diferencia · Bloque repetible cuando exista fundamento](../../investigacion_y_diagnostic/v0.2/plantillas/04_alternativas_y_diferenciacion.md#k05-t04-b03) · K05.T04.B03
- [Síntesis y recepción](../../investigacion_y_diagnostic/v0.2/plantillas/04_alternativas_y_diferenciacion.md#k05-t04-b04) · K05.T04.B04

[Pasos e instrucción](../../investigacion_y_diagnostic/v0.2/04_alternativas_y_diferenciacion.md) · [Contrato completo](../../investigacion_y_diagnostic/v0.2/06_contratos_y_economia_exploratoria.md)

<a id="n06"></a>

## N06 · Recomendar la salida de Diagnostic

**Entrada:** K01–K05 y combinación exploratoria K08–K12.

**Salida:** K06; consumo por N07, N08, N09, N10, N11, N12, N13, N14, N17.

**Cierre:** La autoridad resuelve el compromiso en DEC; una conclusión parcial se declara y una salida de evaluación puede ir directamente a N17.

**Destino:** 01 Entregables/Diagnostic. Mantener fuente, vista e índice.

**Núcleo localizado en la plantilla principal:**
- [Decisión que se presenta](../../investigacion_y_diagnostic/v0.2/plantillas/05_recomendacion_diagnostic.md#k06-t05-b01) · K06.T05.B01
- [Opción o combinación · Bloque repetible para alternativas materiales](../../investigacion_y_diagnostic/v0.2/plantillas/05_recomendacion_diagnostic.md#k06-t05-b02) · K06.T05.B02
- [Comparación y juicio de suficiencia](../../investigacion_y_diagnostic/v0.2/plantillas/05_recomendacion_diagnostic.md#k06-t05-b03) · K06.T05.B03
- [Salida y consecuencias](../../investigacion_y_diagnostic/v0.2/plantillas/05_recomendacion_diagnostic.md#k06-t05-b04) · K06.T05.B04
- [Disposición y transmisión](../../investigacion_y_diagnostic/v0.2/plantillas/05_recomendacion_diagnostic.md#k06-t05-b05) · K06.T05.B05

[Pasos e instrucción](../../investigacion_y_diagnostic/v0.2/05_recomendacion_diagnostic.md) · [Contrato completo](../../investigacion_y_diagnostic/v0.2/06_contratos_y_economia_exploratoria.md)

<a id="n07"></a>

## N07 · Construir posición y mensaje

**Entrada:** Compra K04, alternativas K05, capacidades y oferta.

**Salida:** K07; consumo por N08, N09, N10, N15.

**Cierre:** Volver a N04/N06 si el valor revela otro foco; incorporar DEC para el diseño adoptado y condicionar afirmaciones externas a su soporte.

**Destino:** 01 Entregables/Design. Mantener fuente, vista e índice.

**Núcleo localizado en la plantilla principal:**
- [Identificación y pregunta](../../posicionamiento_demanda_y_conversion/v0.1/plantillas/01_posicionamiento.md#k07-t01-b01) · K07.T01.B01
- [Marco candidato — bloque repetible](../../posicionamiento_demanda_y_conversion/v0.1/plantillas/01_posicionamiento.md#k07-t01-b02) · K07.T01.B02
- [Comparación y recomendación](../../posicionamiento_demanda_y_conversion/v0.1/plantillas/01_posicionamiento.md#k07-t01-b03) · K07.T01.B03

[Pasos e instrucción](../../posicionamiento_demanda_y_conversion/v0.1/01_posicionamiento_y_promesas.md) · [Contrato completo](../../posicionamiento_demanda_y_conversion/v0.1/06_contratos_y_revision.md)

<a id="n08"></a>

## N08 · Definir oferta y precio

**Entrada:** K04/K05 y costes/capacidades de K11/K12.

**Salida:** K08; consumo por N06, N09, N10, N11, N12, N15.

**Cierre:** En exploración, guardar la representación en Diagnostic y mantener la economía en su fuente única; para uso concreto comprobar autoridad y preparación pertinentes.

**Destino:** 01 Entregables/Design. Mantener fuente, vista e índice.

**Núcleo localizado en la plantilla principal:**
- [Campos del resultado](../../oferta_entrega_y_economia/v0.1/plantillas/01_oferta.md#k08-t01-b01) · K08.T01.B01

[Pasos e instrucción](../../oferta_entrega_y_economia/v0.1/01_oferta_y_precio.md) · [Contrato completo](../../oferta_entrega_y_economia/v0.1/07_contratos_y_revision.md)

<a id="n09"></a>

## N09 · Elegir rutas de demanda

**Entrada:** Acceso K03, comprador K04, oferta K08 y capacidad.

**Salida:** K09; consumo por N06, N10, N12, N13, N14, N15.

**Cierre:** Usar una primera ruta suficiente cuando cubra la pregunta y pueda atenderse; ampliar por brecha demostrada, no por cuota de canales.

**Destino:** 01 Entregables/Design. Mantener fuente, vista e índice.

**Núcleo localizado en la plantilla principal:**
- [Propósito, población y mecanismo](../../posicionamiento_demanda_y_conversion/v0.1/plantillas/03_ruta_de_demanda.md#k09-t03-b01) · K09.T03.B01
- [Acceso, secuencia y recepción](../../posicionamiento_demanda_y_conversion/v0.1/plantillas/03_ruta_de_demanda.md#k09-t03-b02) · K09.T03.B02
- [Esfuerzo, comparación y condición de uso](../../posicionamiento_demanda_y_conversion/v0.1/plantillas/03_ruta_de_demanda.md#k09-t03-b03) · K09.T03.B03

[Pasos e instrucción](../../posicionamiento_demanda_y_conversion/v0.1/02_acceso_y_demanda.md) · [Contrato completo](../../posicionamiento_demanda_y_conversion/v0.1/06_contratos_y_revision.md)

<a id="n10"></a>

## N10 · Diseñar compra y traspasos

**Entrada:** K04, oferta, acceso y condiciones de entrega/caja.

**Salida:** K10; consumo por N06, N11, N12, N13, N14, N15.

**Cierre:** Ajustar cadencia a ventana de compra, permiso y capacidad; antes de automatizar comprobar sus eventos, excepciones y autoridad.

**Destino:** 01 Entregables/Design. Mantener fuente, vista e índice.

**Núcleo localizado en la plantilla principal:**
- [Recorrido y objeto](../../posicionamiento_demanda_y_conversion/v0.1/plantillas/04_recorrido_y_transicion.md#k10-t04-b01) · K10.T04.B01
- [Transición o rama — bloque repetible](../../posicionamiento_demanda_y_conversion/v0.1/plantillas/04_recorrido_y_transicion.md#k10-t04-b02) · K10.T04.B02
- [Cierre, variantes y revisión](../../posicionamiento_demanda_y_conversion/v0.1/plantillas/04_recorrido_y_transicion.md#k10-t04-b03) · K10.T04.B03

[Pasos e instrucción](../../posicionamiento_demanda_y_conversion/v0.1/03_conversion_y_compra.md) · [Contrato completo](../../posicionamiento_demanda_y_conversion/v0.1/06_contratos_y_revision.md)

<a id="n11"></a>

## N11 · Diseñar entrega y cobro

**Entrada:** Oferta, aceptación, recursos y restricciones.

**Salida:** K11; consumo por N06, N08, N10, N12, N13, N14, N15.

**Cierre:** Distinguir aceptación, entrega, reconocimiento y caja; completar variantes solo cuando cambien una obligación o relación material.

**Destino:** 01 Entregables/Design. Mantener fuente, vista e índice.

**Núcleo localizado en la plantilla principal:**
- [Campos del resultado](../../oferta_entrega_y_economia/v0.1/plantillas/02_entrega_y_traspaso.md#k11-t02-b01) · K11.T02.B01

[Pasos e instrucción](../../oferta_entrega_y_economia/v0.1/02_entrega_y_cobro.md) · [Contrato completo](../../oferta_entrega_y_economia/v0.1/07_contratos_y_revision.md)

<a id="n12"></a>

## N12 · Analizar economía y capacidad

**Entrada:** Combinación K08–K11 con unidades, periodos y fundamentos.

**Salida:** K12; consumo por N06, N08, N09, N10, N11, N13, N14.

**Cierre:** Calcular cada bloque suficiente y mostrar lo ausente. Las relaciones adicionales de la variante deben quedar explícitas antes de concluir.

**Destino:** 01 Entregables/Economia. Mantener fuente, vista e índice.

**Núcleo localizado en la plantilla principal:**
- [Campos del resultado](../../oferta_entrega_y_economia/v0.1/plantillas/05_modelo_y_conclusion.md#k12-t05-b01) · K12.T05.B01

[Pasos e instrucción](../../oferta_entrega_y_economia/v0.1/03_economia_y_capacidad.md) · [Contrato completo](../../oferta_entrega_y_economia/v0.1/07_contratos_y_revision.md)

<a id="n13"></a>

## N13 · Instrumentar para decidir

**Entrada:** Decisión, eventos, unidades y fuentes.

**Salida:** K13; consumo por N14, N15, N16, N17.

**Cierre:** Instrumentar las decisiones necesarias; incorporar métricas estándar solo con definición y fundamento compatibles.

**Destino:** 01 Entregables/Design. Mantener fuente, vista e índice.

**Núcleo localizado en la plantilla principal:**
- [Campos del resultado](../../medicion_preparacion_y_transferencia/v0.1/plantillas/01_evento_y_medida.md#k13-t01-b01) · K13.T01.B01

[Pasos e instrucción](../../medicion_preparacion_y_transferencia/v0.1/01_medicion_y_revision.md) · [Contrato completo](../../medicion_preparacion_y_transferencia/v0.1/07_contratos_y_revision.md)

<a id="n14"></a>

## N14 · Preparar obligaciones y evidencia

**Entrada:** Obligación K01 o pregunta abierta con alcance.

**Salida:** K14; consumo por N15, N16, N17.

**Cierre:** Para obtención ligera conservar solo los campos aplicables. Fijar los criterios del alcance autorizado antes de producir y comprobar sus piezas.

**Destino:** 01 Entregables/Despliegue y 03 QA. Mantener fuente, vista e índice.

**Núcleo localizado en la plantilla principal:**
- [Campos del resultado](../../medicion_preparacion_y_transferencia/v0.1/plantillas/03_preparacion_y_secuencia.md#k14-t03-b01) · K14.T03.B01

[Pasos e instrucción](../../medicion_preparacion_y_transferencia/v0.1/02_preparacion_y_secuencia.md) · [Contrato completo](../../medicion_preparacion_y_transferencia/v0.1/07_contratos_y_revision.md)

<a id="n15"></a>

## N15 · Producir piezas y configurar medios

**Entrada:** Diseño pertinente, inventario y criterios K14.

**Salida:** K15; consumo por N16, N17.

**Cierre:** Una descripción no acredita configuración. Mantener una sola fuente editable y referenciarla desde la entrega de despliegue.

**Destino:** 05 Operacion. Mantener fuente, vista e índice.

**Núcleo localizado en la plantilla principal:**
- [Campos del resultado](../../medicion_preparacion_y_transferencia/v0.1/plantillas/05_pieza_y_configuracion.md#k15-t05-b01) · K15.T05.B01

[Pasos e instrucción](../../medicion_preparacion_y_transferencia/v0.1/04_materializacion_y_uso.md) · [Contrato completo](../../medicion_preparacion_y_transferencia/v0.1/07_contratos_y_revision.md)

<a id="n16"></a>

## N16 · Comprobar preparación delimitada

**Entrada:** Criterio K14, piezas K15 y medios/operador.

**Salida:** K16; consumo por N14, N15, N17.

**Cierre:** Cumplido, incumplido, inconcluyente o no ejecutado por criterio. La revisión documental no sustituye uso observado cuando este se requiere.

**Destino:** 03 QA. Mantener fuente, vista e índice.

**Núcleo localizado en la plantilla principal:**
- [Campos del resultado](../../medicion_preparacion_y_transferencia/v0.1/plantillas/06_observacion_y_correccion.md#k16-t06-b01) · K16.T06.B01

[Pasos e instrucción](../../medicion_preparacion_y_transferencia/v0.1/05_comprobacion_de_preparacion.md) · [Contrato completo](../../medicion_preparacion_y_transferencia/v0.1/07_contratos_y_revision.md)

<a id="n17"></a>

## N17 · Transferir y cerrar el alcance

**Entrada:** K01, decisión Diagnostic, archivos y cobertura aplicables.

**Salida:** K17; consumo por receptor y continuidad del encargo.

**Cierre:** Una salida Diagnostic recibe solo lo pertinente; conservar la diferencia entre evaluación, diseño, preparación y actuación observada.

**Destino:** 01 Entregables/Despliegue y 00 Sistema. Mantener fuente, vista e índice.

**Núcleo localizado en la plantilla principal:**
- [Estado, contenido y recepción](../../medicion_preparacion_y_transferencia/v0.1/plantillas/08_transferencia_y_soporte.md#k17-t08-b01) · K17.T08.B01
- [Pendiente y acompañamiento — bloques agrupables](../../medicion_preparacion_y_transferencia/v0.1/plantillas/08_transferencia_y_soporte.md#k17-t08-b02) · K17.T08.B02

[Pasos e instrucción](../../medicion_preparacion_y_transferencia/v0.1/06_transferencia_y_cierre.md) · [Contrato completo](../../medicion_preparacion_y_transferencia/v0.1/07_contratos_y_revision.md)
