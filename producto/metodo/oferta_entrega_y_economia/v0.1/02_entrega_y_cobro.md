# N11 · Entrega, cobro y continuidad

Versión 0.1 · Productor de K11

Empezar con la [primera pasada de N11](../../operacion_conversacional/v0.2/10_primera_pasada.md#n11) y aplicar [núcleo y suficiencia](../../operacion_conversacional/v0.2/12_nucleo_y_suficiencia.md). El procedimiento y contrato siguientes gobiernan el análisis completo.

## Decisión y entradas

Diseñar qué trabajo, medios y condiciones hacen cumplible una unidad vendida y permiten completar su ciclo económico. Recibir compromisos K08, condiciones de mercado K03, aceptación/compra K04, recursos K02 y traspaso K10 cuando exista. E utiliza el recorrido representado de compra sin exigir pedido ni K06 definitivo. N12 devuelve límites de recursos, coste y caja.

## Descomposición del cumplimiento

1. Partir de cada entrega y criterio de conformidad de K08. Descomponer insumos, preparación común, tareas por lote, tareas por unidad, revisión de calidad, aceptación, soporte y cierre. Incluir trabajo provocado por excepciones relevantes; no asignar una tasa de retrabajo sin fundamento.
2. Para cada tarea precisar entrada, acción, condición de inicio, salida observable, ejecutor, autoridad, receptor, medio y evidencia de finalización. Separar trabajo activo de espera, plazo de tercero y demora de aceptación. Un mínimo teórico de horas no es una fecha prometible.
3. Identificar recursos indispensables y sustituibles. Registrar unidad de recurso, cantidad/esfuerzo, simultaneidad, calendario, competencia, disponibilidad neta de otros compromisos y rastro de esa disponibilidad. No sumar horas de roles distintos ni sustituir un rol por menor tarifa sin justificar calidad y acceso. Reutilizar CAP/TRA.
4. Detallar dependencias de terceros: especificación del insumo, plazo, lote mínimo, vigencia de oferta, disponibilidad, condición de pago, alternativa y efecto de fallo. La existencia de un proveedor o una capacidad publicada no demuestra reserva, acuerdo o acceso efectivo.
5. Relacionar tareas y partidas con N12. Distinguir inversión/preparación inicial, trabajo repetido, coste por lote, fijo del periodo, capacidad escalonada, incidencias y desembolso. La hora de un trabajador puede consumir capacidad aunque no cause un pago incremental; su remuneración se cuenta una vez en el perímetro pertinente.
6. Construir precedencias y puntos de recepción. Identificar camino que condiciona el plazo, tareas paralelizables, calendarios de cada recurso, límites de concurrencia y qué evento permite prometer fecha. La disponibilidad agregada del periodo es condición necesaria, no comprobación de agenda ni de servicio en una fecha.

## Traspasos y eventos distintos

El [traspaso](plantillas/02_entrega_y_traspaso.md) comunica identidad y revisión de oferta, unidad/cantidad, condiciones aceptadas, exclusiones, pendientes, insumos, receptor y próxima acción. La recepción debe dejar rastro cuando ocurra. Un archivo enviado no acredita recepción ni aceptación.

| Evento | Condición que debe definir K11 | Consecuencia que no se presume |
|---|---|---|
| Aceptación comercial | Alcance, condiciones, autoridad y evidencia del acuerdo | No acredita insumos, disponibilidad ni inicio autorizado |
| Autorización de inicio | Recursos, permisos, insumos y condiciones previas pertinentes | No acredita tarea realizada |
| Entrega realizada | Objeto, versión, lugar/receptor y evidencia | No equivale a conformidad del comprador |
| Conformidad | Criterio, autoridad receptora, plazo acordado y discrepancias | No equivale por sí sola a factura ni cobro |
| Facturación | Emisor, base, importe, documento y condición que la habilita | No convierte ingreso reconocido en efectivo |
| Vencimiento | Regla desde el evento correcto, calendario y excepciones | No acredita pago puntual |
| Cobro observado | Importe, fecha, moneda, comprobante y aplicación a obligación | No demuestra margen ni ausencia de devoluciones futuras |

Definir también pagos a terceros, tributos aplicables, inversiones, financiación comprometida y devoluciones cuando afecten a caja. El reconocimiento económico y el tratamiento fiscal se documentan según condiciones y criterio competente; el modelo general no los decide por la fecha de factura.

## Excepciones y continuidad

Para entrada incompleta, fallo de calidad, demora, impago, cancelación, devolución o cambio de alcance pertinente, precisar disparador, contención, comunicación responsable, autoridad, trabajo correctivo, coste y efecto en plazo/caja. Evitar resolver automáticamente un incumplimiento extendiendo gratis alcance o fechas. Una excepción interna no sustituye el consentimiento externo necesario.

Cuando el modelo incluya garantía, soporte, renovación o expansión, definir cobertura, periodo, evento de activación/cierre, carga de recursos, precio y aceptación. Renovación prevista no es renovación observada; expansión requiere nuevo alcance y capacidad. Retención no se añade a ofertas que finalizan con su entrega.

A compara medios y condiciones del destino con el origen. B describe qué debe habilitarse y cuándo; ese diseño no declara disponibilidad. Aplicar [variantes](05_variantes_de_oferta_y_operacion.md) para producto físico, servicio/proyecto, recurrencia, distribución y autoservicio, combinándolas cuando corresponda.

## Salida y calidad

K11 reúne mapa de tareas y precedencias, recursos, traspasos, aceptación, costes, eventos de caja, incidencias, compromisos pendientes y condiciones de revisión. N08 recibe cambios de alcance/precio; N10 inicio/traspaso; N12 economía; N13 eventos; N14–N16 requisitos y recorridos que habrá que preparar y comprobar en la prestación futura.

E admite estimación descompuesta con procedencia y límites. Un coste desconocido no es gratuito. O requiere personas, medios, receptores y condiciones efectivos para el compromiso; el diseño de este componente no sustituye su comprobación posterior. Revisar si cada promesa tiene trabajo y recepción, si cada trabajo tiene recurso y coste pertinente, y si cada obligación tiene evento económico y de caja identificable. La carencia afecta al compromiso dependiente.

Cambios en alcance, proveedor, disponibilidad, tiempo, aceptación o pago reabren K08/K10/K12 y K06 cuando alteran la tesis. Aplicar CAM por campo, conservar las versiones y hechos previos, y actualizar las instrucciones y materiales consumidores antes del uso afectado.
