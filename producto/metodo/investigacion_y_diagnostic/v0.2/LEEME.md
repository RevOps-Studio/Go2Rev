# Investigación y recomendación Diagnostic

Versión 0.2 · 11 de septiembre de 2026 · Componente fundacional FND03

Desarrolla N03–N06: mercado y acceso, comprador y compra, alternativas y diferenciación, y decisión de Diagnostic. Se construyen instrucciones, contratos y plantillas vacías. Todos los procedimientos de investigación y decisión descritos corresponden a una futura prestación, posterior a la construcción completa de Go2Rev. Aquí se revisa la documentación del método.

## Finalidad y entrada

Producir conocimiento que permita elegir una ruta comercial delimitada o recomendar su ajuste, aplazamiento o cierre. La investigación debe examinar lo que el encargo da por supuesto y explicar qué aporta frente al conocimiento inicial. La recomendación conecta necesidad, alternativas, oferta, acceso, compra, entrega, cobro y recursos.

La entrada es K01 con iniciativa, ámbito, autoridad y salida prevista, y K02 con representación de oferta, afirmaciones, límites, preguntas y transferencia A o capacidades B. Se utiliza [encargo y conocimiento v0.1](../../encargo_y_conocimiento/v0.1/LEEME.md), sin exigir un diagnóstico ya elaborado ni historial de ventas para comenzar.

La investigación externa es una capacidad sustantiva de Diagnostic. Su lectura de mercado, competidores, productos/soluciones, comprador, tendencias y condiciones debe cruzarse expresamente con la información interna y producir consecuencias para la recomendación. Las fuentes metodológicas del registro de procedencia justifican la construcción de Go2Rev; las fuentes de negocio se obtendrán para cada futura prestación y no se confunden con aquellas.

## Leer y producir por tarea

| Tarea de prestación | Instrucción | Plantilla vacía |
|---|---|---|
| Formular preguntas, descubrir factores, profundizar y decidir suficiencia | [Investigación común](01_investigacion_y_suficiencia.md) | [Preguntas y cobertura](plantillas/01_preguntas_y_cobertura.md) |
| Sugerir fuentes, herramientas y lugares; valorar acceso o MCP | [Rutina breve de fuentes y acceso](09_rutina_de_fuentes_y_acceso.md) | Propuestas dentro de preguntas y cobertura |
| Cruzar conocimiento externo con información del cliente | [Investigación externa y contraste](08_investigacion_externa_y_contraste.md) | [Contraste externo e interno](plantillas/07_contraste_externo_interno.md) |
| Delimitar mercado, estructura, entrada y magnitudes útiles | [N03 Mercado y acceso](02_mercado_y_acceso.md) | [K03](plantillas/02_mercado_y_acceso.md) |
| Comparar segmentos y comprender cómo se decide la compra | [N04 Comprador y compra](03_comprador_y_compra.md) | [K04](plantillas/03_comprador_y_compra.md) |
| Comparar alternativas y formular diferencias defendibles | [N05 Alternativas](04_alternativas_y_diferenciacion.md) | [K05](plantillas/04_alternativas_y_diferenciacion.md) |
| Integrar hallazgos y recomendar una salida de Diagnostic | [N06 Recomendación](05_recomendacion_diagnostic.md) | [K06](plantillas/05_recomendacion_diagnostic.md) |
| Obtener las entradas exploratorias y gestionar iteraciones | [Contratos y economía exploratoria](06_contratos_y_economia_exploratoria.md) | [Intercambio exploratorio](plantillas/06_intercambio_exploratorio.md) |
| Revisar decisiones de reutilización | [Fuentes y correspondencia](07_fuentes_y_correspondencia.md) | Registro de diseño; lectura ajena a la operación ordinaria |

Los registros FUE, AF, HUE, SOL, CON, TRA, CAP, DEC y CAM conservan la semántica de FND02. Las plantillas nuevas son secciones agrupables en K03–K06; no añaden registros paralelos de fuentes ni maestros. La información material se referencia una vez y se consume por campo, versión y uso.

## Operación por conversación

El consultor expresa la decisión que necesita informar. El asistente recupera el encargo y los campos pertinentes, identifica la tarea de la tabla y propone el análisis que realizará. Investiga, compara y redacta la recomendación; solicita al responsable únicamente información exclusiva o autoridad que falte. Los códigos de nodos no son comandos que deba aprender la persona.

Se comienza con una exploración de la situación de compra y del ámbito. Mercado, comprador y alternativas se refinan mutuamente: una alternativa descubierta puede revelar otra forma de segmentar o una barrera distinta. Los cambios se aplican a las dependencias afectadas, conservando lo ya suficiente. No se repite la investigación por cambiar de conversación.

La rutina de fuentes propone candidatas concretas según necesidad y explica su aportación, acceso y limitaciones. El asistente incorpora las pertinentes dentro de la investigación autorizada; una conexión MCP nueva o un gasto se propone con su justificación y requiere la autoridad correspondiente. El cruce entre ambas perspectivas conserva premisas, razonamiento, conclusión y decisión afectada.

El resumen al consultor muestra decisión, hallazgos que la cambian, propuesta, fundamento, límite y siguiente acción. Las decisiones de producto y arquitectura durante la construcción corresponden a Carlos; los procedimientos anteriores describen el trabajo futuro del servicio.

## Capacidades y límites del componente

Se requieren lectura de originales con localizadores, análisis de tablas, escritura editable y, para investigación externa actual, acceso efectivo a las fuentes pertinentes. Si una capacidad falta, se emplean originales accesibles suficientes o se limita la actualidad, cobertura o conclusión. No se presume navegación ni se exige un proveedor, conector o plataforma propia.

FND03 especifica el consumo exploratorio de N08–N12 y la petición de evidencia que puede requerir N14–N16. Sus productores sustantivos están en FND04/FND05 y los protocolos en FND06, enlazados en el [mapa de tareas](../../operacion_conversacional/v0.1/02_rutas_y_lectura.md). Su existencia documental no acredita operación comercial ni protocolos ejecutados.

El [paquete fundacional](../../../paquete_fundacional/v0.1/LEEME.md) identifica la versión del conjunto y su guía de implementación. Las instrucciones son autónomas respecto del archivo de procedencia y de los maestros de desarrollo.
