# Reutilización y procedencia

Versión 0.2 · Lectura por capacidad y tarea · Fundamento de construcción y alcance de reutilización

## Estado físico y vigencia

El ZIP consolidado se ha desplegado bajo `Back to the plan/fuentes/Go2Rev_snapshot_migracion_v0.2_2026-09-10`. Los 629 archivos de su manifiesto coinciden en SHA256; ese total incluye referencias y otras copias, no solo los 433 archivos de workspace declarados por la exportación.

Los maestros acreditados son Plan v0.38, Producto v0.27 y Evidencias v0.34. No hay versión posterior de esas tres familias en el workspace exportado inspeccionado. La primera continuación de arquitectura produjo Plan v0.40, Producto v0.29 y Evidencias v0.36, conservados como versiones sustituidas; estos números son procedencia, no selección vigente. Los originales exportados permanecen inalterados.

RevOS declara versión 4.4.0 en `.claude-plugin/plugin.json`; sus 62 archivos de `fuente/` coinciden byte a byte con las entradas del ZIP `original/RevOS-main (5).zip`. El árbol GTM Planner declara 0.3.0; los 45 archivos coinciden con los hashes Git de `procedencia.json`, asociado al commit `c03068ce187d264caa6f5e9fc172d46907ccbcca`. Se verifica la procedencia conservada localmente; no se ha vuelto a consultar el remoto como comprobación independiente del commit.

Las tres semillas existen; `Investigacion GTR - Seed proyecto.md` y `GoToMarket oportnidad españa.md` tienen el mismo SHA256 `ff9ed280b5aca59378f6673faf040d14a642ddb1dfaf20237fcd41151c659171`. Se han leído una sola vez como investigación duplicada, con foco en tesis y recomendaciones. No son dos corroboraciones.

El detalle de integridad se conserva en el archivo de procedencia. Esta comprobación acredita presencia e integridad local, no validez metodológica o de mercado. La construcción utiliza exclusivamente conceptos y reglas metodológicas pertinentes; ninguna referencia convierte una aplicación anterior en componente o evidencia de la primera base.

## Correspondencia con las fuentes de diseño Go2Rev

Conservar significa mantener una regla útil; adaptar, cambiar su alcance o formulación; completar, añadir análisis ausente o insuficientemente especificado; retirar, dejar de usar una regla en la futura implementación. Retirar nunca significa borrar originales o resultados históricos.

| Original metodológico leído | Acción de construcción | Correspondencia y cambio sustantivo |
|---|---|---|
| D0 integrado en entrada v0.7 | Conservar y completar | N01 conserva encuadre/salida; completa contrato del servicio y condiciones de investigación sin exigir segmento decidido |
| D1 integrado y formato v0.1 | Conservar y completar | N02 y 02 separan solicitud, recibido y derivado; añaden población, periodo, unidad, naturaleza, independencia y reconciliación |
| D2 investigación v0.2 | Conservar, adaptar y completar | N03–N05 distribuyen mercado, comprador y alternativas; conservan Q8 de examen de premisas y refutación; desarrollan exploración, profundización y suficiencia por afirmación |
| D3 integrado | Conservar y completar | N06 mantiene las cinco salidas; añade comparación de combinaciones y contrato explícito de economía/acceso exploratorios |
| G1 oferta v0.2 | Conservar, redistribuir y completar | N04/N07/N08/N09 separan comprador, posicionamiento, oferta/precio y demanda; conservan promesa trazable y origen–respuesta–cualificación con coste de intentos fallidos |
| G2 economía v0.2 | Conservar y completar | N12 conserva desconocido distinto de cero, caja/capacidad, escenario diferencial y umbrales; N08 diseña precio y N11 cumplimiento; completar dominio de mezcla/producto/canal cuando se implemente |
| G3 recorrido v0.1 | Conservar y ampliar | N10/N11 separan compra y cumplimiento; conservan transición, autoridad, receptor y cambio de premisa; adaptan ruta a canal/autoservicio y posventa pertinente |
| G4 pruebas v0.1 | Conservar y adaptar | N13/N14 incorporan medición y secuencia. Retirar como límite general que toda construcción deba nacer de una prueba: también se construye por obligación de la promesa contratada |
| P1 materiales v0.2 | Conservar y adaptar | N15 conserva contenido utilizable, configuración real y M0 de presentación; adapta selección de piezas a cada recorrido, sin guion/propuesta obligatorios |
| P1 paquete v0.1 | Conservar en su uso | N15/N17 conservan selección, integridad y procedencia al transferir archivos; no se convierte en procedimiento rutinario de migración de sesión |
| P2 integrado | Conservar y completar | N16 desarrolla protocolos de cobertura por recorrido y tipo de evidencia para una futura prestación; su ejecución no forma parte de la construcción fundacional |
| P3 cierre v0.1 | Conservar y completar | N17 amplía desde evaluación de una salida recibida hacia recepción del servicio, límites de soporte y aprendizaje autorizado |
| Entrada v0.7 | Adaptar conceptos y construir nueva entrada | Conservar operación conversacional y trazabilidad; redactar una entrada autónoma basada en N01–N17, sin depender del original durante la prestación |
| Formato expediente y kit v0.1 | Adaptar y completar | Contratos de 02 y plantillas del método sustituyen corchetes genéricos por significado, productor, uso y suficiencia. Mantener la distinción entre propuesta, aceptación y cobro |

