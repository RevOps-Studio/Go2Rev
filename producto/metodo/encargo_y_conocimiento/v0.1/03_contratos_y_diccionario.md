# Contratos de K01, K02 y registros compartidos

Versión 0.1 · Especificación general de intercambio

## Convenciones de uso y formato

Las [plantillas](LEEME.md) contienen campos y reglas de cumplimentación, con la columna de valor vacía. Son definiciones del producto, no registros de una prestación. Durante una prestación se crean únicamente las instancias pertinentes, fuera de las fuentes metodológicas. Las secciones repetibles pueden convivir en un solo documento editable; las referencias permiten localizar cada objeto sin imponer una base de datos.

Un ID identifica de forma estable el objeto; su revisión identifica un contenido. No renumerar objetos para ordenar tablas. Cada referencia material indica ID, revisión y campo o sección. Una fecha identifica cuándo se obtuvo o decidió algo; no sustituye a la revisión. Las versiones que sustentaron una decisión se conservan localizables aunque otra versión pase a ser vigente.

La columna vacía significa que la plantilla aún no se ha utilizado. En una prestación, un campo requerido sin dato se registra **desconocido**, con motivo y HUE cuando afecte a una decisión. **No aplica** exige justificar la condición no activada. Cero es un valor y requiere fundamento. Un guion, silencio o campo vacío no pueden interpretarse como ninguno de esos estados.

Los textos son concisos y específicos. Fechas: año-mes-día, con hora y zona cuando la secuencia importe. Importes: moneda, unidad comercial, periodo y tratamiento de impuestos. Porcentajes: base, numerador y denominador. Duraciones/capacidades: unidad, calendario y periodo. Una fecha no conocida se conserva desconocida, sin sustituirla por la fecha de lectura.

**E** identifica uso exploratorio; **O**, uso para operación preparada. El uso se define por campo o conjunto de campos, no como una calificación de verdad global. La naturaleza y la procedencia acompañan al campo en ambos usos. Ningún estado de edición o recepción convierte una hipótesis en condición cumplida.

## Objetos y responsabilidad

| Objeto | Unidad de registro y prefijo | Productor y autoridad | Consumidor |
|---|---|---|---|
| Encargo | K01, una iniciativa y revisión de alcance | Consultor propone; patrocinador y consultor acuerdan compromisos | N02–N17 según campos |
| Base de conocimiento | K02, índice y perfil de una iniciativa | Asistente analiza; consultor responde de la interpretación | N03–N14; N17 conserva continuidad |
| Fuente | FUE, una versión de un material con ubicación y cobertura leída | Quien recibe o recupera el material | Analista y revisor de la afirmación |
| Afirmación | AF, una proposición material y su uso delimitado | Analista; el declarante se atribuye como fuente | Decisión, cálculo o artefacto dependiente |
| Hueco | HUE, campo o pregunta sin resolver para una decisión | Analista con el consumidor | Responsable de obtención y decisor afectado |
| Solicitud | SOL, petición o tarea de obtención con un productor y alcance | Asistente selecciona; responsable aporta/obtiene | N02 o nodo que necesita el dato |
| Contradicción | CON, conjunto de afirmaciones incompatibles sobre un objeto comparable | Analista propone conciliación; responsable aclara el hecho propio | Consumidores de esas afirmaciones |
| Transferencia | TRA, elemento y condiciones de origen frente a destino | Analista; consultor revisa inferencia | N03–N12 según elemento |
| Capacidad | CAP, capacidad necesaria para una tarea y uso | Analista; propietario acredita disponibilidad | N06, N08–N12, N14 |
| Decisión | DEC, elección sobre un compromiso o criterio identificado | Asistente recomienda; autoridad de K01 decide | Productores y consumidores de lo decidido |
| Artefacto y consumo | K del productor y relación con campos que recibe otro nodo | Productor describe; consumidor evalúa suficiencia | Nodo receptor y N17 |
| Cambio | CAM, modificación material de un campo/premisa y sus efectos | Analista; autoridad revisa compromiso si cambia | Descendientes afectados y N17 |

