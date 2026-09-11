# Cobertura e integración del conjunto

Versión de conjunto 0.4 · Correspondencia de producto

Este mapa relaciona obligaciones de arquitectura con las instrucciones que las desarrollan. Orienta la revisión documental y la selección de piezas; no sustituye sus procedimientos, crea otro plan maestro ni acredita ejecución. La arquitectura mantiene los diecisiete nodos y la correspondencia con los once pasos de origen (auditoría conservada en el repositorio de desarrollo).

## Cobertura por nodo

| Nodo | Productor sustantivo | Contrato y consumidor decisivo |
|---|---|---|
| N01 | [Encargo y salida](../../metodo/encargo_y_conocimiento/v0.1/01_encargo_y_salida.md) | K01: alcance/autoridad y economía de salida para N06/N17 y compromisos de todos |
| N02 | [Conocimiento y solicitud](../../metodo/encargo_y_conocimiento/v0.1/02_conocimiento_y_solicitud.md) | K02: originales/AF, TRA/CAP, huecos y consumo por campo |
| N03 | [Mercado y acceso](../../metodo/investigacion_y_diagnostic/v0.2/02_mercado_y_acceso.md) | K03: ámbito, población, condiciones y acceso para compra y viabilidad |
| N04 | [Comprador y compra](../../metodo/investigacion_y_diagnostic/v0.2/03_comprador_y_compra.md) | K04: situaciones, roles, criterios y eventos para alternativa, oferta y ruta |
| N05 | [Alternativas y diferenciación](../../metodo/investigacion_y_diagnostic/v0.2/04_alternativas_y_diferenciacion.md) | K05: comparación y diferencia fundada para N06–N10 |
| N06 | [Recomendación Diagnostic](../../metodo/investigacion_y_diagnostic/v0.2/05_recomendacion_diagnostic.md) | K06: combinación, fundamento, condiciones y recomendación; DEC separado |
| N07 | [Posicionamiento y promesas](../../metodo/posicionamiento_demanda_y_conversion/v0.1/01_posicionamiento_y_promesas.md) | K07: marco, afirmaciones y límites para oferta, mensajes y materiales |
| N08 | [Oferta y precio](../../metodo/oferta_entrega_y_economia/v0.1/01_oferta_y_precio.md) | K08: unidad, alcance, mecanismo y condiciones para N06/N09–N12/N15 |
| N09 | [Acceso y demanda](../../metodo/posicionamiento_demanda_y_conversion/v0.1/02_acceso_y_demanda.md) | K09: mecanismo/población, trabajo, señal y recepción para N10/N12–N16 |
| N10 | [Conversión y compra](../../metodo/posicionamiento_demanda_y_conversion/v0.1/03_conversion_y_compra.md) | K10: transiciones, autoridad, trabajo y aceptación para N11–N16 |
| N11 | [Entrega y cobro](../../metodo/oferta_entrega_y_economia/v0.1/02_entrega_y_cobro.md) | K11: tareas/recursos, conformidad, incidencias y caja para oferta/economía/kit |
| N12 | [Economía y capacidad](../../metodo/oferta_entrega_y_economia/v0.1/03_economia_y_capacidad.md) | K12: dominio, resultado, restricciones y umbral para Diagnostic y decisiones |
| N13 | [Medición y revisión](../../metodo/medicion_preparacion_y_transferencia/v0.1/01_medicion_y_revision.md) | K13: evento, identidad, cálculo, fuente y decisión para preparar/continuar |
| N14 | [Preparación y secuencia](../../metodo/medicion_preparacion_y_transferencia/v0.1/02_preparacion_y_secuencia.md) | K14: obligaciones y protocolos previos para N15/N16/N17 |
| N15 | [Materialización y uso](../../metodo/medicion_preparacion_y_transferencia/v0.1/04_materializacion_y_uso.md) | K15: contenido, fuente/vista y configuración real para comprobar/transferir |
| N16 | [Comprobación de preparación](../../metodo/medicion_preparacion_y_transferencia/v0.1/05_comprobacion_de_preparacion.md) | K16: resultado con contexto/criterio, ayuda, defecto y límite para N17 |
| N17 | [Transferencia y cierre](../../metodo/medicion_preparacion_y_transferencia/v0.1/06_transferencia_y_cierre.md) | K17: estado, recepción, fuentes, continuidad y fin del acompañamiento |

Las guías de componente enlazan sus plantillas vacías. Los contratos comunes se mantienen en [encargo y conocimiento](../../metodo/encargo_y_conocimiento/v0.1/03_contratos_y_diccionario.md), [investigación y Diagnostic](../../metodo/investigacion_y_diagnostic/v0.2/06_contratos_y_economia_exploratoria.md), [oferta, entrega y economía](../../metodo/oferta_entrega_y_economia/v0.1/07_contratos_y_revision.md), [posición, demanda y conversión](../../metodo/posicionamiento_demanda_y_conversion/v0.1/06_contratos_y_revision.md), [preparación y transferencia](../../metodo/medicion_preparacion_y_transferencia/v0.1/07_contratos_y_revision.md) y [operación conversacional](../../metodo/operacion_conversacional/v0.3/06_contrato_y_revision.md). Una recepción es por campo, versión, uso y suficiencia; no es un aprobado de nodo ni una autorización de negocio.

