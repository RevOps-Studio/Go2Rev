# Procedencia y correspondencia de FND05

Versión 0.1 · Lectura por capacidad · 11 de septiembre de 2026

## Fuentes vigentes y alcance

Este componente desarrolla N07/N09/N10 de la [arquitectura aceptada](../../../producto/arquitectura/v0.2/03_nodos_y_entregables.md). Utiliza el [diccionario FND02](../../../producto/metodo/encargo_y_conocimiento/v0.1/03_contratos_y_diccionario.md), los [contratos exploratorios de Diagnostic](../../../producto/metodo/investigacion_y_diagnostic/v0.2/06_contratos_y_economia_exploratoria.md), el [contraste externo/interno](../../../producto/metodo/investigacion_y_diagnostic/v0.2/08_investigacion_externa_y_contraste.md), la [rutina de fuentes/acceso](../../../producto/metodo/investigacion_y_diagnostic/v0.2/09_rutina_de_fuentes_y_acceso.md) y los [contratos de oferta, entrega y economía](../../../producto/metodo/oferta_entrega_y_economia/v0.1/07_contratos_y_revision.md). La elaboración completa esas interfaces con instrucciones, relaciones generales y seis plantillas vacías.

La [correspondencia de arquitectura](../../arquitectura/05_reutilizacion_y_fuentes.md) conserva la comprobación física y los faltantes. Se consulta solo el original pertinente; no se repite la recuperación por sesión. Los documentos históricos son procedencia, no instrucciones de ejecución ni dependencias de la futura operación.

Raíz del consolidado: `Back to the plan/fuentes/Go2Rev_snapshot_migracion_v0.2_2026-09-10/`.

**G** = `workspace/outputs/work01-20260910/metodo/` dentro de esa raíz.

**R** = `referencia_corte_v0.1/Go2Rev_snapshot_pre_migracion_v0.1_2026-09-10/20_referencias/RevOS_4.4.0/fuente/`.

**T** = mismo prefijo de referencias, bajo `GTM_Planner_0.3.0/fuente/`. La procedencia local conservada corresponde al commit `c03068ce187d264caa6f5e9fc172d46907ccbcca`; no se atribuye una nueva comprobación remota.

## Lectura ampliada para FND05

Las franjas de lectura de los cuatro archivos RevOS siguientes comprenden las secciones sustantivas indicadas; se omite la convención transversal repetida. Solo se reutilizan los apartados de plantilla expresamente identificados, sin atribuir lectura integral de las plantillas.

| Original y lectura efectiva | Conservar / adaptar | Completar / retirar en Go2Rev |
|---|---|---|
| R `skills/growth-system-design/SKILL.md`: propósito, posición, principios y proceso, líneas 13–69; plantilla §5 por mecanismo, líneas 124–137 | Mecanismo de generación de demanda conectado con entradas, salidas, capacidades, riesgo y resto del sistema | Completar identidad, acceso efectivo, actividad de intentos sin resultado y economía. Retirar cuotas de mecanismos/candidatos, horizontes fijos y promesa de predictibilidad como condición presumida |
| R `skills/channel-strategy-design/SKILL.md`: propósito, posición, principios y proceso, líneas 13–71; plantilla §5 por canal, líneas 124–138 | Función de canal, coherencia con posición, restricciones, coste y secuencia según requisitos | Completar comparabilidad de referencias, incertidumbre, permisos y capacidad. Retirar número obligatorio de canales, pesos genéricos, calendario universal y precedencia orgánico/pago impuesta |
| R `skills/sales-conversion-design/SKILL.md`: propósito, posición, principios y proceso, líneas 13–71; plantilla §4–§7, líneas 130–188 | Ajuste frente a intención, condición verificable, asignación, compromiso de respuesta, devolución y retroalimentación | Completar desconocido distinto de incumplimiento, capacidad temporal, receptor efectivo y retorno sin duplicar adquisición. Retirar etapas/departamentos predeterminados, horas universales y automatización obligatoria |
| R `skills/sales-process-design/SKILL.md`: propósito, posición, principios y proceso, líneas 13–74; plantilla §4–§6, líneas 124–184 | Compra como secuencia de decisiones, trabajo por etapa, evidencia, cadencia con propósito y cierre | Completar ramas, oferta aceptada, pedido/inicio/caja separados, versiones y carga íntegra. Retirar número obligatorio de etapas, marcos de cualificación impuestos, probabilidades por etiqueta y previsión obligatoria |
| T `skills/demand-plan/SKILL.md`, completo | Hipótesis de mecanismo, función de canal, requisitos operativos y secuencia de desarrollo | Adaptar al ámbito K09 y al intercambio E. Retirar cuotas, periodo fijo de primera señal, dependencia de herramientas nominadas, despacho de agentes y confirmación por fase; no son requisitos Go2Rev |
| T `skills/demand-plan/references/engine-catalog.md`, completo | Familias de mecanismo como alternativas con requisitos y relaciones causales | Reconstruir un catálogo general de opciones para N09, sin heredar costes, tiempos, sectores, prioridades o velocidades universales |
| T `skills/demand-plan/references/channel-functions.md`, completo | Separar canal y función dentro del recorrido | Completar origen, exposición/contacto, respuesta, recepción y compra con unidad y condición propias; retirar una taxonomía o mezcla obligatorias |
| T `skills/demand-plan/references/benchmark-rules.md`, completo | Fuente visible, límites del benchmark y tratamiento de incertidumbre | Exigir definición, población, periodo, método y comparabilidad. Retirar prioridad automática del dato propio y rango deliberadamente amplio como sustituto de evidencia ausente |
| T `skills/positioning/references/pillar-test.md`, completo | Relevancia, contraste y fundamento de una razón; afirmación no acreditada conserva incertidumbre | Separar requisito básico de diferenciador y de preferencia demostrada. Retirar cuota de pilares y obligación de que toda razón de confianza sea exclusiva |
| T `skills/positioning/references/anti-messages.md`, completo | Examinar promesas vacías, lenguaje confuso y afirmaciones sin capacidad o evidencia | Reformular, condicionar o retirar según uso y fundamento. Retirar prohibición automática de lenguaje compartido, superioridad presumida y clasificación obligatoria de objeciones al mensaje |