La inferencia y la hipótesis se registran como AF con un bloque obligatorio de derivación: premisas, razonamiento o fórmula, alternativas, refutación, incertidumbre y uso. Esto evita mantener dos copias de una misma proposición. La naturaleza **decisión** se expresa mediante DEC; AF no duplica su autoridad. El conjunto conserva las cinco naturalezas de la arquitectura.

## Contrato K01

**Productores de entrada:** patrocinador (mandato, decisiones y recursos), producto/operación (representación y capacidades) y consultor (propuesta de prestación). Original y localizador son admisibles antes de asignar FUE. N02 normaliza esos identificadores; no se exige K02 terminado para producir K01.

| Campos consumibles | Condición de suficiencia | Consumidores y uso |
|---|---|---|
| Iniciativa, recorrido, representación y ámbito | Se entiende qué se evalúa; origen/destino o intención/capacidad separados | N02–N12 para seleccionar información y alternativas |
| Objetivo, pregunta y alternativas admitidas | Decisión concreta, responsable y conjunto acotado; foco puede ser resultado de Diagnostic | N02–N06 para investigar y recomendar; N13 para relacionar medidas con decisiones |
| Entregas, exclusiones y acompañamiento | Contenido, destinatario, dependencia, recepción y límite identificados | N06–N17 para construir y recibir solo el alcance habilitado |
| Condiciones de evaluación y salida | Resultado entregable aun con cierre; consecuencias y tratamiento económico determinables antes de contratar | N06 recomienda salida; N17 aplica recepción y terminación |
| Roles, recursos y permisos | Autoridad con rastro; disponibilidad o carencia explícita y momento límite | Cada nodo antes del compromiso dependiente; N14–N16 para actuaciones de preparación y comprobación |
| Decisiones y revisiones | Estado y condiciones vigentes, fuente o DEC y evento de reapertura | Todos los consumidores para conservar autorización y revisar cambios |

**Rechazo localizado:** falta de representación devuelve el campo a N01/producto; alcance incompatible devuelve la propuesta al consultor; autoridad o economía de salida indeterminada impide el compromiso contractual correspondiente. El análisis de preparación del encargo puede continuar. La carencia no se resuelve marcando K01 como revisado.

## Contrato K02

**Entradas:** versión de ámbito/preguntas de K01 y materiales disponibles con su condición de acceso. **Salida:** perfil y referencias a FUE, AF, HUE, SOL, CON, TRA o CAP, más relaciones de consumo. Las matrices pueden integrarse en K02 sin crear nuevos objetos K.

| Campos consumibles | Productor o regla | Consumidores y límite |
|---|---|---|
| Perfil: oferta, situación de compra, modelo de entrega/cobro y capacidades | Síntesis referenciada; N01 define ámbito, N02 interpreta materiales | N03–N06 y N08–N12; no sustituye investigación de destino o diseño |
| Afirmaciones materiales y fuentes | AF + FUE con naturaleza, procedencia, ámbito, localizador y cobertura | Cada nodo toma únicamente las que soportan su pregunta |
| Inferencias e hipótesis | AF con derivación; incertidumbre y refutación explícitas | N06–N14; E permite exploración sin atribuir condición cumplida |
| Transferencia A o capacidades B | TRA o CAP enlazadas con AF y huecos | N03–N12 y N14 para diferenciar lo reutilizable, investigable y por habilitar |
| Restricciones, contradicciones y huecos | Consecuencia, responsable y alternativa por uso | N06 para recomendación; productor afectado para resolver o limitar |
| Solicitudes y cobertura de recepción | Lo pedido, lo recibido, lo analizado y lo pendiente separados | Responsables de obtención; N02 incorpora solo después de examinar |
| Índice de versiones y relaciones | Ubicaciones actuales y referencias conservadas | Reanudación y N17, sin volver a cargar todo el material |

K02 se considera suficiente **para una tarea indicada** si cada entrada material que esta consume tiene soporte pertinente o condición explícita de hipótesis/ausencia compatible con ese uso; si sus límites y contradicciones están visibles; y si se puede localizar su fundamento. Una ausencia que pueda invalidar el compromiso no se neutraliza con una recepción general de K02.

## Transiciones y estados separados

