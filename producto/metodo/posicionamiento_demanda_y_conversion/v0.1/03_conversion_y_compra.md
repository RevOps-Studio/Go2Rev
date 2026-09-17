# N10 · Conversión y recorrido de compra

Versión 0.1 · Productor de K10

Empezar con la [primera pasada de N10](../../operacion_conversacional/v0.4/10_primera_pasada.md#n10) y aplicar [núcleo y suficiencia](../../operacion_conversacional/v0.4/12_nucleo_y_suficiencia.md). El procedimiento y contrato siguientes gobiernan el análisis completo.


<!-- procedimiento:inicio -->
## Procedimiento de primera pasada

Trabajar con la entrada común y aplicar [INV-01–21](../../operacion_conversacional/v0.4/13_invariantes.md). Los identificadores de campos y bloques se localizan en la plantilla generada; la referencia posterior conserva el razonamiento y sus casos de aplicabilidad.

1. Recuperar compra K04, oferta K08, ruta K09 y condiciones K11/K12. Representar objeto de trabajo, decisiones del comprador, estados y eventos observables.
2. Definir para cada transición el criterio discriminante, acción, responsable, información y receptor. Separar pertinencia e intención; incorporar retorno, excepción y cierre.
3. Abrir recepción/seguimiento para fijar cadencia conforme a ventana de compra, permiso y capacidad. Abrir costes y cohortes antes de valorar el recorrido.
4. Entregar K10 con evidencia de evento, traspasos, condiciones económicas y límites. Para automatizar, transmitir a N14/N15 eventos, excepciones y autoridad y fijar la comprobación pertinente.

**Bloques de salida:** K10.T04.B01, K10.T04.B02, K10.T04.B03. Su condición y momento gobiernan la exigibilidad; las piezas auxiliares se abren según la tarea.
<!-- procedimiento:fin -->

## Referencia sustantiva y condiciones de ampliación


## Decisión y entradas

Diseñar cómo una señal llega a una decisión de compra, quién hace el trabajo y qué evidencia habilita cada compromiso. Recibir K04 roles/criterios/recorrido, K09 origen y señales, K08 unidad/condiciones, K11 inicio y cumplimiento, y K12 límites. K07 aporta mensajes para el ámbito habilitado. Para E se representa el recorrido y su esfuerzo sin requerir comprador contactado, acuerdo, K07 definitivo ni K06 final.

Cuando exista un proceso propio en una prestación, comparar descripción con eventos y fuentes reales. En A examinar diferencias de compra en destino; en B construir una hipótesis de recorrido sin presentar un historial inexistente. El diseño no presupone departamentos separados, cargos comerciales ni un CRM.

## Diseñar desde las decisiones del comprador

1. **Definir objeto y fronteras.** Precisar cuenta, unidad compradora, ocasión, acuerdo/pedido y unidad vendida. Separar varias personas de una misma decisión y varias decisiones de una misma cuenta. Delimitar dónde termina la generación/recepción de señal y comienza el trabajo de conversión; asignar propietario único de cada actividad/coste, aunque lo haga la misma persona.
2. **Mapear decisiones y riesgos.** Identificar qué debe comprender o resolver el comprador, quién participa, qué criterio aplica, qué documento/evidencia necesita y qué autoridad compromete. Incluir evaluación técnica, económica, contractual o de suministro cuando sean pertinentes; no presumir presupuesto o jerarquía por tamaño de empresa.
3. **Crear etapas solo con función.** Separar una etapa cuando cambie decisión, requisito, ejecutor/receptor o compromiso. Puede haber ramas, tareas paralelas y retorno. El orden comercial diseñado no fuerza al comprador a seguirlo. Una propuesta redactada es actividad del proveedor; su aceptación necesita un evento distinto.
4. **Especificar cada transición.** Definir origen/destino, proposición que debe cumplirse, evidencia y fuente adecuadas, ejecutor, autoridad, receptor, efecto permitido y condición de devolución/espera/cierre. Distinguir condición cumplida, incumplida, desconocida y no aplicable justificada; la condición de avanzar se satisface solo con lo exigible para ese paso. Lo desconocido no se convierte en incumplimiento factual ni se admite como cumplido.
5. **Separar pertinencia e intención.** La pertinencia relaciona situación, comprador, oferta y capacidad de servir; la intención necesita una señal compatible con una decisión de compra. Evaluar ambas para la siguiente acción. Puede ser legítimo aclarar un dato sin abrir una oportunidad; la decisión debe decir qué habilita. No imponer etiquetas MQL/SAL/SQL, marcos de cualificación ni puntuaciones. Si se adopta un criterio compuesto, cada condición conserva significado y una imposibilidad material no se compensa con otras puntuaciones.
6. **Definir oportunidad y cierre por evidencia.** Cuando la ruta necesite ese objeto, especificar qué ocasión, necesidad/alcance, contraparte y siguiente decisión justifican trabajarlo, con fuente de origen y señal. No convertir toda cuenta pertinente en oportunidad. Distinguir acuerdo comercial aceptado, pedido firme bajo condiciones, autorización de inicio, entrega y cobro; el cierre de venta usa un criterio explícito y no representa todos esos eventos a la vez.

## Acción, asignación y seguimiento

7. **Construir el trabajo de cada etapa.** Precisar propósito, entrada, contenido/material requerido, acción, salida y lugar de recepción. Para aclarar una necesidad, examinar primero la información disponible y formular preguntas discriminantes sobre la decisión; evitar cuestionarios por rutina. Para explicar o comparar, utilizar K07/K08 y evidencia apropiada. Para una oferta económica, conservar unidad, precio, condiciones y facultad de excepción. El asistente redacta y analiza; las interacciones se realizarán únicamente en la prestación autorizada.
8. **Tratar objeciones como información.** Relacionar duda con criterio K04, distinguir falta de comprensión, falta de evidencia, incompatibilidad y cambio de prioridad. Responder con evidencia/condición pertinente o reconocer el límite. Un problema de capacidad no se resuelve con un argumento; un cambio de alcance vuelve a N08/N11/N12. Registrar la necesidad de prueba en N14 cuando proceda, sin ejecutar ni inventar su resultado.
9. **Asignar receptor y respaldo.** Definir asignación por competencia, ámbito, disponibilidad y conflicto pertinente; quién acepta la recepción, qué ocurre si la rechaza y qué sucede si el responsable no está disponible. Una asignación propuesta o nombre de rol no acredita persona y tiempo reales. No repartir entre recursos no intercambiables como si fueran capacidad conjunta.
10. **Dimensionar respuesta y cadencia.** Definir evento que inicia el reloj, calendario/zona, trabajo necesario, tiempo de espera permitido y condición de revisión/escalado. Distinguir confirmación de recepción y resolución. Proponer ritmo y límite de seguimiento según urgencia documentada, preferencia del destinatario, ciclo de compra, coste y capacidad; no fijar intentos, horas o semanas universales. Que una actuación pueda automatizarse no demuestra que el receptor esté atendido.
11. **Resolver ausencia y devolución.** Ante información incompleta, rechazo, silencio, aplazamiento, imposibilidad o cambio, definir responsable, motivo, estado de la decisión, tarea permitida, evidencia pendiente y condición de reapertura. Una devolución exige contenido útil para el receptor; no consiste en devolver todo a una secuencia genérica. La falta de respuesta no prueba falta de necesidad ni autoriza contacto indefinido. Conservar motivos declarados, observados e inferidos separados.
12. **Cerrar traspaso a cumplimiento.** N11 recibe identidad del acuerdo, oferta/revisión, unidades/cantidades, entregas/exclusiones, condiciones efectivamente aceptadas, autoridad, insumos, fechas/reglas, obligaciones económicas, pendientes y receptor. Diferenciar enviado de recibido y de autorizado para iniciar. Si el cliente cambia condiciones, resolver versiones y autoridad antes de comenzar el trabajo afectado.

## Cantidades y expectativa de compra

Cada etapa define qué mide y con qué unidad/cohorte/ventana. No asignar probabilidad por nombre de etapa ni producir ingreso esperado multiplicando un importe por un porcentaje arbitrario. Una aceptación condicionada conserva sus condiciones; la previsión de fecha no es un acuerdo.

Si existen datos pertinentes durante una prestación y la decisión requiere una estimación, usar las [reglas de cohortes y dominio](04_costes_cohortes_y_capacidad.md). Separar cantidades acordadas, decisiones abiertas y resultados hipotéticos, con fecha de corte, evidencia y límites. No es obligatorio producir forecast para poder diseñar un proceso ni sumar todos los acuerdos potenciales como capacidad comprometida.

## Salida, suficiencia y cambios

K10 reúne recorrido/ramas, condiciones de transición, evidencia, trabajo y materiales, responsables, respuesta/seguimiento, cierre, devolución y traspaso. N12 recibe cantidad de actividades, esfuerzo por recurso, costes y tiempos de todos los intentos; N13 recibe definiciones de evento; N15 instrucciones/piezas; N16 acciones críticas y criterios que tendrá que comprobar.

E basta para examinar plausibilidad y carga cuando las hipótesis y ausencias están delimitadas. Para O, cada compromiso necesario requiere receptor, medio, contenido, condiciones y preparación efectivos; preparación y transferencia especifica su comprobación futura. Una tabla de etapas completa no demuestra uso ni conducta de compradores.

El consultor revisa diseño; el responsable comercial y operación confirman factibilidad y recepción; el patrocinador decide compromisos/excepciones conforme a K01. Cambios de comprador, oferta, señal, autoridad, capacidad o cobro reabren campos y transiciones afectados. Conservar eventos previos y su versión, corregir la interpretación sin fabricar un evento anterior, y retirar uso de materiales que se hayan quedado sin fundamento.


## Preguntas discriminantes y regla de seguimiento

Seleccionar únicamente preguntas cuya respuesta cambie una transición: qué hecho abrió la necesidad; qué ocurre si no se cambia; cómo se resuelve hoy; qué criterio decide entre alternativas; quién puede aceptar y qué necesita comprobar; qué condición o fecha limita el compromiso. Recuperar primero las respuestas ya documentadas y solicitar hechos concretos cuando hagan falta. Registrar ausencia o contradicción sin inventar intención de compra.

Para cada seguimiento, definir desencadenante, información útil que aporta, destinatario, espera razonada y salida por respuesta, rechazo, aplazamiento o falta de pertinencia. La cadencia se deriva del ciclo de decisión, preferencia, coste y capacidad. Una secuencia de contactos no es una obligación independiente de esos criterios.
