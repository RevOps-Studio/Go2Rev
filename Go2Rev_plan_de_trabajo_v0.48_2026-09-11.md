# Go2Rev Plan de trabajo v0.48

11 de septiembre de 2026 · Responsable de producto Carlos Estrada

[Producto v0.37](Go2Rev_producto_y_metodo_v0.37_2026-09-11.md) · [Evidencias v0.44](Go2Rev_evidencias_y_pruebas_v0.44_2026-09-11.md)

## Objetivo y estado

La primera metodología Go2Rev queda construida e integrada como [paquete fundacional v0.1](producto/paquete_fundacional/v0.1/LEEME.md), listo para iniciar una implementación en su alcance declarado. El cierre del 11 de septiembre es documental y corresponde al asistente; no atribuye revisión o aceptación adicional de Carlos. La base sigue enteramente teórica: no ha habido clientes ni pruebas de la metodología.

La [arquitectura v0.2](producto/arquitectura/v0.2/01_arquitectura_metodologica.md) define diecisiete nodos, contratos, fuentes, dependencias, calidad y gobierno. Los componentes [encargo y conocimiento v0.1](producto/metodo/encargo_y_conocimiento/v0.1/LEEME.md) e [investigación y Diagnostic v0.2](producto/metodo/investigacion_y_diagnostic/v0.2/LEEME.md) desarrollan N01–N06 con instrucciones, contratos y plantillas vacías. [Oferta, entrega y economía v0.1](producto/metodo/oferta_entrega_y_economia/v0.1/LEEME.md) desarrolla N08/N11/N12 con fórmulas generales, seis plantillas vacías y modelo editable. [Posicionamiento, demanda y conversión v0.1](producto/metodo/posicionamiento_demanda_y_conversion/v0.1/LEEME.md) desarrolla N07/N09/N10, incluidas entradas exploratorias para Diagnostic, con instrucciones, contratos y seis plantillas vacías. [Medición, preparación y transferencia v0.1](producto/metodo/medicion_preparacion_y_transferencia/v0.1/LEEME.md) desarrolla N13–N17 con instrucciones, protocolos de futura prestación, contratos y ocho plantillas vacías. [Operación conversacional v0.1](producto/metodo/operacion_conversacional/v0.1/LEEME.md) integra entrada, guía del consultor, rutas N01–N17, capacidades y continuidad. FND08 completa guía de implementación, alcance/variantes, composición de entregas, cobertura, versiones e inventario; la distribución local fija el conjunto completo y sus límites.

El backlog fundacional está cerrado. La captación y la validación comercial siguen diferidas. Las pruebas podrán comenzar después de este cierre, incluida la primera implementación autorizada; este trabajo no las inicia ni crea registros de prestación.

## Secuencia de desarrollo

1. **Construcción fundacional completa.** Desarrollar capacidades, instrucciones, plantillas, modelos generales, protocolos y guías de todos los componentes comprometidos; integrar dependencias y revisar la documentación.
2. **Versión fundacional cerrada.** Publicar una versión identificable con alcance, archivos completos, instrucciones de uso, requisitos de entrada y límites. Este cierre es de construcción; conserva el estado teórico.
3. **Prueba e implementación después de la construcción.** Solo se podrá abrir esta etapa tras el cierre anterior. La prueba podrá realizarse en la primera implementación autorizada; no se impone una actividad intermedia para poder construir o entregar la base. Su información permanecerá separada de las fuentes metodológicas.
4. **Aprendizaje posterior.** Gestionar las mejoras justificadas por la aplicación de la versión terminada, preservando la base general del producto.

La construcción del producto y las fases Diagnostic, Design y Despliegue de una futura prestación son ámbitos distintos. Los procedimientos de investigación, pruebas y uso con operador se redactan ahora como parte del método; no se ejecutan ahora para completar el desarrollo.

## Backlog de construcción