| Eje | Valores o distinciones | Regla de transición |
|---|---|---|
| Edición de artefacto | Borrador, revisado, sustituido | Revisado identifica autor y alcance de revisión; sustituido conserva ubicación del contenido anterior |
| Decisión | Propuesta, aceptada, condicionada, rechazada | Solo la autoridad identificada cambia su disposición. Condicionada especifica parte habilitada y parte detenida |
| Naturaleza del conocimiento | Observación, declaración, inferencia, hipótesis; decisión en DEC | Cambia solo al cambiar el fundamento, conservando la revisión previa; no por aprobar un documento |
| Procedencia | Interna, externa, derivada | Se establece por el origen del conocimiento; una derivación cita sus premisas internas/externas |
| Disponibilidad de fuente | Accesible leída, leída parcialmente, accesible pendiente de lectura, no accesible, original no localizado | Lo no leído no sustenta una extracción propia; la cobertura delimita lo leído |
| Solicitud | Por emitir, emitida, recibida parcial, recibida, no disponible, cerrada | Recibir requiere referencia al material; cerrar exige disposición de cada hueco, incluida limitación justificada |
| Hueco | Abierto, resuelto, uso limitado, no aplica justificado | Resuelto requiere AF/FUE o DEC pertinente. Si se limita el uso, conserva incertidumbre y disparador de revisión |
| Contradicción | Abierta, conciliada por ámbito, corregida, sin resolver con uso limitado | La conclusión conserva ambas referencias y la explicación; no borrar la discrepancia original |
| Situación operativa | Diseñada, preparada, comprobada, real observada | Se atribuye en los nodos correspondientes a una prestación y con su evidencia; encargo y conocimiento no la declara por sí mismo |

El soporte para una afirmación se expresa mediante un juicio por uso, con evidencia a favor/en contra y carencias. No se fija una escala numérica global. La disponibilidad de una capacidad se interpreta con las reglas de la matriz B, sin confundirla con los estados de artefacto o decisión.

## Recepción y dependencia por campos

Antes de consumir una entrada, el analista receptor comprueba identidad, revisión, ámbito/unidades, vigencia y suficiencia para su decisión. Registra la relación cuando el campo sostenga una conclusión o compromiso material; no registra cada frase del documento. La [plantilla de decisiones y cambios](plantillas/06_decisiones_y_cambios.md) incluye esta relación.

La recepción contiene productor y versión, campos recibidos, tarea consumidora, uso E/O, límites y disposición: **admitido**, **admitido con límites** o **devuelto**. Una devolución indica campo, razón, productor responsable y condición para volver a consumir. La aceptación de una entrada por un analista no es autorización de negocio.

Un consumidor que necesita mayor suficiencia identifica qué nueva conclusión pretende sostener y por qué la evidencia previa no basta. No exige completar todas las secciones ajenas a su tarea. La versión exploratoria de N08–N12 puede empezar desde K01/K02 sin N06 final; N06 consume sus conclusiones exploratorias para recomendar. Los contratos de esos componentes desarrollarán su contenido sin cambiar esta distinción.

## Revisión ante cambios

1. Registrar CAM con campo/premisa, versión anterior y propuesta, motivo, fuente, ámbito y autor. Una propuesta de cambio de alcance no modifica por sí sola K01 aceptado.
2. Consultar las relaciones de consumo y derivación. Identificar afectados directos y recorrer sus descendientes hasta que no haya efecto material adicional. Justificar la ausencia de impacto cuando corresponda.
3. Disponer cada efecto: actualizar contenido, recalcular, revisar argumento, retirar uso o sin impacto. Si una premisa indispensable se invalida, marcar el compromiso dependiente pendiente de revisión antes de continuar ese uso.
4. Corregir primero productores, luego consumidores. Preservar versiones que justificaron decisiones anteriores. Solicitar nueva autoridad solo si cambia el compromiso o vence su condición.
5. Cerrar el cambio con versiones resultantes, disposiciones verificadas documentalmente y condiciones pendientes visibles. Un cambio de sesión no es un CAM por sí mismo.

N17 conserva la continuidad de decisiones y cambios en la prestación. Este componente construye la semántica mínima que necesitan los nodos; no añade maestros al desarrollo de Go2Rev.
