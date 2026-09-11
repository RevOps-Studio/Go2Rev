# Plantilla de evento y medida

Versión 0.1 · K13 · Campos empresariales vacíos

Usar con [medición y revisión](../01_medicion_y_revision.md). Repetir el bloque por evento/medida pertinente, agrupando definiciones compartidas. No exige un dashboard ni una cantidad fija de indicadores.

| Campo | Regla | Valor |
|---|---|---|
| Referencia y estado | K13/sección/revisión, ubicación, autor, fecha y estado documental | |
| Encargo y uso | K01/revisión, ámbito y uso E/O de los campos | |
| Decisión | Compromiso que podría cambiar, responsable y alternativas | |
| Mecanismo | Relación entre evento, condición/resultado y decisión; AF que la fundamenta | |
| Evento | Qué sucede y qué condición acredita el hecho; distinguir actividad, señal, compra, entrega y caja | |
| Objeto e identidad | Unidad, identificador/enlace, deduplicación y repetición pertinente | |
| Población | Inclusión/exclusión, ámbito y cobertura del universo elegible | |
| Fechas y ventana | Hecho, registro, recepción, corte, calendario/zona y seguimiento pertinente | |
| Medida y unidad | Nombre descriptivo, magnitud/unidad y significado para la decisión | |
| Fórmula y dominio | Entradas, transformaciones, numerador/denominador y condición de cálculo; referencia K12 cuando proceda | |
| Fuentes | FUE/sistema/campo, original, cobertura leída, versión y responsable | |
| Conciliación | Qué gobierna cada dato/estado y cómo se resuelve discrepancia, duplicidad o llegada tardía | |
| Captura | Origen, extracción/recepción, transformación, destino y medio suficiente para N15 | |
| Disponibilidad | CAP, acceso, calidad, latencia y requisitos por habilitar | |
| Ausencias | Desconocido, inválido, pendiente y cero observado separados; efecto sobre cálculo/conclusión | |
| Línea base y referencia | Periodo/población comparables, fuente y límite; ausencia sin sustitución arbitraria | |
| Objetivo | Aspiración o compromiso, DEC y horizonte; separado de observación | |
| Umbral de acción | Fundamento K12/condición/riesgo o relación simbólica, autoridad y acción que activa | |
| Interpretación | Explicación, alternativa contraria, madurez, sesgos y límite de generalización/atribución | |
| Responsables | Quién captura/calcula, quién interpreta y quién decide; disponibilidad pertinente | |
| Revisión | Evento o periodo justificado y plazo útil para actuar; sin reunión obligatoria | |
| Comprobación requerida | Qué debe verificar N16 para declarar captura/cálculo/consulta preparados | |
| Consumo y cambios | Receptor/campo/revisión, disposición, HUE/CON y condición CAM | |

La futura observación y decisión se relacionan en [revisión y decisión](02_revision_y_decision.md). La plantilla general no contiene valores, objetivos ni umbrales empresariales.

## Aplicabilidad de los bloques

Antes de emitir K13, completar el núcleo de [N13 Instrumentar para decidir](../../../operacion_conversacional/v0.2/10_primera_pasada.md). Las reglas CONTR, EVAL, USO y de variante de esta plantilla mantienen su momento de exigibilidad. Un bloque condicional se completa cuando afecte al resultado; documentar la condición que lo hace aplicable o su exclusión. Una ausencia material queda localizada y limita el uso dependiente. La cabecera común se registra una vez por artefacto.