Cada fila se cierra por contenido e integración del entregable indicado. El orden responde a sus dependencias de construcción.

| ID | Componente final que se construye | Dependencia | Estado y condición de cierre |
|---|---|---|---|
| FND01 | Arquitectura, límites de producto y regla de construcción fundacional | Decisiones de producto | Cerrado en v0.2 como base de construcción aceptada |
| FND02 | Contrato de encargo y salida; solicitud selectiva; registro de fuentes, afirmaciones y decisiones; transferencia A y capacidades B | FND01 | Cerrado documentalmente en v0.1 el 11 de septiembre. Instrucciones N01/N02, contratos K01/K02, seis plantillas vacías y guía local; integrado con arquitectura y consumidores |
| FND03 | Investigación externa, comprador, alternativas, tendencias y cruce con el cliente; recomendación Diagnostic y rutina de fuentes/acceso | FND02; coordinación con FND04 | Revisado y completado documentalmente en v0.2. N03–N06, contraste externo/interno exigible, sugerencia de fuentes y acceso/MCP, contratos y siete plantillas vacías; N08/N11/N12 E construidos en FND04 y N09/N10 E construidos en FND05; protocolos de futura actuación construidos en FND06 |
| FND04 | Oferta y precio, entrega y cobro, economía y capacidad | FND02; contrato exploratorio de FND03 | Cerrado documentalmente en v0.1 el 11 de septiembre. N08/N11/N12 y sus representaciones E; instrucciones, fórmulas y dominio, variantes, seis plantillas vacías y libro editable de seis hojas; revisión documental y límites de cálculo explícitos |
| FND05 | Posicionamiento, demanda y conversión | FND03 y FND04 | Cerrado documentalmente en v0.1 el 11 de septiembre. N07/N09/N10, acceso/compra E sin K06 final ni K07 adoptado; catorce documentos con seis plantillas vacías, variantes directa/intermediada/autoservicio y coste/carga de toda la cohorte compatibles con K12 |
| FND06 | Medición, preparación, materialización, comprobación y transferencia | FND03–FND05 | Cerrado documentalmente en v0.1 el 11 de septiembre. N13–N17, diecisiete archivos y ocho plantillas vacías: medidas/decisiones, preparación por obligación o incertidumbre, protocolos de evidencia/funcionamiento/uso, producción de piezas/medios y transferencia con soporte acotado. Protocolos redactados sin ejecutar |
| FND07 | Entrada conversacional e instrucciones por capacidades del entorno | FND02–FND06 | Cerrado documentalmente en v0.1 el 11 de septiembre. Doce archivos: entrada reutilizable, guía del consultor, mapa de diecisiete nodos, capacidades/alternativas, adaptación, continuidad/cambios, contratos/fuentes y tres plantillas vacías. Reglas comunes entre proveedores y protocolo posterior por capacidad; sin instalación ni pruebas ejecutadas |
| FND08 | Paquete fundacional completo y guía de implementación | FND02–FND07 | Cerrado documentalmente el 11 de septiembre en conjunto v0.1. Guía, alcance/variantes, composición de cinco entregas, cobertura N01–N17, versiones, inventario/manifiesto y distribución local de 114 archivos. Conserva 36 plantillas vacías y modelo editable. Revisadas integración e integridad y las vistas Word; pruebas del método sin ejecutar |