## Lecturas pertinentes conservadas de FND04

La [correspondencia FND04](../oferta_entrega_y_economia/09_fuentes_y_correspondencia.md) documenta estas lecturas previas. Se conserva su alcance sin presentarlas como una nueva lectura integral ni volver a cargar contenido histórico de aplicación.

| Original y cobertura conservada | Conservar / adaptar | Completar / retirar en FND05 |
|---|---|---|
| G `G1_oferta_basada_en_evidencia_v0.2.md`: instrucciones 1–8, criterios y formato | Promesa trazable, relación comprador/oferta/acceso y coste de intentos sin venta | Distribuir posicionamiento N07 y demanda N09 sin perder vínculo con K08. Completar decisiones de marco, mensajes, mecanismos, cohortes y contratos; retirar requisitos históricos de aplicación |
| G `G3_recorrido_y_responsabilidades_v0.1.md`: instrucciones 1–9, criterios y formato | Condición/acción/evidencia, ejecutor/autoridad/receptor, traspaso y hechos preservados ante cambios | Desarrollar N10 con trabajo sin avance, devolución, recepción y variantes; mantener K11 como contrato único de inicio/cumplimiento. Retirar ejecución durante la construcción |
| R `skills/positioning-messaging/SKILL.md`: propósito, posición, principios y proceso, líneas 14–75; no plantilla completa | Marco de compra, alternativas, expectativas y capacidades que sostienen promesas | Adaptar a compromiso controlable, comparación razonada y suficiencia por uso. Retirar cuotas, confianza por procedencia y aprobación como evidencia |
| T `skills/positioning/SKILL.md`: propósito, principios y proceso, líneas 14–81 | Mercado, capacidades y decisión de categoría como fundamentos | Completar mensajes por decisión/rol, fundamento de cada afirmación, condiciones y revisión del consumidor; no heredar gobierno ni plantilla completa no leída |
| T `skills/positioning/references/category-decision.md`, completo | Comparar marcos desde comprador, alternativas, capacidades e implicaciones | Completar coste de comprensión y efectos sobre demanda/conversión. Retirar cuota de categorías y puntuación como prueba de adecuación; elegir marco no acredita poder de precio |

La economía de FND05 se apoya en las fórmulas y contratos actuales de FND04. Las definiciones de cohortes, unidades, seguimiento incompleto, atribución, carga por recurso, conciliación de costes y variantes de compra aquí desarrolladas son elaboración metodológica de Go2Rev. No se atribuyen a una calculadora original ni a binarios o motores no inspeccionados. Esos originales mantienen su límite de reutilización; no se reconstruyen desde resúmenes.

## Correspondencia con lo construido

| Capacidad final | Resolución |
|---|---|
| Marco de compra y promesa defendible | 01 y plantillas 01/02: alternativas, expectativas, capacidad, fundamento, argumento contrario y recomendación |
| Investigación que cambia el diseño | 01/02/06: AF interna/externa, comparabilidad, conclusión derivada y consumidor; hallazgos externos pueden ampliar las opciones |
| Acceso y compra exploratorios para Diagnostic | 02/03/06: K09/K10 E sin K06 final ni K07 adoptado; misma combinación que K08/K11/K12 |
| Demanda conectada con trabajo real | 02/04 y plantillas 03/05: mecanismo, acceso, permisos, población, señal, recepción y coste completo |
| Conversión con decisiones verificables | 03 y plantillas 04/06: ajuste/intención, evidencia, autoridad, respuesta, devolución, cierre y recepción |
| Economía compatible con la población | 04 y plantilla 05: objetos/cohortes, madurez, denominadores, carga, partida única y dominio de representación K12 |
| Variantes de compra y oferta | 05: directa, intermediada y autoservicio; producto físico, servicio y recurrencia; sin equiparar acuerdo de canal y venta final |
| Preparación y continuidad posteriores | 06: campos concretos para N13–N17, permisos por acción, suficiencia por uso y CAM por dependencia efectiva |

La revisión de construcción examina cobertura, razonamiento, interfaces, dimensionalidad de las relaciones, integridad de enlaces, estructura de tablas y campos vacíos. No se ejecutan mensajes, campañas, recorridos de compra ni pruebas del método. El resultado y el trabajo pendiente se mantienen en Evidencias y Plan, respectivamente; este archivo es correspondencia del producto.
