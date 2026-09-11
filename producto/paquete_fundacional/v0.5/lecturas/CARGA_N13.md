# Go2Rev · N13 · Lectura inicial

Conjunto 0.5 · Compilación derivada, no fuente editable. El contenido expresamente incluido sustituye la apertura del original metodológico de esa versión; una sección no sustituye el resto del archivo. Las fuentes del encargo y del mercado requieren lectura efectiva.

## N13 · Instrumentar para decidir

**Entrada:** Decisión, eventos, unidades y fuentes.

**Salida:** K13; consumo por N14, N15, N16, N17.

**Cierre:** Instrumentar las decisiones necesarias; incorporar métricas estándar solo con definición y fundamento compatibles.

**Destino:** 01 Entregables/Design. Mantener fuente, vista e índice.

<a id="fuente-4692cc11a61d"></a>

## Fuente: 01_medicion_y_revision.md

Procedencia: `producto/metodo/medicion_preparacion_y_transferencia/v0.1/01_medicion_y_revision.md` · SHA256 `509df7814b0e3c36f524e68c3b0a2f4210e90870e1278134191262c8a610f95f` · Incluye: sección Procedimiento de primera pasada íntegra.

## Procedimiento de primera pasada

Trabajar con la entrada común y aplicar [INV-01–20](../../../metodo/operacion_conversacional/v0.3/13_invariantes.md). Los identificadores de campos y bloques se localizan en la plantilla generada; la referencia posterior conserva el razonamiento y sus casos de aplicabilidad.

1. Partir de una decisión que necesita información y de los eventos K09–K12. Precisar objeto, identidad, fecha y unidad de análisis.
2. Definir captura, fuente, responsable, cálculo y corte de cada medida. Abrir relaciones y excepciones si hay agregación, duplicados, faltantes o transición entre sistemas.
3. Diseñar revisión e interpretación: condición, autoridad y acción ante el resultado. Abrir la ficha de revisión para vincular medida y decisión.
4. Entregar K13 a N15 para instrumentar y a N16 para comprobar contenido y funcionamiento pertinentes; mantener límites de cobertura y trazabilidad hasta el original.

**Bloques de salida:** K13.T01.B01. Su condición y momento gobiernan la exigibilidad; las piezas auxiliares se abren según la tarea.

<a id="fuente-cc7f6eec16e9"></a>

## Fuente: 01_evento_y_medida.md

Procedencia: `producto/metodo/medicion_preparacion_y_transferencia/v0.1/plantillas/01_evento_y_medida.md` · SHA256 `653214009e60037d1779269107a96978491be3384258e99b912e528e8d5e35d6` · Incluye: archivo íntegro.

# Plantilla de evento y medida

Vista generada · Corregir la [definición de campos](../../../metodo/esquema/v0.1/plantillas.json), no esta vista. ★ = campo de la plantilla principal: aplicar condición y momento; las piezas auxiliares pueden ser indispensables. Cabecera: identidad, versión, ámbito y K01, autor y fecha, ubicación, estado documental, receptor y uso. Registrar una vez por artefacto; los bloques remiten a ella. FUE, AF y otros registros con identidad propia conservan sus metadatos. La aceptación se localiza en DEC.


Versión 0.1 · K13 · Campos empresariales vacíos

Usar con [medición y revisión](../../../metodo/medicion_preparacion_y_transferencia/v0.1/01_medicion_y_revision.md). Repetir el bloque por evento/medida pertinente, agrupando definiciones compartidas. No exige un dashboard ni una cantidad fija de indicadores.

<a id="k13-t01-b01"></a>

