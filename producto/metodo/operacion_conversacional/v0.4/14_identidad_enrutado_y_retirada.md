# Identidad, enrutado y retirada de trabajo incompatible

Versión 0.1 · Protocolo transversal de activación

## Identidad del método

Una sesión aplica Go2Rev cuando puede localizar una versión identificada de su entrada común, sus invariantes, el índice del encargo y las instrucciones del nodo productor. Go2Rev tiene diecisiete nodos N01–N17 y contratos K01–K17. RevOS 4.4.0 y GTM Planner 0.3.0 aportaron referencias selectivas durante la construcción; no forman parte de la ejecución, no añaden pasos y no gobiernan decisiones del encargo.

Compartir vocabulario con otra metodología no constituye conflicto. El conflicto aparece cuando una regla, secuencia, precondición, plantilla o salida ajena pretende gobernar el trabajo sin estar incorporada expresamente a la versión de Go2Rev utilizada.

## Puerta de enrutado

Antes de producir un resultado dependiente del método, el asistente comprueba y comunica un recibo breve:

| Elemento | Comprobación | Disposición si falta o discrepa |
|---|---|---|
| Método y versión | Paquete Go2Rev vigente según índice y localizador accesible | Estado detenido hasta identificar una versión íntegra |
| Encargo | Identidad, raíz, K01 y autoridad pertinentes | Limitar la producción al encuadre recuperable |
| Tarea | Nodo productor, contrato de salida, receptor y uso E/O | Resolver el productor; no elegir por semejanza léxica |
| Instrucciones | `CARGA_INICIO.md`, carga del nodo y extensiones activadas efectivamente leídas | Abrirlas o declarar la dependencia ausente |
| Fuentes de contenido | Originales internos/externos necesarios y cobertura leída | Registrar HUE y avanzar solo lo independiente |
| Enrutado | Conforme, limitado o detenido, con motivo | No ocultar la limitación en una nota final |

El recibo no necesita un documento separado cuando esos campos consten en la respuesta y el índice. En una continuación sin cambios, basta confirmar la versión, la tarea y cualquier variación de acceso.

## Elegir tarea y tratar precondiciones

La petición se relaciona con el resultado que debe producirse y con su contrato, no con el nombre más parecido de una skill. Si varias tareas Go2Rev pudieran producirlo, usar K01, la última decisión y los consumidores para resolver la ruta. Si aún quedan alternativas incompatibles, avanzar sus partes comunes y solicitar únicamente la decisión discriminante.

Una precondición se evalúa por el uso dependiente. Se considera crítica cuando su ausencia puede cambiar la identidad del método, la autoridad, el ámbito, el fundamento material, una cifra o el compromiso que se pretende emitir. En ese caso, el resultado queda limitado o detenido hasta resolverla. Las tareas independientes pueden continuar con fuentes y límites propios; nunca heredan por proximidad una regla de otro método.

## Objetivos, cálculos y recomendaciones

Un objetivo puede definir el umbral que una combinación debería alcanzar. Despejar una ecuación desde ese objetivo produce un valor requerido, no evidencia de que el mercado lo acepte ni de que la organización pueda entregarlo. Etiquetar por separado objetivo, valor requerido, dato observado, hipótesis y recomendación. Una recomendación cuantitativa exige fundamento independiente suficiente para el uso, además de coherencia aritmética.

## Identidad de artefactos

Las fuentes de trabajo usan `ID - Go2Rev - Titulo - vN.ext` y conservan en cabecera versión del paquete, ámbito, autor, estado y receptor. Una vista externa puede adaptar el título al cliente, pero el índice y la fuente editable mantienen la identidad metodológica. El estado documental no acredita validez del contenido ni aceptación de una decisión.

## Detección y retirada

Son indicios de contaminación: pasos o skills ajenos presentados como Go2Rev; precondiciones externas usadas para decidir; resultados sin nodo/contrato localizable; o cálculos cuya premisa procede solo del objetivo que debían evaluar.

Al detectar uno:

1. Detener los usos que dependan del contenido dudoso y conservar el archivo original.
2. Marcarlo en su primera línea e índice como **RETIRADO**, con fecha, causa, método o premisa incompatible y alcance conocido.
3. Moverlo a `04 Archivo/Retirados`, preservando identidad y versión; no sobrescribirlo con una corrección.
4. Recorrer sus consumidores y disponer cada uno como no afectado, limitado, retirado o por rehacer. Registrar CAM cuando una decisión o contenido vigente deba cambiar.
5. Recuperar las fuentes válidas y rehacer únicamente los campos afectados con el productor Go2Rev pertinente.
6. Cerrar la incidencia cuando los usos dependientes estén conciliados y el índice apunte a las versiones vigentes.

La retirada evita que un resultado incompatible vuelva a consumirse; no borra la evidencia de lo ocurrido ni convierte el trabajo rehecho en validación del método.