El [contrato exploratorio de FND03](producto/metodo/investigacion_y_diagnostic/v0.2/06_contratos_y_economia_exploratoria.md) especifica qué consumirá Diagnostic de N08–N12. FND04 ha construido los productores de oferta, entrega y economía; FND05 completa acceso y compra, con población, trabajo de todos los intentos y costes conciliados con K12. Las versiones E permiten esa producción antes de K06 final y sin posicionamiento adoptado. FND06 desarrolla los consumidores N13–N17 y sus protocolos de futura prestación, incluida obtención acotada antes de K06 final. FND07 integra entrada global, capacidades del entorno y continuidad por tarea. FND08 completa el paquete, la guía y la revisión integrada del alcance. La [cobertura del conjunto](producto/paquete_fundacional/v0.1/04_cobertura_e_integracion.md) enlaza productores y contratos; el [alcance publicado](producto/paquete_fundacional/v0.1/02_alcance_y_variantes.md) distingue desarrollo metodológico, automatización del libro y requisitos de prestación. Las familias y componentes se especifican en [construcción del producto](producto/arquitectura/v0.2/06_construccion_y_revision.md); el estado y la siguiente tarea se mantienen únicamente en este Plan.

## Criterio aplicado al cierre de construcción

- Todos los nodos N01–N17 tienen instrucciones que explican análisis, entradas, salidas, consumidores, alternativas ante carencias y criterios de decisión.
- Las plantillas contienen campos definidos, reglas y guías. Los campos empresariales permanecen vacíos hasta una prestación.
- Los modelos económicos contienen fórmulas generales, unidades, dominios y tratamiento explícito de ausencias; ninguna cifra de una empresa condiciona su construcción.
- Las dependencias y versiones exploratorias están resueltas en los contratos. Consultor, patrocinador y operador tienen límites claros de decisión.
- Los protocolos de comprobación de una futura prestación están redactados y enlazados con sus capacidades. Su ejecución permanece posterior al cierre de construcción.
- La entrada conversacional, guía del consultor, paquete editable e instrucciones de continuidad están completos. El alcance declarado puede prestarse sin recuperar instrucciones externas al producto.
- La revisión documental ha corregido omisiones, incoherencias, fórmulas inconsistentes, referencias rotas y problemas de legibilidad. Existe un inventario de componentes y versión.

Listo para implementar significa que el producto necesario para comenzar una prestación está construido. No implica aplicación previa, demanda acreditada o validación de resultados comerciales. Una pieza esencial pendiente impide declarar listo ese alcance.

## Forma de trabajo

Carlos dedica 4–5 horas semanales a decisiones de producto y arquitectura. El asistente produce análisis, instrucciones, formatos y demás componentes. Los detalles que no cambian el alcance aceptado se resuelven durante la construcción.

La revisión de construcción examina los propios entregables: cobertura, razonamiento, interfaces, fórmulas, archivos y presentación. No requiere ejecutar un recorrido de negocio. Los controles técnicos de edición y legibilidad no se presentan como prueba de la metodología.

Una nueva necesidad entra en el backlog solo si señala una carencia del entregable final, su consecuencia y la pieza afectada. Las decisiones comerciales sobre precio, duración, sectores o países se abordarán cuando corresponda comprometer una oferta; no se convierten en campañas actuales ni bloquean el diseño general.

## Continuidad después del cierre

FND01–FND08 están cerrados en el alcance identificado por la versión del conjunto. La [distribución local](entregables/Go2Rev_fundacional_v0.1.zip) contiene fuentes editables, vistas, modelo, instrucciones y herramientas documentales opcionales. No incluye los maestros de desarrollo ni el archivo histórico. Las correcciones editoriales de integración conservan versiones anteriores y su procedencia.

Carlos puede revisar decisiones de producto y arquitectura desde el paquete. Una observación que señale una carencia concreta reabre la pieza afectada y sus dependencias en este Plan; no crea otro maestro ni convierte automáticamente el cierre en validación. La siguiente actividad de aplicación requerirá su ámbito autorizado y utilizará las instrucciones de implementación ya construidas. No se exige un ejercicio previo, campaña o investigación comercial para disponer de la base.

Esta versión sustituye la v0.47 e incorpora el cierre documental de FND08 y del conjunto fundacional v0.1. Las pruebas de método, comportamiento entre proveedores, cálculo con parámetros y uso con operador siguen sin ejecutar; captación y validación comercial permanecen diferidas. El cierre no inicia ninguna de esas actividades.
