# Plantilla · Decisiones, artefactos, consumo y cambios

Versión de plantilla 0.1 · Campos de prestación vacíos

Usar con [contratos y diccionario](../03_contratos_y_diccionario.md). Son registros de una futura prestación. La columna Valor permanece vacía en el producto. Repetir solo por decisiones, entregas y dependencias materiales; pueden convivir en un índice compartido con K01/K02.

## Decisión DEC · Bloque repetible

Productor de propuesta: asistente/consultor. Autoridad: la identificada en K01. Los campos de disposición se completan cuando se produzca la decisión; mientras, su estado es propuesta. La naturaleza del registro es decisión y no equivale a evidencia de mercado.

| Campo | Regla | Valor |
|---|---|---|
| ID, revisión, autor y fecha de propuesta | Identidad y contenido | |
| Pregunta y compromiso | Qué se decide, alcance y consecuencia | |
| K01 y autoridad competente | Revisión del encargo, rol y facultad de decisión | |
| Opciones consideradas | Alternativas materiales, incluida limitación o no continuación si pertinente | |
| Recomendación y razón | Opción propuesta, mecanismo, comparación y principal argumento contrario examinado | |
| Entradas y revisiones | K/AF/FUE/TRA/CAP, campos y versiones que sustentan la propuesta | |
| Criterio y juicio de suficiencia | Qué evidencia exige el compromiso y por qué basta o no lo disponible | |
| Incertidumbres y límites | HUE/CON, consecuencia y condiciones | |
| Disposición | Propuesta, aceptada, condicionada o rechazada; solo autoridad identificada | |
| Decisor, fecha y rastro | Original/localizador de la decisión efectiva y alcance; requerido al disponer | |
| Compromiso habilitado | Acción, recurso y límites que realmente permite la decisión; requerido al disponer | |
| Condición pendiente | Responsable, evidencia de cumplimiento, evento límite y parte detenida; requerido si condicionada | |
| Revisión y consumidores | Qué cambio la reabre y qué artefactos utilizan la decisión | |

## Artefacto · Bloque repetible por salida lógica K

Productor: nodo responsable. K01 y K02 pueden referir su cabecera y añadir únicamente los campos que falten; no duplicar sus metadatos. Este formato es común para los nodos posteriores.

| Campo | Regla | Valor |
|---|---|---|
| ID, revisión y ubicación | K del productor, archivo/sección y contenido actual | |
| Productor, autor y fecha | Nodo y responsable de elaboración | |
| Finalidad y ámbito | Decisión o tarea; unidad/periodo y variante pertinente | |
| Entradas y fuentes editables | Versiones, AF/FUE, cálculos o registros que sustentan los campos materiales | |
| Campos consumibles | Campo/sección, significado, unidad si procede, uso E/O y limitaciones | |
| Estado y revisión documental | Borrador/revisado/sustituido; revisor, fecha y cobertura | |
| Consumidores | Relaciones de uso por nodo/campo | |
| Decisión relacionada | DEC, si habilita compromiso; no inferir aceptación del estado revisado | |
| Reapertura y contenido anterior | Condición de revisión y localizador de versiones utilizadas previamente | |

## Relación de consumo · Bloque repetible por conjunto coherente de campos

Productor: describe la entrada. Analista receptor: determina suficiencia para la tarea, sin sustituir autoridad de negocio. Se puede agrupar un conjunto de campos con el mismo productor, versión, ámbito y uso.

| Campo | Regla | Valor |
|---|---|---|
| Entrada de productor | K/AF/TRA/CAP, revisión, campos y localizador | |
| Consumidor y decisión | Nodo/artefacto receptor y tarea que necesita los campos | |
| Compatibilidad | Ámbito, periodo, unidades y vigencia revisados | |
| Uso propuesto | E/O y conclusión o compromiso preciso | |
| Juicio de suficiencia | Fundamento, contradicciones y ausencias relevantes | |
| Disposición de recepción | Admitido, admitido con límites o devuelto | |
| Límites o devolución | Campo concreto, razón, responsable productor y condición para volver a consumir | |
| Responsable y fecha | Analista receptor; no equivale a aprobación del patrocinador | |
| Dependencias resultantes | Artefactos/decisiones que desde ahora dependen de esa versión | |

## Cambio CAM · Bloque repetible por modificación material

Productor: analista con responsables afectados. K01 gobierna quién puede autorizar un compromiso distinto. Un cambio propuesto no sustituye la versión aceptada antes de esa decisión.

| Campo | Regla | Valor |
|---|---|---|
| ID, revisión, autor y fecha | Identidad y contenido del cambio | |
| Objeto y campo | K/AF/FUE/TRA/CAP/DEC y localizador | |
| Contenido anterior y propuesto | Revisiones, valor o premisa y diferencia de significado | |
| Causa, fuente y ámbito | Nuevo original, corrección, periodo o decisión; referencias y alcance | |
| Impacto directo | Relaciones de consumo afectadas y efecto sobre conclusiones/compromisos | |
| Descendientes | Dependencias sucesivas hasta acotar el efecto; no asumir actualización global | |
| Uso pendiente de revisión | Compromiso que debe limitarse y desde qué momento | |
| Autoridad necesaria | DEC si cambia alcance, recurso o compromiso; motivo si no requiere nueva decisión | |
| Responsable de resolución | Quién actualiza productor y quién revisa consumidores | |
| Condición de cierre | Disposiciones resueltas, versiones resultantes y límites visibles | |

### Disposición de impacto · Bloque repetible por artefacto o decisión afectada

| Campo | Regla | Valor |
|---|---|---|
| Afectado y campo | Identificador/revisión, dependencia y localizador | |
| Acción | Actualizar, recalcular, revisar argumento, retirar uso o sin impacto con razón | |
| Fundamento y alcance | Por qué esa disposición es suficiente y qué no cambia | |
| Responsable y orden | Productor antes que consumidor; evento necesario para cierre | |
| Resolución | Versión resultante, revisión realizada y DEC si corresponde | |
| Uso resultante y límites | Compromiso habilitado o pendiente, con fundamento | |