## Interfaces que deben conservarse

**Investigación y decisión.** La [lectura externa y contraste](../../metodo/investigacion_y_diagnostic/v0.2/08_investigacion_externa_y_contraste.md) conecta fuente/AF externa, premisa propia, comparabilidad, derivación y campo afectado. La [rutina de fuentes](../../metodo/investigacion_y_diagnostic/v0.2/09_rutina_de_fuentes_y_acceso.md) incorpora propuestas por necesidad; disponibilidad/conexión no se consume como contenido leído. Evidencia contraria y hallazgos no contemplados en el encargo forman parte del análisis.

**Iteración exploratoria.** K08 E representa unidad/oferta; K09/K10 E y K11 E producen acceso, compra, trabajo y cumplimiento; K12 E devuelve economía/restricciones; K06 recomienda. Las entradas E no exigen K06 final ni K07 adoptado. La iteración termina por suficiencia para el compromiso o por una carencia delimitada que requiere otra salida, nunca por una cuota de vueltas.

**Evidencia adicional.** N14 puede preparar una pregunta de Diagnostic con el diseño disponible; N13/N15 aportan observación y piezas pertinentes, y N16 comprueba la preparación de ese ámbito cuando proceda. Los [protocolos de evidencia](../../metodo/medicion_preparacion_y_transferencia/v0.1/03_protocolos_de_evidencia.md) devuelven originales/AF al productor analítico. El resultado de una tarea del operador no sustituye una conclusión de mercado.

**Costes y capacidad.** Las [cohortes y actividad](../../metodo/posicionamiento_demanda_y_conversion/v0.1/04_costes_cohortes_y_capacidad.md) producen coste/carga de todos los intentos. K12 conserva identidad, población, periodo y cobertura; un reparto no crea otra partida y un coste por resultado no se convierte por ello en variable lineal. Las [fórmulas](../../metodo/oferta_entrega_y_economia/v0.1/04_formulas_y_dominio.md) y [guía del libro](../../metodo/oferta_entrega_y_economia/v0.1/08_guia_del_modelo.md) mantienen unidades, dominio, desconocidos, calendarios y automatización explícita.

**Diseño y preparación.** Las variantes de compra/entrega determinan obligaciones K14, contenido K15, criterios/observaciones K16 y recepción K17. La cobertura viene tanto de la promesa como de la incertidumbre; no exige un fallo previo para construir una pieza necesaria. Contenido, configuración, uso y resultado comercial conservan estados distintos.

**Cambios y cierre.** CAM identifica productor y consumidores efectivos; actualizar fuente antes de vistas y dependientes, retirando usos de premisas invalidadas. K17 puede recibir la salida Diagnostic con K01/K06 sin exigir construcción posterior. Una recepción condicionada preserva la carencia y la terminación del soporte sigue K01.

## Cobertura transversal del producto

| Obligación | Desarrollo y localizador |
|---|---|
| B2B y recorridos A/B; variantes con límites | [Alcance](02_alcance_y_variantes.md), TRA/CAP encargo y conocimiento y reglas oferta, entrega y economía/posición, demanda y conversión |
| Cinco conjuntos recibibles | [Composición de entregas](03_entregables_y_recepcion.md) y N15/N17 |
| Gobierno proporcionado | [Dependencias y gobierno](../../arquitectura/v0.2/04_dependencias_y_gobernanza.md), K01/DEC y tres momentos de compromiso |
| Conversación y autonomía | [Entrada común](../../metodo/operacion_conversacional/v0.3/ENTRADA_GO2REV.md), guía y rutas; uso sin RevOS o LLM |
| Capacidades y alternativa suficiente | [Capacidades](../../metodo/operacion_conversacional/v0.3/03_capacidades_y_alternativas.md) y [adaptación](../../metodo/operacion_conversacional/v0.3/04_adaptacion_del_entorno.md) |
| Continuidad y conservación | [Continuidad](../../metodo/operacion_conversacional/v0.3/05_continuidad_y_cambios.md) y [versiones del producto](05_versiones_y_mantenimiento.md) |
| Paquete autónomo y fuentes editables | [Inventario](INVENTARIO.md), manifiesto y guías; archivo histórico ajeno a la operación |

## Procedencia y alcance de reutilización

La integración usa las fuentes metodológicas actuales de arquitectura–operación conversacional. Sus correspondencias identifican los originales Go2Rev, RevOS 4.4.0, GTM Planner 0.3.0 y semillas pertinentes realmente leídos, con alcance y límites. paquete de implementación conserva esos límites; no atribuye una nueva lectura de todo el archivo ni reutilización de motores o documentos no inspeccionados.

Se conserva la arquitectura, contratos y razonamiento construidos; se adapta navegación y formulación temporal para el conjunto disponible; se completa guía de implementación, composición de entregas, alcance y fijación de versión; se retiran de la entrada operativa los avisos de componentes futuros ya construidos y las dependencias del índice de desarrollo. Las fuentes de procedencia siguen siendo referencias de diseño, no fuentes editables de la prestación.

El resultado de revisión y cierre de construcción se registra en Evidencias y el estado en el Plan del desarrollo. Este mapa es una especificación de cobertura del producto y no otro registro de pruebas o resultados.
