# Plantilla · Base de conocimiento K02

Versión de plantilla 0.1 · Campos de prestación vacíos

Usar con [N02](../02_conocimiento_y_solicitud.md) y [contratos](../03_contratos_y_diccionario.md). Las reglas son metadatos; no son afirmaciones de una prestación. Repetir únicamente los registros pertinentes a decisiones materiales. Los bloques pueden separarse en archivos enlazados sin duplicar el contenido.

## Índice y perfil de K02

| Campo | Regla | Valor |
|---|---|---|
| Identificación, revisión y fecha | K02, prestación, autor y revisión; consultor; requerido | |
| Encargo de referencia | K01 y revisión de ámbito/preguntas; requerido | |
| Estado de edición y revisión | Estado, revisor, fecha y cobertura documental; requerido | |
| Oferta e iniciativa | Síntesis de representación y mecanismo con AF/K01; requerido para explorar | |
| Ámbito y recorrido | Origen/destino A o intención/capacidad B; K01; requerido | |
| Situación de compra y roles | Conocido o hipótesis; AF, alcance y límite; lo desconocido se conserva | |
| Forma de venta, entrega y cobro | Unidad, actores y condiciones conocidas; AF; lo desconocido se conserva | |
| Capacidades y restricciones | Síntesis con AF y TRA/CAP; qué uso limitan | |
| Preguntas que orientan el siguiente trabajo | Decisión/nodo y HUE; requerido | |
| Índice de fuentes y afirmaciones | Ubicación de registros FUE y AF vigentes y versiones referenciadas; requerido | |
| Matriz aplicable | Ubicación de transferencia A o capacidades B; requerido según recorrido | |
| Contradicciones, huecos y solicitudes | CON, HUE y SOL pertinentes; indicar cobertura revisada para interpretar ausencia de registros | |
| Decisiones y relaciones de consumo | Ubicación de DEC, artefactos y cambios; requerido cuando existan | |
| Alcance de lectura y límite de la base | Qué materiales/ámbitos fueron examinados y qué queda fuera; requerido | |
| Uso propuesto al receptor | Tarea, campos, versión y limitaciones; receptor evalúa su suficiencia | |

## Fuente FUE · Bloque repetible

Productor: quien obtiene o recibe el material. Requeridos todos los campos aplicables antes de utilizarlo como fundamento. Una fuente no leída se puede inventariar, pero no sustenta una extracción propia.

| Campo | Regla | Valor |
|---|---|---|
| ID y revisión de fuente | Identidad estable y versión de la ficha/material | |
| Título y tipo | Identifica documento, registro, declaración, publicación u otro soporte | |
| Autor o entidad responsable | Productor del contenido, distinto de quien lo recupera | |
| Ubicación del material | Ruta o URL exacta y versión; localizable en el soporte de prestación | |
| Localizador de lectura | Página, sección, tabla/celda, intervalo o referencia equivalente | |
| Fecha del contenido y periodo | Separar producción del material y periodo que describe; conservar desconocidos | |
| Fecha de recepción/consulta | Momento efectivo y responsable de acceso | |
| Procedencia | Interna, externa o derivada; origen del material, no nivel de confianza | |
| Original o lectura secundaria | Si es secundaria, identificar original citado y si fue realmente recuperado | |
| Disponibilidad y cobertura leída | Estado del diccionario, secciones leídas y limitaciones de extracción | |
| Ámbito | Iniciativa, geografía, segmento, población y origen/destino pertinentes | |
| Método de producción | Cómo se obtuvo el contenido o medida, cobertura y sesgos conocidos; desconocido si no consta | |
| Grupo de origen | Fuente primaria o conjunto de datos común; relaciona dependencias y republicaciones | |
| Permiso y límites de uso | Acceso, reproducción, custodia o entrega acordados; no inferir permiso por disponibilidad | |
| Transformación de lectura | Extracción, traducción, transcripción o resumen realizado, autor y pérdida relevante; no aplica si ninguna | |
| Referencias asociadas | AF que utiliza la fuente, copias/ediciones y SOL de origen si corresponde | |

## Afirmación AF · Bloque repetible

Productor: analista. Requerida para toda proposición material consumida. El localizador ha de sostener la proposición exacta en el ámbito atribuido.

