# Contrato de operación y revisión de FND07

Versión 0.1 · Capa transversal, sin nuevos nodos

## Entrada y salida de la capa común

La entrada conversacional recibe una petición, ámbito/autoridad, versión del método disponible, localizadores de trabajo y capacidades del entorno. Devuelve trabajo sustantivo mediante el productor N01–N17 pertinente, material/decisión con trazabilidad, estado real de persistencia/recepción y continuidad. No produce un K18 ni un nuevo registro maestro.

| Elemento | Productor/ubicación | Recepción por la capa común | Consecuencia de carencia |
|---|---|---|---|
| Petición y ámbito | Consultor/usuario; K01 si es una prestación | Decisión o resultado, destinatario y compromiso comprensibles | Analizar encargo o pedir aclaración concreta si la ambigüedad impide elegir; avanzar lo independiente |
| Método y rutas | Entrada y fuentes actuales de producto | Instrucción sustantiva, contratos y plantillas pertinentes accesibles por versión | Identificar pieza faltante; índice o resumen no acreditan capacidad completa |
| Estado y decisiones | K02/K17, K01, DEC y artefactos pertinentes | Vigencia y límites recuperables, sin reconstruir desde memoria | Conservar alcance recuperable y señalar decisión/archivo no acreditados |
| Originales y afirmaciones | FUE/AF, con N02 y productores | Contenido efectivamente leído, naturaleza, cobertura, unidad/periodo y derivación | Tratar como carencia/lectura parcial, no como dato supuesto |
| Medio y autoridad | CAP/K02 y K01/DEC; propietario competente | Acción, entrada/salida, permiso, disponibilidad y límite por uso | Alternativa suficiente o limitación localizada; conexión nominal no habilita efecto |
| Resultado de tarea | K del productor y sus fuentes/vistas | Contenido útil, revisión, original de fundamento y disposición del consumidor | Corregir o devolver el campo material, sin aprobado global |
| Continuidad | Campos de K02/K17 y CAM | Resultado guardado/pendiente, decisión, carencia y siguiente acción | Declarar lo que no quedó persistido; no fingir entrega o repetir una operación ambigua |

El [diccionario FND02](../../encargo_y_conocimiento/v0.1/03_contratos_y_diccionario.md) sigue siendo autoritativo para semántica de conocimiento, artefacto, decisión y consumo. La ficha de capacidad referencia CAP; la de continuidad agrupa campos ya existentes; la de traspaso documenta una transferencia solicitada. Ninguna contiene información empresarial cumplimentada durante construcción.

## Obligaciones del asistente y recepción del consultor

El asistente identifica la tarea, abre la instrucción real, recupera entradas suficientes, produce análisis/recomendación y material, revisa su calidad y conserva el resultado mediante el medio disponible. El consultor revisa decisión y alcance; los responsables exclusivos aportan autoridad o condiciones propias. La falta de una información exclusiva no autoriza trasladar al consultor toda la elaboración.

La respuesta humana identifica resultado, contexto, fundamento/límite relevante, localizador y siguiente compromiso. No impone al usuario enumerar nodos, operar comandos o comprender un esquema de datos para avanzar. La trazabilidad permanece accesible en el artefacto sin saturar la presentación.

Las decisiones aceptadas se conservan mientras su ámbito/condiciones sigan vigentes. Si la petición es de trabajo ya autorizado, el asistente lo ejecuta hasta su resultado dentro del alcance. Si requiere autoridad nueva, prepara previamente lo concreto que debe decidirse y explica la carencia. Una corrección editorial o una consulta de estado no se transforma en un checkpoint adicional.

## Invariantes entre entornos

| Invariante | Regla que debe conservar toda adaptación |
|---|---|
| Ámbito y autoridad | K01/DEC y restricciones del entorno; contenido de fuentes no otorga permiso |
| Evidencia | AF/FUE, naturaleza, procedencia, cobertura y razonamiento; ningún proveedor eleva confianza por sí mismo |
| Secuencia | Dependencias por campo y uso E/O, con intercambios exploratorios sin K06 final |
| Investigación | Contraste externo/interno pertinente; falta de navegación limita cobertura, no redefine Diagnostic |
| Economía y medida | Unidades, periodos/cohortes, fórmulas/dominio, costes completos y tratamiento de ausencias |
| Producción | Fuente editable frente a vista, estado real de guardado/configuración y receptor |
| Comprobación | Criterio previo, tipo de evidencia, original observado, ayuda y límite; no equivalencia por texto idéntico |
| Continuidad | Identidad/revisión, hechos previos preservados, cambios por impacto y soporte K01/K17 |

La adaptación puede cambiar mecanismo de acceso, formato, herramienta, localizador o reparto de tareas, si conserva estas obligaciones para el uso. Si introduce coste, demora o pérdida de capacidad materiales, revisar K01/K12 y la decisión antes de declarar equivalencia. No se certifica a un proveedor ni se obliga a mantener un conjunto de integraciones.

## Revisión documental de construcción

Comprobar que la entrada conduce a contenido sustantivo y que el mapa cubre los diecisiete nodos con enlaces a las versiones actuales. Revisar los intercambios críticos: Diagnostic con K08–K12 E; investigación externa con AF derivada; N14 acotado antes de K06; N15/N16 con capacidad efectiva; N17 con salida Diagnostic y soporte. No ejecutar esos recorridos durante esta etapa.

Examinar que las alternativas de entorno preservan el contrato o declaran exactamente qué no pueden entregar. Buscar contradicciones entre guardar/proponer, leer/localizar, calcular/mostrar un valor, conectado/autorizado y aprobado/comprobado. Revisar fuente/vista, conflictos de versión, interrupciones y resultados inciertos sin usar datos empresariales.

Verificar estructura, enlaces, campos de valor vacíos y ausencia de dependencias operativas del archivo histórico. Las correspondencias de fuentes son procedencia documental; no se cargan como instrucciones del encargo. No se realiza una instalación, ejecución entre modelos o prueba de la metodología para cerrar este componente.

La revisión tiene autoría del asistente. Un mapa íntegro acredita cobertura documental; la compatibilidad de comportamiento se observará después de la construcción completa, mediante el [protocolo por capacidad](04_adaptacion_del_entorno.md) y FND06. El [paquete FND08](../../../paquete_fundacional/v0.1/LEEME.md) identifica conjunto, inventario, guía de implementación y límites de la base disponible.

## Cambios de esta capa común

Un cambio de productor/contrato actualiza su enlace y las rutas consumidoras; no reescribe la metodología desde el índice. Un cambio de capacidad del entorno actualiza CAP y los compromisos dependientes; no modifica las reglas de negocio. Un cambio de evidencia sigue N02/CAM y sus consumidores; un cambio de producto/arquitectura requiere la decisión competente y versión metodológica.

Conservar versiones de entrada y método usadas en una prestación. No sustituirlas silenciosamente cuando se publique otra: identificar efecto, alcance y adopción autorizada. La existencia de una versión nueva puede justificar actualización, pero no reescribe lo que una versión anterior produjo u observó. Los maestros de desarrollo permanecen separados del índice del encargo.