Los once pasos quedan íntegramente relacionados. La correspondencia conserva el razonamiento metodológico de origen. Los diecisiete nodos requieren sus propias instrucciones completas; su aparición en un mapa no equivale a implementación.

## Correspondencia con originales RevOS y GTM Planner

Los identificadores R y T remiten al registro de lectura posterior. Una adaptación conceptual no demuestra equivalencia operativa ni autoriza copiar todo el producto.

| Capacidad de la propuesta | Original pertinente leído | Conservar o adaptar | Completar o retirar para Go2Rev |
|---|---|---|---|
| N01 encargo | R01 orquestador/grafo; G D0 | Alcance, dependencias y separación entre fase/nodo/skill | Salida Diagnostic autónoma y permisos por compromiso. Retirar tiers, modelo obligatorio y aprobación por cada skill |
| N02 conocimiento | R02 intake/brief/knowledge; R01 convenciones; T01 intake/template | Captura separada de interpretación; cruce de fuentes, tensiones y recolección temprana | Ámbito iniciativa/origen/destino. Retirar jerarquía automática por tipo de fuente, CRM de confianza alta por defecto y conversión automática de faltantes en supuestos |
| N03 mercado/acceso | T02 market-map y referencias; G D2 | Preparación de fuentes y alternativas al acceso faltante | Ampliar el mapa competitivo hacia estructura de mercado, compra, entrada y entrega; no equiparar web con disponibilidad garantizada ni requerir una herramienta concreta |
| N04 comprador | R02 plantillas/proceso; R04 sales-process; T01 | Roles, criterios y recorrido de compra | Priorización de segmento por situación, transferencia y posibilidad de servir; no inventar histórico ni aplicar perfil corporativo por defecto |
| N05 alternativas | R03 competitive; T02 tres capas/gap | Directos, sustitutos, trabajo interno y no cambiar; posición relevante y defendible | Retirar máximo de cinco competidores y veto a comparar características cuando sean decisivas. Un espacio aparentemente libre permanece hipótesis si falta evidencia |
| N06 Diagnostic | R03 revenue-diagnostic; R06 checkpoint; G D3/G2 | Tesis causal, prioridades y decisiones explícitas | Pasar de fugas del motor actual a viabilidad de construir una ruta. Permitir ajustar/cerrar conforme a contratación, sin diagnóstico que confirme automáticamente construcción |
| N07 posicionamiento | R04 positioning; T03 category/pillar/anti-messages | Comparación de categorías, razones para creer y control de afirmaciones | Retirar cuotas de pilares, superioridad obligatoria y promesa de resultado que exceda control; mantener diferenciación como hipótesis cuando corresponda |
| N08 oferta/precio | G G1/G2; R04 positioning; T03 | Expectativas de compra y efecto de categoría/precio | Completar unidad, paquetes, condiciones, aceptación de precio y economía. No atribuir una metodología integral de pricing a originales que aquí no la especifican |
| N09 demanda | R04 growth/channels; T04 demand y referencias; G G1 | Mecanismo con inputs/outputs, función de canal, requisitos y secuencia | Retirar 3–5 motores, 3–6 canales, plazos universales, rangos inventados como fallback y superioridad general de orgánico. Añadir coste de cohorte y canal indirecto |
| N10 conversión | R04 sales-conversion/sales-process; G G3 | Encaje/intención, estados, devolución, traspaso y compra vista desde comprador | Retirar etapas, scoring, probabilidades y marcos obligatorios; completar autoservicio e intermediación según necesidad |
| N11 entrega/cobro | G G2/G3 | Condiciones, recepción, capacidad y eventos | Completar cumplimiento y posventa pertinente. RevOS/GTM leídos no se dan por fuentes completas de logística o fiscalidad |
| N12 economía | G G2 v0.2 | Fuente editable, análisis diferencial, caja, contribución y restricciones | Completar alcance de modelos al implementarlos. No reutilizar fórmulas de archivos binarios o scripts que no se han inspeccionado para esta tarea |
| N13 medición | R05 measurement/reporting; T05 execution-readiness | Fórmula, fuente, periodo, responsable y decisión | Incluir medición dentro de Go2Rev; retirar North Star única, métricas de recurrencia, reuniones y automatización por cuota |
| N14 preparación | R05 roadmap; T05 roadmap/readiness; G G4 | Dependencias, recursos, responsable y resultado observable | Retirar horizontes/volúmenes fijos. Un hito de preparación puede estar bajo control del equipo; no exigir ventas como criterio universal de finalización |
| N15 materialización | R07 stack/playbook; G P1 | Necesidad deriva del diseño, contenido accionable y medio mínimo | Configuración y materiales del recorrido contratado; no desplegar stack ni biblioteca de 40–80 preguntas por plantilla |
| N16 calidad/uso | R06 system-qa; G P2/P1 | Revisión que busca refutar coherencia; criterios y rastro | Añadir cobertura, fundamento, análisis y uso. La coherencia de RevOS por sí sola no declara calidad metodológica suficiente |
| N17 continuidad | R01 cambio; R06 checkpoint; R07 exec; G P3 | Efecto descendente, procedencia y guía de recepción | Gobierno proporcional, historial de versiones materiales, soporte acotado y autonomía; no copiar contadores de dos revisiones ni estructuras de gobierno por rutina |

