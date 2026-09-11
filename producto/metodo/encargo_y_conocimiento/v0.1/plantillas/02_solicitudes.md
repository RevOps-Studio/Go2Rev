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
| Contenido solicitado | Dato, documento o aclaración preciso; evitar pedir un diagnóstico elaborado por el cliente; requerido |  |
| Unidad y periodo | Definición, moneda/base, población/cohorte o ventana cuando corresponda; no aplica con motivo en contenido cualitativo |  |
| Material ya revisado | FUE y campos extraídos; delimita lo que no debe volver a pedirse; requerido |  |
| Fuente esperada y productor | Original adecuado y persona/rol que lo aporta u obtiene; requerido |  |
| Responsable de análisis | Quién incorpora y evalúa suficiencia; requerido |  |
| Formato y cobertura admisibles | Exportación, documento, sección o aclaración; mínimo para el uso, sin imponer herramienta; requerido |  |
| Canal y permiso | Medio de obtención y autorización necesaria para contacto/acceso; requerido antes de la acción correspondiente |  |
| Prioridad y consecuencia | Compromiso afectado, reversibilidad y efecto de no obtenerlo; requerido |  |
| Fecha o evento límite | Momento en que cambia o impide el uso; requerido |  |
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

## Redacción de la petición

El texto que se envíe durante la prestación debe expresar: decisión a la que sirve, material exacto, unidad/periodo, forma sencilla de aportarlo, momento necesario y alternativa si no existe. La solicitud permanece como borrador hasta contar con autoridad para enviarla. Su recepción puede ser parcial sin reiniciar la petición completa.

## Aplicabilidad de los bloques

Antes de emitir K02, completar el núcleo de [N02 Convertir originales en conocimiento](../../../operacion_conversacional/v0.3/10_primera_pasada.md). Las reglas CONTR, EVAL, USO y de variante de esta plantilla mantienen su momento de exigibilidad. Un bloque condicional se completa cuando afecte al resultado; documentar la condición que lo hace aplicable o su exclusión. Una ausencia material queda localizada y limita el uso dependiente. La cabecera común se registra una vez por artefacto.
