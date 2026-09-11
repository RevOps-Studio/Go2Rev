# Carpetas y guardado del encargo

Versión 0.2 · Convención operativa común a los diecisiete nodos

Preparar una raíz persistente por encargo. La biblioteca Go2Rev conserva una versión identificada y sus plantillas vacías; el trabajo propio se guarda en esta raíz, fuera de la biblioteca. El nombre del encargo procede del mandato recibido. Una sesión utiliza el espacio existente y actualiza sus archivos.

## Estructura predeterminada

| Carpeta | Contenido vigente | Regla de ubicación |
|---|---|---|
| 00 Sistema | Encargo, índice, decisiones, fuentes y afirmaciones, cambios, continuidad | Agrupar los registros de K01/K02/K17; usar un solo índice localizable |
| 01 Entregables/Diagnostic | Investigación interpretada y recomendación de evaluación | Mantener aquí sus fuentes editables y vistas de lectura |
| 01 Entregables/Design | Diseño de posición, oferta, acceso, compra, entrega y medición | Una fuente por contenido, referenciada por los informes que lo consumen |
| 01 Entregables/Economia | Libro y relaciones económicas vigentes | Conservar una fuente de cálculo por combinación identificada; Diagnostic y Design la referencian |
| 01 Entregables/Despliegue | Preparación, cobertura, recepción y transferencia | Relacionar obligaciones con piezas de Operación y evidencia de QA |
| 02 Anexos/Material del cliente | Originales recibidos y sus sucesivas versiones | Conservar identidad y procedencia, incluidos límites de lectura |
| 02 Anexos/Investigacion externa | Documentos, datos y capturas de fuentes externas autorizadas | Registrar en FUE el original o URL, fecha y cobertura; un enlace puede conservar una fuente que no se puede redistribuir |
| 02 Anexos/Actas y transcripciones | Relatos, actas y registros de conversaciones | Distinguir original, transcripción, resumen y acuerdo; DEC registra la autoridad del acuerdo |
| 03 QA | Protocolos, revisión de contenido y resultados de comprobación | Identificar criterio, versión, autor y estado; protocolo diseñado y resultado observado son contenidos distintos |
| 04 Archivo | Fuentes editables y vistas sustituidas que sustentaron decisiones | Conservar la ruta relativa anterior bajo una revisión identificada; actualizar el índice y enlaces afectados |
| 05 Operacion | Materiales y guías para ejecutar las tareas comprometidas | Fuente editable de cada pieza, vistas y configuración o referencia al sistema efectivo |

Dentro de cada conjunto de Entregables y de Operacion usar `Fuentes` para editar y `Lectura` para las vistas destinadas al receptor. Se crean cuando exista el primer contenido de ese tipo. Los documentos pueden estar en borrador, revisados o entregados dentro de su ubicación: la carpeta no acredita su estado. Un material en Operacion necesita la evidencia pertinente antes de anunciar preparación comprobada.

## Preparación inicial y continuación

1. Localizar la raíz acordada y comprobar si ya contiene un encargo. Recuperar su índice y versión del método antes de crear archivos.
2. Si es un inicio, preparar las seis carpetas principales y las subdivisiones de Entregables y Anexos. Incorporar un índice vacío de continuidad en `00 Sistema`; redactar K01 con la información autorizada. Crear los demás archivos cuando exista contenido útil para su función.
3. Si hay una estructura previa que debe respetarse, registrar una tabla de correspondencia entre estas funciones y sus ubicaciones reales en el índice. Mantener esa correspondencia en todos los guardados. Una carpeta inaccesible queda pendiente; no se declara creada.
4. En una continuación, abrir el índice, las decisiones y el contenido de la tarea. Completar solo las ubicaciones necesarias que falten. Conservar los archivos existentes y conciliar revisiones incompatibles antes de sustituirlas.

La [estructura vacía](../../../paquete_fundacional/v0.2/LEEME.md) se distribuye como ZIP independiente, con instrucciones y una plantilla de índice. Prepararla es una operación documental; no habilita contratación, contacto ni actuación comercial por sí sola.

## Regla de destino por resultado

Cada nodo puede producir varios tipos de resultado. El original recuperado va a Anexos; su interpretación a la fuente del entregable; una decisión a Sistema; un protocolo o comprobación a QA; una pieza de uso a Operacion. La [primera pasada por nodo](10_primera_pasada.md) concreta los destinos y el núcleo de contenido de cada salida.

El cruce entre evidencia externa y datos del cliente se redacta en la fuente de Diagnostic, con referencias a ambos originales. Las actas de reconciliación pueden conservarse en Anexos, mientras la conclusión vigente se integra en su productor. Evitar repartir una misma condición o fórmula entre originales editables independientes.

## Nombrar y conservar

Usar `ID - Titulo - vN.ext`, con identidad estable por pieza y título comprensible. La versión identifica contenido; el estado se registra en el documento y en el índice. Los originales externos mantienen su nombre recibido siempre que sea posible y obtienen su ID en FUE. E y O describen el uso habilitado, no una numeración de versiones ni carpetas nuevas.

Antes de sustituir contenido que fundamentó una decisión, conservar su versión en Archivo y sus localizadores históricos. Las vistas de esa fuente se regeneran o se marcan pendientes. Una corrección que no altera significado puede conservar versión, con fecha y alcance de revisión en el índice. Un cambio material conserva versión anterior y CAM; si cambia un compromiso, se obtiene la decisión correspondiente.

## Cierre de cada tarea

1. Determinar tipo de resultado, fuente editable, revisión base y ruta de destino.
2. Producir el contenido y revisar su fundamento, interfaces y legibilidad.
3. Guardar y volver a leer lo escrito. Actualizar la vista cuando corresponda.
4. Actualizar en el índice la ruta, versión, estado, decisión, pendientes y siguiente acción. Mantener las referencias históricas que sigan siendo necesarias.
5. Comunicar resultado y enlace o archivo recibido. Si solo se entrega texto o una descarga, indicar el destino previsto y la persistencia pendiente.

La descarga de una sesión no confirma que la carpeta del consultor haya cambiado. En un medio sin escritura, entregar un ZIP de cambios con rutas relativas y una relación de altas/sustituciones; el responsable conserva la versión anterior e incorpora los cambios. La siguiente sesión usa esa copia actualizada. Las instrucciones de [uso por entorno](09_uso_por_entorno.md) precisan la preparación y la continuidad.