## Registro de lectura por capacidad

Raíz **G**: `workspace/outputs/work01-20260910/` dentro del consolidado. Raíz **R**: `referencia_corte_v0.1/Go2Rev_snapshot_pre_migracion_v0.1_2026-09-10/20_referencias/RevOS_4.4.0/fuente/`. Raíz **T**: mismo prefijo de referencias, `GTM_Planner_0.3.0/fuente/`.

- **G:** Producto v0.27, definición §§1–10, mapa §12 y estado/continuidad §§30–35; Plan v0.38, entrada/mandato y cierre vigente; Evidencias v0.34, entrada/estado y cierre. No se relee todo el historial acumulado. Método: `metodo/instrucciones_minimas_v0.7.md`, `D2_investigacion_y_decision_v0.2.md`, `G1_oferta_basada_en_evidencia_v0.2.md`, `G2_economia_y_capacidad_v0.2.md`, `G3_recorrido_y_responsabilidades_v0.1.md`, `G4_pruebas_y_construccion_minima_v0.1.md`, `P1_materiales_operativos_v0.2.md`, `P1_preparacion_del_paquete_v0.1.md`, `P3_cierre_y_continuidad_v0.1.md` y `formato_expediente_y_kit_v0.1.md`: instrucciones, criterios y formatos originales leídos como fuentes de diseño.
- **R01:** `.claude-plugin/plugin.json`; `skills/revos-orchestrator/SKILL.md`; `references/grafo-dependencias.md` y `references/convenciones.md` bajo ese directorio; `skills/cambio/SKILL.md`. Lectura de reglas, artefactos, dependencias y tratamiento de cambios.
- **R02:** `skills/client-intake-form/SKILL.md` y `skills/brief-intake/SKILL.md`, procesos y plantillas; `skills/knowledge-base-builder/SKILL.md`, propósito/principios, proceso y encabezados de plantilla. No se atribuye lectura detallada de cada campo de su plantilla.
- **R03:** `skills/competitive-research/SKILL.md`, proceso y plantilla; `skills/revenue-diagnostic/SKILL.md`, proceso y encabezados de plantilla. Se usa el análisis causal; no se atribuye inspección del artefacto visual propuesto.
- **R04:** `skills/positioning-messaging/SKILL.md`, `growth-system-design/SKILL.md`, `sales-conversion-design/SKILL.md`, `channel-strategy-design/SKILL.md` y `sales-process-design/SKILL.md`, todos bajo `skills/`: lectura de procesos y estructura de salida. No se afirma reutilización literal de sus plantillas completas.
- **R05:** `skills/measurement-framework/SKILL.md`, proceso y estructura; `skills/reporting-operating-system/SKILL.md`, proceso y especificación de salidas incluida en él; `skills/execution-roadmap-builder/SKILL.md`, proceso.
- **R06:** `skills/diagnostic-checkpoint/SKILL.md`, proceso/plantilla/cierre; `skills/system-qa/SKILL.md`, principios, proceso y matriz de verificación. Se identifican expresamente su límite de coherencia y su revisión adversarial.
- **R07:** `skills/martech-stack-audit/SKILL.md` y `skills/conversion-playbook-builder/SKILL.md`, proceso; `skills/exec-deliverables/SKILL.md`, especificaciones de documentos ejecutivos y handover. Sin lectura detallada de nodos CRM, martech o diseño de contenido; no se certifica su reutilización.
- **T01:** `skills/intake/SKILL.md` y `references/snapshot-template.md` en ese directorio, completos.
- **T02:** `skills/market-map/SKILL.md` y sus referencias `source-readiness.md`, `three-layer-model.md`, `gap-vs-hole.md`, completos.
- **T03:** `skills/positioning/SKILL.md` y sus referencias `category-decision.md`, `pillar-test.md`, `anti-messages.md`, completos.
- **T04:** `skills/demand-plan/SKILL.md` y sus referencias `engine-catalog.md`, `channel-functions.md`, `benchmark-rules.md`, completos.
- **T05:** `skills/roadmap/SKILL.md` y sus referencias `execution-readiness.md`, `gtm-plan-template.md`, completos.