| Campo | Regla | Valor |
|---|---|---|
| ID, revisión, autor y fecha | Identidad y contenido de la afirmación | |
| Enunciado | Proposición precisa con condiciones; separar proposiciones con fundamentos distintos | |
| Naturaleza | Observación, declaración, inferencia o hipótesis; las decisiones se registran en DEC | |
| Procedencia | Interna, externa o derivada; independiente de naturaleza | |
| Ámbito y vigencia | Iniciativa, geografía, segmento, población y periodo; origen/destino cuando aplique | |
| Unidad y definición | Unidad/base, eventos o definición de conceptos comparados; no aplica justificado en proposición cualitativa | |
| Soporte y localizador | FUE con revisión y ubicación exacta; en una derivación, también AF de premisas | |
| Atribución y operación de observación | Declarante cuando sea declaración; procedimiento y cobertura cuando sea observación | |
| Evidencia contraria y dependencias | AF/FUE que contradicen o limitan; grupo de origen y alcance del contraste realizado | |
| Juicio de soporte por uso | Por qué pertinencia, calidad, independencia, actualidad y coherencia bastan o no para la tarea | |
| Incertidumbre y limitaciones | Qué no puede concluirse y qué condición sigue desconocida | |
| Uso permitido y excluido | Decisión/campo receptor, E/O y límites; diferenciar explorar y comprometer | |
| Contradicciones y huecos | CON/HUE si procede y efecto sobre uso | |
| Revisor y condición de revisión | Responsable de interpretación, alcance revisado y cambio que obliga a reconsiderarla | |

### Derivación · Obligatoria si AF es inferencia o hipótesis

| Campo | Regla | Valor |
|---|---|---|
| Premisas | AF/FUE con revisión, ámbito y soporte; supuestos sin evidencia identificados como tales | |
| Razonamiento o fórmula | Secuencia que conecta premisas y conclusión; ubicación de cálculo editable si lo hay | |
| Unidades y transformaciones | Dominio, unidades, base temporal y operación sobre los originales cuando corresponda | |
| Explicaciones u opciones alternativas | Alternativas materiales examinadas y por qué se prefieren o descartan | |
| Condición de refutación o cambio | Evidencia o variación de premisa que haría abandonar o limitar la conclusión | |
| Consecuencia de desconocidos | Qué no es calculable o qué elección permanece abierta; desconocido no equivale a cero | |

## Contradicción CON · Bloque repetible

Productor: analista; el responsable del hecho aporta aclaraciones. Requeridos todos los campos aplicables mientras afecte al uso de una afirmación.

| Campo | Regla | Valor |
|---|---|---|
| ID, revisión, autor y fecha | Identidad y contenido | |
| Afirmaciones en conflicto | AF/revisiones y proposición incompatible | |
| Comprobación de comparabilidad | Definición, ámbito, población, periodo, extracción y transformaciones | |
| Efecto sobre el uso | Decisión, cálculo o compromiso afectado y campos que deben limitarse | |
| Explicaciones y contraste propuesto | Diferencia de ámbito, error, cambio real u otra explicación sustentable; material necesario | |
| Responsable y solicitud | Quién aclara/analiza, SOL si procede y evento límite | |
| Estado y resolución | Según diccionario; fundamento y referencias de corrección o conciliación | |
| Uso residual y revisión | Qué puede seguir utilizándose, con qué límite y cuándo reabrir | |

## Hueco HUE · Bloque repetible

Productor: analista con el consumidor. Un hueco persiste aunque la solicitud asociada haya recibido material insuficiente.

| Campo | Regla | Valor |
|---|---|---|
| ID, revisión, autor y fecha | Identidad y contenido | |
| Campo o pregunta pendiente | Qué no se conoce; no presumir que el material no existe | |
| Ámbito, unidad y periodo | Qué haría pertinente una respuesta; no aplica con motivo cuando corresponda | |
| Decisión y uso afectados | Nodo/campo, compromiso y consecuencia de la ausencia | |
| Prioridad razonada | Consecuencia, reversibilidad, momento necesario y esfuerzo proporcionado | |
| Vía de resolución | Fuente esperada, responsable, SOL o trabajo analítico y evento límite | |
| Alternativa y límite de uso | Fuente alternativa, derivación fundamentada, conclusión limitada o compromiso detenido | |
| Estado y fundamento | Abierto, resuelto, uso limitado o no aplica justificado; AF/FUE/DEC que sostiene la disposición | |
| Reapertura y dependencias | Condición que exige reconsiderar y consumidores a revisar | |

## Aplicabilidad de los bloques

Antes de emitir K02, completar el núcleo de [N02 Convertir originales en conocimiento](../../../operacion_conversacional/v0.2/10_primera_pasada.md). Las reglas CONTR, EVAL, USO y de variante de esta plantilla mantienen su momento de exigibilidad. Un bloque condicional se completa cuando afecte al resultado; documentar la condición que lo hace aplicable o su exclusión. Una ausencia material queda localizada y limita el uso dependiente. La cabecera común se registra una vez por artefacto.
