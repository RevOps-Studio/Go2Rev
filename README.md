# Go2Rev

Metodología fundacional B2B para diseñar una salida al mercado y preparar su operación: Diagnostic, Design y Despliegue. Contempla una oferta existente en un contexto nuevo y una nueva iniciativa, con operación por conversación e independencia del proveedor de LLM.

La base fundacional v0.1 se cerró documentalmente el 11 de septiembre de 2026. Conserva su estado teórico: no ha habido clientes ni pruebas de la metodología. El cierre de construcción no inicia la captación, la validación comercial ni una prestación.

## Empezar

- [Paquete fundacional y guía de implementación](producto/paquete_fundacional/v0.1/LEEME.md).
- [Entrada conversacional del método](producto/metodo/operacion_conversacional/v0.1/ENTRADA_GO2REV.md).
- [Distribución completa en ZIP](entregables/Go2Rev_fundacional_v0.1.zip) y [suma SHA-256](entregables/Go2Rev_fundacional_v0.1.sha256).
- [Continuidad del desarrollo y tres maestros vigentes](LEEME_CONTINUIDAD.md).

## Contenido del repositorio

`producto/` contiene las fuentes metodológicas vigentes, diecisiete nodos, contratos, treinta y seis plantillas vacías, un modelo económico editable y las vistas de lectura. `herramientas/` contiene los generadores y sus instrucciones. `entregables/` conserva la distribución identificada del conjunto fundacional.

Los tres maestros mantienen sus funciones: Plan para tareas y estado; Producto para definición y arquitectura; Evidencias para decisiones, procedencia y revisión documental. Este archivo es únicamente una entrada al repositorio.

## Conservación y reproducción

Las correcciones se realizan primero en las fuentes de `producto/`. Las [herramientas de documentación](herramientas/documentos/LEEME.md), del [modelo económico](herramientas/modelo_economico/LEEME.md) y del [paquete](herramientas/paquete/LEEME.md) describen cómo generar sus derivados y qué dependencias requieren. Esas dependencias no se incluyen en Git.

El archivo local `Back to the plan/`, las versiones sustituidas que contiene y las salidas temporales de revisión quedan fuera de este repositorio. Las correspondencias metodológicas conservan la procedencia de esos originales; su texto íntegro no está incluido en esta copia de GitHub. El producto operativo no necesita cargar ese archivo histórico.

La configuración de Git conserva los bytes de los archivos para mantener la correspondencia con el manifiesto SHA-256 del paquete.

## Mejoras y versiones estables

`main` conserva la base estable. Cada mejora se desarrolla en una rama propia, con avances guardados en commits y subidos a GitHub. La misma rama se mantiene durante las sesiones necesarias para completar esa mejora.

Los cambios se presentan mediante una solicitud de integración (pull request), con su alcance, revisión y límites. Se incorporan a `main` tras la revisión y autorización de Carlos. Las reglas de continuidad del trabajo están en [AGENTS.md](AGENTS.md).

La etiqueta `base-fundacional-v0.1` identifica la versión inicial del repositorio. Permite recuperar sus archivos sin depender del estado posterior de una rama. Si hay que deshacer una integración, se conserva el historial mediante un commit de reversión. Los archivos excluidos de Git, como el archivo histórico local, requieren su propia conservación.