<!-- bloque: K13.T01.B01 -->
| Campo | Regla | Valor |
|---|---|---|
| ★ Referencia y estado | K13/sección/revisión, ubicación, autor, fecha y estado documental |  |
| ★ Encargo y uso | K01/revisión, ámbito y uso E/O de los campos |  |
| ★ Decisión | Compromiso que podría cambiar, responsable y alternativas |  |
| ★ Mecanismo | Relación entre evento, condición/resultado y decisión; AF que la fundamenta |  |
| ★ Evento | Qué sucede y qué condición acredita el hecho; distinguir actividad, señal, compra, entrega y caja |  |
| ★ Objeto e identidad | Unidad, identificador/enlace, deduplicación y repetición pertinente |  |
| ★ Población | Inclusión/exclusión, ámbito y cobertura del universo elegible |  |
| ★ Fechas y ventana | Hecho, registro, recepción, corte, calendario/zona y seguimiento pertinente |  |
| ★ Medida y unidad | Nombre descriptivo, magnitud/unidad y significado para la decisión |  |
| ★ Fórmula y dominio | Entradas, transformaciones, numerador/denominador y condición de cálculo; referencia K12 cuando proceda |  |
| ★ Fuentes | FUE/sistema/campo, original, cobertura leída, versión y responsable |  |
| ★ Conciliación | Qué gobierna cada dato/estado y cómo se resuelve discrepancia, duplicidad o llegada tardía |  |
| ★ Captura | Origen, extracción/recepción, transformación, destino y medio suficiente para N15 |  |
| ★ Disponibilidad | CAP, acceso, calidad, latencia y requisitos por habilitar |  |
| ★ Ausencias | Desconocido, inválido, pendiente y cero observado separados; efecto sobre cálculo/conclusión |  |
| ★ Línea base y referencia | Periodo/población comparables, fuente y límite; ausencia sin sustitución arbitraria |  |
| ★ Objetivo | Aspiración o compromiso, DEC y horizonte; separado de observación |  |
| ★ Umbral de acción | Fundamento K12/condición/riesgo o relación simbólica, autoridad y acción que activa |  |
| ★ Interpretación | Explicación, alternativa contraria, madurez, sesgos y límite de generalización/atribución |  |
| ★ Responsables | Quién captura/calcula, quién interpreta y quién decide; disponibilidad pertinente |  |
| ★ Revisión | Evento o periodo justificado y plazo útil para actuar; sin reunión obligatoria |  |
| ★ Comprobación requerida | Qué debe verificar N16 para declarar captura/cálculo/consulta preparados |  |
| ★ Consumo y cambios | Receptor/campo/revisión, disposición, HUE/CON y condición CAM |  |

La futura observación y decisión se relacionan en [revisión y decisión](../../../metodo/medicion_preparacion_y_transferencia/v0.1/plantillas/02_revision_y_decision.md). La plantilla general no contiene valores, objetivos ni umbrales empresariales.

## Aplicabilidad de los bloques

Antes de emitir K13, completar el núcleo de [N13 Instrumentar para decidir](../../../metodo/operacion_conversacional/v0.3/10_primera_pasada.md). Las reglas CONTR, EVAL, USO y de variante de esta plantilla mantienen su momento de exigibilidad. Un bloque condicional se completa cuando afecte al resultado; documentar la condición que lo hace aplicable o su exclusión. Una ausencia material queda localizada y limita el uso dependiente. La cabecera común se registra una vez por artefacto.


## Ampliar según la tarea

Abrir las secciones indicadas antes del uso dependiente; conservar el resto localizable.

| Condición | Lectura y sección |
|---|---|
| Al desarrollar una decisión, variante o excepción que los pasos breves no resuelven; antes de usar una fórmula o procedimiento especializado. | [01_medicion_y_revision](CARGA_N13_extension.md#fuente-4692cc11a61d): Referencia sustantiva pertinente a la pregunta |
| Antes de emitir el resultado a su consumidor; al cambiar entradas, ámbito o uso E/O. | [07_contratos_y_revision](CARGA_N13_extension.md#fuente-6b7560f1965b): Contrato K13 y relación de consumo afectada |
| Al vincular una medida con una revisión y acción de autoridad. | [02_revision_y_decision](CARGA_N13_extension.md#fuente-867a7f99cd43): Bloques aplicables de la plantilla |
