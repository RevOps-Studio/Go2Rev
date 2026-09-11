# Encargo y conocimiento

Versión 0.1 · 11 de septiembre de 2026 · Componente fundacional FND02

Este componente desarrolla N01 y N02 de la arquitectura aceptada. Contiene instrucciones de prestación y plantillas generales con campos vacíos. Su construcción no supone ejecutar la metodología ni iniciar una prestación. El conjunto disponible y su guía se identifican en el [paquete fundacional](../../../paquete_fundacional/v0.1/LEEME.md).

## Finalidad y alcance

Delimitar una iniciativa y el compromiso que puede asumirse; prever la salida de Diagnostic antes de contratar; convertir los materiales disponibles en conocimiento trazable; obtener selectivamente lo que falta; y entregar entradas utilizables a investigación, diseño y continuidad.

Aplica al foco B2B y a ambos recorridos: A, oferta existente en contexto nuevo; B, nueva iniciativa. La representación de una oferta permite comenzar una evaluación aunque el mercado o segmento prioritario todavía deban decidirse. El historial comercial y las herramientas conectadas son entradas condicionales.

## Lectura por tarea

| Tarea durante una futura prestación | Instrucción | Formato de salida |
|---|---|---|
| Delimitar o revisar iniciativa, alcance, entrega y salida | [Encuadre y salida](01_encargo_y_salida.md) | [Encargo K01](plantillas/01_encargo.md) |
| Incorporar materiales, analizar conocimiento y seleccionar peticiones | [Conocimiento y solicitud](02_conocimiento_y_solicitud.md) | [Solicitudes](plantillas/02_solicitudes.md) y [conocimiento K02](plantillas/03_conocimiento.md) |
| Examinar transferencia desde un contexto de origen | Apartado A de conocimiento | [Transferencia A](plantillas/04_transferencia_A.md) |
| Examinar capacidades de una nueva iniciativa | Apartado B de conocimiento | [Capacidades B](plantillas/05_capacidades_B.md) |
| Registrar decisión, aceptación de entrada o cambio material | [Contratos y diccionario](03_contratos_y_diccionario.md) | [Decisiones y cambios](plantillas/06_decisiones_y_cambios.md) |
| Revisar procedencia del componente | [Fuentes y correspondencia](04_fuentes_y_correspondencia.md) | Registro de diseño; no requiere lectura durante la prestación |

Las plantillas son secciones reutilizables, no seis entregables obligatorios. Pueden reunirse en un archivo de prestación con un índice. K01 y K02 identifican objetos lógicos; sus secciones conservan referencias estables cuando comparten soporte. La base metodológica se mantiene separada de cualquier información que se incorpore durante una prestación.

## Entrada por conversación

El consultor expresa qué necesita decidir o qué material acaba de recibir. El asistente identifica la tarea de la tabla, recupera el alcance y las entradas pertinentes, y comunica qué analizará y qué salida actualizará. Los identificadores sirven para conservar trazabilidad; la persona no necesita pronunciarlos ni aprender comandos.

Antes de pedir información, el asistente lee lo disponible y distingue lo extraíble, lo que debe investigar y lo que solo puede aclarar su responsable. Devuelve una propuesta razonada, el límite del conocimiento disponible y la siguiente acción permitida. Una decisión ya documentada no se solicita de nuevo si su alcance y condiciones siguen vigentes.

Al reanudar se leen únicamente el índice actual de la prestación, las versiones de K01/K02 necesarias y los originales que sustentan la tarea. Se conserva el trabajo vigente. El cambio de conversación no crea una nueva iniciativa ni reabre por sí mismo decisiones.

## Capacidades del entorno

Se necesita leer texto y tablas con localizadores, redactar y conservar archivos editables. Cuando un original exija extracción especializada, navegación o acceso a un sistema, el asistente declara qué pudo leer y qué falta. Puede trabajar con una exportación íntegra accesible o limitar la afirmación afectada. Una ruta, una URL o un acceso mencionado no acreditan lectura.

La lógica de análisis es común entre proveedores de LLM y utilizable por el consultor sin LLM. Las instrucciones no requieren una plataforma propia, un conector, RevOS ni GTM Planner. La [entrada conversacional y las guías de entorno](../../operacion_conversacional/v0.1/LEEME.md) integran estos contratos con los demás componentes.

## Recepción documental del componente

La revisión de construcción comprueba que los procedimientos explican el análisis, que cada campo tiene significado y productor, que K01/K02 tienen consumidores y límites, y que las plantillas permanecen vacías. La integridad de enlaces y la legibilidad son parte de esa revisión. La prueba de la metodología se realizará después de completar su construcción íntegra.