Las dependencias se han leído en el grafo original y en contratos de las piezas pertinentes, no solo en una compilación. Los documentos binarios de RevOS (Blueprint, Workflow, Master Doc) existen, pero no se han analizado en esta tarea. Su presencia no acredita equivalencia de fórmulas, estilos o estructura. No se necesita leerlos para estas propuestas de capacidad; sí antes de reutilizar materialmente sus componentes.

## Semillas y antecedentes

Se leyó completo `semillas/go2rev_marco-operativo_v1.md`; de la investigación duplicada, las tesis iniciales y `Recommendations`, incluidos arquitectura, precios, umbrales y secuencia. De `investigacion/Go2Rev_revision_fundamentos_v0.1_2026-09-09.md`, las correcciones y fundamentos metodológicos pertinentes. Esta revisión es una fuente interna secundaria; sus URLs no se consideran páginas recuperadas en esta sesión.

Se conserva la distinción entre iniciar una ruta y mejorar una ya existente, y entre modelo de negocio y B2B/B2C. Se retiran módulos obligatorios, tarifas, plazos, umbrales y transición a RevOS. No se adoptan contextos empresariales, especializaciones geográficas ni afirmaciones de exclusividad de las semillas. La base se construye desde la promesa de producto y los contratos de capacidad.

## Disponibilidad para la construcción

El registro de ausencias se conserva en `00_control_exportacion/faltantes_y_exclusiones_externas.json`, dentro del archivo de procedencia. No se incorpora como backlog de producto ni se reconstruyen originales. Recuperar un documento histórico no es un entregable de construcción.

Cuando falte un original metodológico pertinente, se identificará la regla cuya reutilización no puede acreditarse y se redactará un componente propio desde su contrato. Una fórmula, plantilla o instrucción solo se incorporará después de examinar su contenido y adaptarlo al alcance fundacional. Los binarios no leídos mantienen ese límite de reutilización.

La primera versión debe contener todo lo necesario para prestar su alcance sin cargar el archivo histórico. La procedencia permite justificar decisiones de diseño; no sustituye una pieza pendiente ni se convierte en dependencia de operación.
