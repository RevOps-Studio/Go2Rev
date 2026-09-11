# Plantilla · Solicitud selectiva y recepción

Vista generada · Corregir la [definición de campos](../../../esquema/v0.1/plantillas.json), no esta vista. ★ = campo de la plantilla principal: aplicar condición y momento; las piezas auxiliares pueden ser indispensables. Cabecera: identidad, versión, ámbito y K01, autor y fecha, ubicación, estado documental, receptor y uso. Registrar una vez por artefacto; los bloques remiten a ella. FUE, AF y otros registros con identidad propia conservan sus metadatos. La aceptación se localiza en DEC.


Versión de plantilla 0.1 · Campos de prestación vacíos

Usar con [N02](../02_conocimiento_y_solicitud.md) y [diccionario](../03_contratos_y_diccionario.md). Cada bloque describe una SOL repetible. El asistente lo redacta después de revisar lo disponible. La columna Valor queda vacía en la fuente metodológica.

## Necesidad y obtención

<a id="k02-t02-b01"></a>

<!-- bloque: K02.T02.B01 -->
| Campo | Regla | Valor |
|---|---|---|
| ID, revisión, autor y fecha | Identidad estable SOL y contenido; requerido al crear la petición |  |
| K01 y ámbito | Revisión de encargo, iniciativa, geografía/segmento y recorrido pertinentes; requerido |  |
| Huecos y decisión consumidora | Referencias HUE, nodo, campo y decisión que necesita la información; requerido |  |
| Contenido solicitado | Dato, documento o aclaración preciso; aprovechar material existente y pedir solo la carencia residual. El consultor produce el análisis contratado; requerido |  |
| Unidad y periodo | Definición, moneda/base, población/cohorte o ventana cuando corresponda; no aplica con motivo en contenido cualitativo |  |
| Material ya revisado | FUE y campos extraídos; delimita lo que no debe volver a pedirse; requerido |  |
| Fuente esperada y productor | Original adecuado y persona/rol que lo aporta u obtiene; requerido |  |
| Responsable de análisis | Quién incorpora y evalúa suficiencia; requerido |  |
| Formato y cobertura admisibles | Original, exportación, sección o aclaración; cobertura suficiente por contenido, ámbito, selección, unidad y periodo, sin imponer herramienta ni cuotas universales. El asistente normaliza; requerido |  |
| Canal y permiso | Medio de obtención y autorización necesaria para contacto/acceso; requerido antes de la acción correspondiente |  |
| Prioridad y consecuencia | Recuperar de HUE prioridad y uso afectados: imprescindible, deseable u opcional para esa decisión. Precisar consecuencia, reversibilidad, trabajo que puede continuar y esfuerzo estimado si añade elaboración al cliente; compararlo con utilidad y alternativa antes de pedir; requerido |  |
| Fecha o evento límite | Momento antes del que cambia o impide el uso: CONTR/EVAL o USO dependiente; conservar condiciones ya acordadas, sin exigir toda la información al inicio; requerido |  |
| Alternativa si no existe | Otra fuente, derivación sustentable, límite de conclusión o suspensión del uso; requerido |  |
| Estado de solicitud | Según diccionario; requerido, con fecha de la transición |  |

## Recepción · Bloque repetible por material o respuesta recibida

<a id="k02-t02-b02"></a>

<!-- bloque: K02.T02.B02 -->
| Campo | Regla | Valor |
|---|---|---|
| SOL y fecha de recepción | Enlace a petición y momento recibido; completar solo cuando se reciba |  |
| Material recibido | FUE/original, versión y localizador; quien lo recibe |  |
| Cobertura y legibilidad | Qué campos/periodos llegaron y cuáles se pudieron leer; analista |  |
| Diferencias respecto a solicitud | Omisiones, ámbitos, unidades o condiciones distintos; analista |  |
| Afirmaciones incorporadas | AF y revisión, tras examinar el original; analista |  |
| Disposición por hueco | HUE resuelto, aún abierto, uso limitado o no aplica justificado; fundamento y consumidor |  |
| Petición residual o alternativa | Qué falta, quién actúa y cuándo; solo por contenido aún necesario |  |
| Cierre de solicitud | Fecha, motivo y disposición de todos sus huecos; recibir un archivo no basta para cerrar |  |

## Comunicación inicial

<a id="comunicacion-inicial"></a>

Vista preparada por el consultor desde K01/K02 y las SOL seleccionadas. Sustituir los marcadores con contenido sustentado de la prestación y retirar los párrafos que no apliquen antes de enviar. Conservar el rastro de la revisión enviada en SOL; no generar otro registro de estado. Consultar la [guía de intake](../04_intake_diagnostic.md).

**Asunto:** Inicio de Diagnostic de {{iniciativa}}

Trabajaremos para ayudarte a decidir {{decisión y ámbito acordados}}. Con lo que ya hemos revisado, entendemos que {{síntesis breve de la iniciativa y la oferta}}. El punto que necesitamos que confirmes o corrijas es {{aclaración factual o decisión pendiente y responsable}}.

Ya contamos con {{material efectivamente recibido y cobertura revisada}}. Para empezar, puedes facilitarnos {{selección de materiales existentes todavía necesarios y propietario, si se conoce}} mediante {{canal y ubicación autorizados}}. Nos sirve {{formato y cobertura admisibles}}; nosotros extraeremos y ordenaremos la información.

Necesitaremos {{aportación imprescindible}} antes de {{evento dependiente y motivo}}. {{Material deseable, utilidad y momento, solo si procede}}. Si un material no existe, no lo localizas, está desactualizado o no puedes compartirlo, indícanos cuál: revisaremos la alternativa y su efecto sobre la evaluación.

Go2Rev preparará la investigación externa, su contraste con vuestra información y la propuesta de diagnóstico. En {{siguiente resultado o evento acordado}} compartiremos {{interpretación o resultado controlable}} y las aclaraciones concretas que sigan siendo necesarias.

## Ampliación o aclaración posterior

Para resolver {{decisión o conclusión afectada}}, ya hemos revisado {{material y parte cubierta}}. Falta {{dato o aclaración residual}}; nos sirve {{original, formato, unidad, periodo y cobertura pertinentes}} de {{propietario}} antes de {{evento y motivo}}.

La aportación supondría {{trabajo adicional y estimación de esfuerzo, solo si exige elaborarlo}}. Si no está disponible, la alternativa es {{alternativa y límite de conclusión}}. Mientras tanto, avanzaremos con {{trabajo independiente permitido}}.

Los marcadores son instrucciones de composición, no valores de un encargo. Una petición sin carencia concreta se omite. La autorización vigente se recupera de K01; el texto no autoriza por sí mismo contacto o acceso.


## Redacción de la petición

El texto que se envíe durante la prestación debe expresar: decisión a la que sirve, material exacto, unidad/periodo, forma sencilla de aportarlo, momento necesario y alternativa si no existe. La solicitud permanece como borrador hasta contar con autoridad para enviarla. Su recepción puede ser parcial sin reiniciar la petición completa.

## Aplicabilidad de los bloques

Antes de emitir K02, completar el núcleo de [N02 Convertir originales en conocimiento](../../../operacion_conversacional/v0.3/10_primera_pasada.md). Las reglas CONTR, EVAL, USO y de variante de esta plantilla mantienen su momento de exigibilidad. Un bloque condicional se completa cuando afecte al resultado; documentar la condición que lo hace aplicable o su exclusión. Una ausencia material queda localizada y limita el uso dependiente. La cabecera común se registra una vez por artefacto.
