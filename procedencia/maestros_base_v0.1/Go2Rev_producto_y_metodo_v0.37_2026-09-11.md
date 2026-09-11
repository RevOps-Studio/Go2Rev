# Go2Rev Producto y método v0.37

11 de septiembre de 2026 · Responsable de producto Carlos Estrada

[Plan v0.48](Go2Rev_plan_de_trabajo_v0.48_2026-09-11.md) · [Evidencias v0.44](Go2Rev_evidencias_y_pruebas_v0.44_2026-09-11.md)

## Definición y estado

Go2Rev es un servicio de consultoría de RevOps Studio para diseñar y preparar un sistema comercial conectado alrededor de una iniciativa: comprador, oferta, acceso, venta, entrega y cobro. El cliente recibe trabajo y entregables comprometidos, con responsabilidad del consultor y método propio. La herramienta facilita esa prestación; el servicio tiene valor y continuidad autónomos.

La primera versión está construida como [paquete fundacional v0.1](producto/paquete_fundacional/v0.1/LEEME.md), con cierre documental del asistente el 11 de septiembre de 2026. Sigue siendo enteramente teórica: no ha habido clientes ni pruebas de la metodología. Conserva la arquitectura de diecisiete nodos aceptada por Carlos; no se atribuye aceptación adicional del cierre. Sus fuentes contienen capacidades generales y campos empresariales vacíos.

## Alcance aceptado

El foco inicial es B2B, sin reducirlo a software o suscripciones. Se mantienen dos recorridos: **A, oferta existente en contexto nuevo**, y **B, nueva iniciativa**. A tiene prioridad inicial; ambos comparten el sistema metodológico. B2C permanece como extensión conceptual, fuera del alcance inicial que se declarará implementable.

La unidad de encargo es una iniciativa, un mercado prioritario y un primer segmento de compra. El mercado y el segmento pueden ser resultados del Diagnostic dentro de alternativas acotadas. El cliente no debe aportar ya resuelta la investigación que contrata.

En A se separa conocimiento de origen y destino: necesidad, comprador, alternativa, acceso, precio, entrega y condiciones de entrada. En B se distinguen intención, representación de oferta y capacidad disponible o por habilitar. La falta de historial comercial no impide diseñar el método ni iniciar una evaluación fundada.

Venta directa, distribución, autoservicio y combinaciones cambian unidades, roles y traspasos. Producto físico, servicios y recurrencia requieren reglas económicas y de cumplimiento pertinentes. El [alcance de la versión fundacional](producto/paquete_fundacional/v0.1/02_alcance_y_variantes.md) declara las rutas y formas de oferta desarrolladas, sus reglas combinables y límites de automatización; una capacidad efectiva de prestación requiere además recursos y autoridad propios.

## Promesa y límites de prestación

El compromiso base es **diseño conectado y preparación operativa comprobada, con acompañamiento acotado** a las actuaciones expresamente acordadas. Incluye investigación, diseño, materiales y preparación necesarios para el recorrido contratado. La comprobación de uso con operador pertenece a la futura prestación, una vez que la metodología esté construida.

El alcance comercial se acuerda con acciones, recursos, responsables, revisiones y condición de finalización. No incluye operación permanente, compra de medios, desarrollo completo del producto del cliente, implantaciones extensas ni servicios especializados no acordados. Marca, contenido, CRM e integraciones se incorporan cuando sean necesarios para cumplir el alcance y exista capacidad asignada.

No se garantizan ventas, margen, repetibilidad ni resultados dependientes de compradores o terceros. Identificar un recurso no acredita su disponibilidad. Si falta una dependencia indispensable, la entrega debe limitarse, completarse o modificarse de forma expresa.

El cliente puede recibir entregables autónomos sin contratar RevOS, usar un plugin o disponer de un LLM. Los derechos y condiciones de uso de sus entregables se concretarán en la contratación. Precio y duración comerciales se estimarán según alcance; no se establecen valores universales a partir de referencias metodológicas.

## Salida de Diagnostic prevista desde la contratación

El encargo debe prever el valor de la evaluación y las condiciones para continuar, ajustar, aplazar o terminar sin construir el sistema del cliente. Esto forma parte del producto; no obliga a vender fases como paquetes separados.

| Decisión de Diagnostic | Consecuencia que debe prever el encargo |
|---|---|
| Continuar | Diseño y preparación dentro del alcance y recursos acordados |
| Continuar con condiciones | Resolver o limitar incertidumbres antes del compromiso dependiente |
| Obtener evidencia adicional | Delimitar pregunta, actuación, recursos, responsable y decisión posterior |
| Ajustar | Revisar iniciativa, segmento, oferta o acceso y el efecto sobre el encargo |
| Aplazar o cerrar | Entregar evaluación fundamentada y aplicar las condiciones del trabajo que no se ejecutará |

La forma económica de esta salida se fija antes de contratar. Un cierre de evaluación se reconoce como tal; no equivale a entregar un sistema comercial preparado.

## Fases y entregables

Diagnostic investiga oportunidad, comprador, alternativas, productos/soluciones, tendencias, acceso, capacidades y economía inicial. La lectura externa se cruza con información, objetivos y recursos del cliente para producir conclusiones y una recomendación. Una recomendación integral exige contraste externo pertinente; la carencia material limita su alcance. Design conecta posición, oferta, precio, demanda, conversión, entrega, cobro, economía y medición. Despliegue materializa el alcance, comprueba su preparación y transfiere la continuidad. Las dependencias permiten revisar decisiones anteriores.

Se mantienen cinco conjuntos de entrega. La agrupación sirve a la recepción y el uso; no impone cinco documentos ni cinco skills.

| Conjunto | Contenido exigible | Condición de recepción durante una prestación |
|---|---|---|
| Evaluación de oportunidad y viabilidad | Fuentes, alternativas, restricciones, hipótesis, economía exploratoria y recomendación | Explica qué decisión puede tomarse, su fundamento y qué la cambiaría |
| Diseño del sistema comercial | Comprador, posicionamiento, oferta, precio, demanda, conversión, entrega/cobro, responsables y medición | Decisiones compatibles entre sí, con los recursos y con el alcance |
| Modelo económico editable | Entradas con procedencia, unidades, fórmulas, escenarios, contribución, caja, capacidad y umbrales | Distingue calculable, estimado y desconocido y mantiene trazabilidad |
| Kit inicial de operación | Materiales, instrucciones, registros y configuración pertinentes a las tareas contratadas | El operador dispone del contenido y los medios necesarios para actuar |
| Despliegue y transferencia | Acciones, dependencias, responsables, criterios, observaciones, límites y guía de continuidad | El estado entregado corresponde a lo realizado y permite continuar autónomamente |

La base fundacional contiene los métodos, plantillas y [guía de composición y recepción](producto/paquete_fundacional/v0.1/03_entregables_y_recepcion.md) para producir estos conjuntos. Los datos y resultados de una prestación se incorporarán únicamente cuando exista ese encargo, fuera de las fuentes generales del producto.

## Arquitectura aceptada

La [arquitectura v0.2](producto/arquitectura/v0.2/01_arquitectura_metodologica.md) conserva la correspondencia explícita con los once pasos de origen y desarrolla diecisiete capacidades. Los nodos identifican trabajo intelectual y contratos; pueden compartir archivos e instrucciones.

| Grupo | Nodos |
|---|---|
| Encuadre y conocimiento | N01 encargo, N02 base interna |
| Investigación y recomendación | N03 mercado/acceso, N04 comprador/compra, N05 alternativas, N06 viabilidad |
| Diseño comercial y económico | N07 posicionamiento, N08 oferta/precio, N09 demanda, N10 conversión, N11 entrega/cobro, N12 economía/capacidad |
| Preparación y continuidad | N13 medición, N14 preparación/protocolos, N15 materialización, N16 comprobación, N17 transferencia/cierre |

Diagnostic puede consumir versiones exploratorias de oferta, acceso, compra, entrega y economía. Son representaciones de decisión que se producirán con la información de una prestación; no requieren un diseño definitivo ni convierten una hipótesis en hecho.

La arquitectura separa suficiencia de evidencia, calidad del análisis, autoridad para decidir y preparación efectiva. Una aprobación no aumenta la evidencia. La revisión atiende cobertura, fundamento, análisis, coherencia y utilidad; no se resuelve mediante un promedio de puntuaciones.

El detalle está en [información y contratos](producto/arquitectura/v0.2/02_informacion_y_contratos.md), [nodos](producto/arquitectura/v0.2/03_nodos_y_entregables.md), [dependencias y gobierno](producto/arquitectura/v0.2/04_dependencias_y_gobernanza.md), [reutilización](producto/arquitectura/v0.2/05_reutilizacion_y_fuentes.md) y [componentes de construcción](producto/arquitectura/v0.2/06_construccion_y_revision.md).

## Componente construido: encargo y conocimiento

[Encargo y conocimiento v0.1](producto/metodo/encargo_y_conocimiento/v0.1/LEEME.md) desarrolla N01 y N02 con instrucciones de prestación, contratos de entrada y salida, guía de uso por conversación y seis plantillas vacías. La arquitectura de diecisiete nodos se mantiene.

N01 convierte mandato, pregunta y promesa en un encargo delimitado. La salida de Diagnostic concreta evaluación recibible, consecuencias por decisión, tratamiento económico, autoridad, recursos y finalización del acompañamiento antes de contratar. No fija precios ni presume condiciones económicas universales.

N02 separa petición, recepción, original y conclusión. Define extracción de afirmaciones, reconciliación de ámbitos/unidades, análisis de tensiones, inferencias e hipótesis con razonamiento, solicitud selectiva y suficiencia por uso. A compara condiciones de origen y destino; B relaciona intención, representación y disponibilidad de capacidades.

Los registros son secciones editables agrupables, con referencias estables y campos empresariales vacíos. La recepción se resuelve por los campos que necesita cada consumidor. Una carencia limita el compromiso dependiente; una aprobación no aumenta la evidencia. La semántica de decisiones, artefactos y cambios es común a los nodos posteriores.

El componente es una pieza terminada de construcción, con revisión documental propia del asistente. Su integración con los demás componentes está identificada en el paquete fundacional. Las instrucciones describen la futura prestación; no se han aplicado ni probado durante esta construcción.

## Componente construido: investigación y Diagnostic

[Investigación y recomendación Diagnostic v0.2](producto/metodo/investigacion_y_diagnostic/v0.2/LEEME.md) desarrolla N03–N06 con investigación común, instrucciones por nodo, contraste externo/interno, rutina de fuentes/acceso, contratos y siete plantillas vacías. La operación es conversacional y utiliza los registros de FND02; no añade nodos ni otro sistema de gobierno.

N03 define mercado desde la situación de compra, estructura y acceso; distingue universo, condiciones de acceso, capacidad y ventas. Sus fórmulas generales de dimensionamiento conservan población, unidad, periodo, ponderaciones, cobertura y desconocidos. N04 compara segmentos por necesidad, compra, acceso y posibilidad de servir; identifica roles, criterios y eventos de decisión. N05 compara alternativas pertinentes y examina relevancia, distinción, capacidad y razón de adopción de una diferencia.

El [contraste externo e interno](producto/metodo/investigacion_y_diagnostic/v0.2/08_investigacion_externa_y_contraste.md) conecta premisa interna y evidencia externa con razonamiento, conclusión, decisión y campo afectado. Funciona en ambas direcciones: contrastar lo que trae el cliente y derivar implicaciones de hallazgos que no contemplaba. Identifica concordancias, tensiones, condiciones de adecuación y alternativas, conservando origen, comparabilidad y evidencia contraria. No equivale a demostrar aceptación comercial.

La lectura externa cubre las dimensiones pertinentes de mercado, competidores, productos/soluciones, compra, tendencias, acceso y condiciones. El análisis competitivo distingue oferente, solución, disponibilidad, funcionamiento y resultado documentado. Las tendencias distinguen cambio observado, señal, anuncio y previsión, con mecanismo, horizonte y efecto sobre la iniciativa.

La [rutina breve de fuentes y acceso](producto/metodo/investigacion_y_diagnostic/v0.2/09_rutina_de_fuentes_y_acceso.md) sugiere fuentes, herramientas y lugares concretos según las preguntas de la futura prestación. Explica aportación, cobertura, acceso, coste/permiso y alternativa. Separa incorporar una fuente al conjunto de investigación y conectar un servicio por MCP; la conexión se propone cuando añade valor y requiere autoridad antes de ejecutarse. El método no exige proveedor, plataforma ni integración propia.

N06 integra combinaciones coherentes de comprador, oferta, acceso, compra, entrega/cobro y economía. Formula tesis y argumento contrario, examina restricciones y sensibilidad de premisas, y recomienda continuar, condicionar, obtener evidencia adicional, ajustar, aplazar o cerrar. La salida respeta K01 y conserva la diferencia entre recomendación del consultor, decisión del patrocinador y evidencia de mercado.

El [contrato con economía exploratoria](producto/metodo/investigacion_y_diagnostic/v0.2/06_contratos_y_economia_exploratoria.md) define los campos, productores y límites de K08–K12 E. La producción exploratoria no exige una recomendación final previa de N06. FND04 desarrolla los productores N08/N11/N12 y FND05 los de acceso/compra N09/N10. Sus representaciones E conservan población, oferta, trabajo, coste y unidad compatibles sin exigir K07 adoptado. FND06 desarrolla los protocolos y capacidades N13–N17, incluida obtención de evidencia acotada para Diagnostic; no se atribuye preparación efectiva a sus instrucciones ni se ejecutan durante la construcción.

FND03 v0.2 está construido y revisado documentalmente. La revisión completa el tratamiento temporal y el contrato del cruce externo/interno, e incorpora la rutina solicitada por Carlos. No se ha investigado una iniciativa empresarial ni se han ejecutado la metodología o conexiones durante su construcción. La arquitectura y el mandato fundacional se mantienen; el paquete fundacional identifica su integración completa con los demás componentes.

## Componente construido: oferta, entrega y economía

[Oferta, entrega y economía v0.1](producto/metodo/oferta_entrega_y_economia/v0.1/LEEME.md) desarrolla N08/N11/N12 con instrucciones sustantivas, contratos, seis plantillas vacías, fórmulas generales, guía y modelo editable. Las versiones E pueden producirse antes de K06 final; después de una decisión se desarrollan para el alcance habilitado sin convertir hipótesis en evidencia.

N08 conecta necesidad y compra con unidad, configuración, compromiso, exclusiones y finalización. Diseña precio contrastando coste/capacidad/caja propios, alternativas externas comparables y evidencia de valor/compra. Separa referencia, hipótesis, condición autorizada y respuesta observada. Define mecanismo, descuentos, comisiones, condiciones y autoridad sin fijar tarifas ni umbrales universales.

N11 descompone cumplimiento en trabajo, recursos, precedencias, insumos, proveedores, calidad y recepción. Distingue aceptación comercial, inicio, entrega, conformidad, facturación, vencimiento y cobro. Incorpora incidencias, devolución, soporte y renovación pertinentes; una capacidad prevista no se declara disponible.

N12 separa contribución, resultado del perímetro, capacidad y caja. Mantiene unidades, periodos, naturaleza y cobertura de entradas, costes sin duplicación, desconocidos y dominio de fórmulas. El análisis diferencial explicita premisa, mecanismo, efectos conjuntos, condición contraria y umbral de decisión; no transforma capacidad liberada en ventas.

El [modelo general](producto/metodo/oferta_entrega_y_economia/v0.1/08_guia_del_modelo.md) contiene seis hojas: economía de una combinación, umbrales de unidad homogénea, carga por recurso, caja por eventos, existencias y recurrencia. Sus entradas están vacías. La especificación desarrolla además mezcla, lotes/escalones, canal, cohortes y comparaciones con alcance explícito. El libro no automatiza toda variante: una relación adicional material se representa en la fuente editable antes de concluir sobre ella. No se atribuyen planificación temporal, valoración contable, optimización ni validación de aceptación al núcleo de cálculo.

El contraste externo/interno de FND03 se conserva hasta el campo afectado de K08/K11/K12, con comparabilidad, AF derivada y límite. Los huecos pueden activar su rutina de fuentes y acceso; no hay una herramienta ni conexión obligatoria.

La revisión es documental: contenido, contratos, dimensionalidad, referencias, campos vacíos y vistas del libro. No se han introducido parámetros ni ejecutado recorridos de negocio. El comportamiento con entradas en un motor de prestación se comprobará después del cierre de construcción completo. FND04 forma parte del conjunto cerrado; la disponibilidad del libro conserva sus límites y no acredita comportamiento con parámetros.

## Componente construido: posicionamiento, demanda y conversión

[Posicionamiento, demanda y conversión v0.1](producto/metodo/posicionamiento_demanda_y_conversion/v0.1/LEEME.md) desarrolla N07/N09/N10 con instrucciones sustantivas, contratos, relaciones generales, variantes y seis plantillas vacías. La correspondencia conserva el método Go2Rev construido y precisa qué se conserva, adapta, completa o retira de los originales pertinentes de RevOS/GTM efectivamente leídos.

N07 compara marcos de compra por comprensión, alternativas, expectativas, fundamento y capacidad. Recomienda promesa controlable, razones para creer y mensajes por decisión/rol, sin exigir exclusividad a un requisito básico ni atribuir preferencia a la aprobación. El cruce externo/interno permanece visible hasta la afirmación y el campo afectados; una carencia material puede activar la rutina de fuentes y acceso de FND03.

N09 conecta mecanismo, canal, población, acceso, contenido, respuesta y recepción con requisitos, permisos, trabajo y costes. La disponibilidad de acceso, la respuesta y la compra son condiciones distintas. N10 diseña desde decisiones del comprador, con ajuste e intención separados, transiciones verificables, responsable/autoridad/receptor, respuesta, devolución, cierre y traspaso a K11. No se imponen etapas, cuotas de canales, cadencias ni probabilidades universales.

Las reglas distinguen persona, cuenta, ocasión, pedido y unidad económica; preservan cohortes, denominadores, seguimiento incompleto y solapamientos. Todo intento pertinente contribuye a esfuerzo/coste aunque no termine en venta. Las partidas se concilian una sola vez con K12: coste por resultado no se convierte automáticamente en variable por unidad, ni el reparto de una partida compartida crea otro gasto. El diseño conserva capacidad por recurso y calendario, además del total del periodo.

K09/K10 E completan el intercambio de Diagnostic antes de K06 final y sin K07 adoptado. Las variantes directa, intermediada y autoservicio definen decisiones, actores, eventos y traspasos; los consumidores N13–N17 reciben requisitos concretos de medición, protocolos, piezas, comprobación y continuidad. FND06 desarrolla esos consumidores y protocolos; FND07 integra su entrada conversacional y FND08 fija el paquete fundacional completo. FND05 tiene revisión documental del asistente, sin aplicación empresarial, conexiones ni pruebas del método.

## Componente construido: medición, preparación y transferencia

[Medición, preparación y transferencia v0.1](producto/metodo/medicion_preparacion_y_transferencia/v0.1/LEEME.md) desarrolla N13–N17 con instrucciones sustantivas, protocolos de futura prestación, contratos y ocho plantillas vacías. Integra obligaciones, investigación y preparación con los productores FND02–FND05, conservando la arquitectura de diecisiete nodos.

N13 parte de la decisión y define evento, identidad, población/cohorte, fórmula/dominio, fuente, captura, responsable y revisión. Separa observación, referencia, objetivo y umbral; conserva cobertura, desconocidos, madurez, conciliación y cambios de definición. Un reporte o conexión disponibles no acreditan calidad del dato ni acción realizada.

N14 prepara tanto lo necesario para cumplir el encargo como la evidencia requerida por una decisión abierta. Inventaría piezas, medios, dependencias, recursos y criterios; no exige que toda construcción nazca de una prueba. Puede anticiparse a K06 final mediante un protocolo acotado. La investigación externa sigue siendo sustantiva; la obtención directa o actuación comercial se diseña cuando la pregunta y el alcance la justifican, sin ejecutarla durante esta etapa.

N15 traduce el diseño a contenido utilizable, fuentes editables, vistas, guías de tarea y configuraciones aplicadas o pendientes. N16 desarrolla procedimientos distintos para contenido/archivos, cálculo, captura de medidas y uso/traspaso con operador, con criterio previo, rastro, ayuda recibida, defectos y cobertura por variante. Corregir no reescribe la observación; una comprobación parcial no acredita todo el sistema ni resultados de mercado.

N17 contrasta lo entregado con K01, preserva la salida Diagnostic sin exigir construcción posterior, organiza acceso/continuidad y registra recepción con límites. El acompañamiento termina en la condición acordada. El aprendizaje posterior solo se incorpora al producto como regla metodológica autorizada, conservando separados los datos de una prestación.

FND06 está construido y revisado documentalmente por el asistente. Los protocolos están redactados, no ejecutados. FND07 integra entrada conversacional global y capacidades del entorno; FND08 cierra el paquete de implementación y su revisión integrada en el alcance declarado.

## Componente construido: operación conversacional y entorno

[Operación conversacional v0.1](producto/metodo/operacion_conversacional/v0.1/LEEME.md) contiene una [entrada común reutilizable](producto/metodo/operacion_conversacional/v0.1/ENTRADA_GO2REV.md), guía del consultor, mapa de lectura N01–N17, instrucciones de capacidades/alternativas, adaptación del entorno, continuidad/cambios, contrato y tres plantillas vacías. No añade nodos ni otro maestro. Las fuentes sustantivas de FND02–FND06 conservan su autoridad.

La entrada recibe una petición en lenguaje natural y conduce al productor pertinente. El asistente recupera ámbito, decisión, instrucciones y originales materiales; analiza, recomienda, produce y revisa el resultado autorizado. Conserva las decisiones vigentes y solicita solo información exclusiva o autoridad pendiente. Un cambio de sesión no reinicia el encargo ni exige otra recuperación general.

La capacidad se define por acción, entrada, salida, permiso, disponibilidad y criterio de recepción. Leer, localizar, calcular, mostrar un resultado, guardar, configurar y recibir son condiciones distintas. La alternativa debe conservar el contrato o declarar exactamente qué uso queda limitado. La falta de navegación no convierte un análisis interno en Diagnostic integral, y una conexión no otorga evidencia ni autoridad por sí misma.

La adaptación puede cambiar medio, formato o localizador manteniendo unidades, naturaleza de afirmaciones, contratos E/O, criterios y fuentes/versiones. Define persistencia, resolución de conflictos de edición, resultados ambiguos y traslado solicitado sin plataforma propia. Las plantillas agrupan campos CAP/K02/K17 existentes; durante construcción no se completan con registros empresariales.

FND07 tiene revisión documental del asistente. El contrato de neutralidad y el protocolo de comprobación posterior están redactados; no se ha ejecutado el método ni acreditado comportamiento entre proveedores. FND08 consolida paquete, guía de implementación, cobertura y límites de la base fundacional.

## Componente construido: paquete de implementación

El [paquete fundacional v0.1](producto/paquete_fundacional/v0.1/LEEME.md) fija la combinación de arquitectura y componentes, con [guía de implementación](producto/paquete_fundacional/v0.1/01_guia_de_implementacion.md), [alcance y variantes](producto/paquete_fundacional/v0.1/02_alcance_y_variantes.md), composición de cinco conjuntos de entrega, cobertura por nodo, mantenimiento de versiones e inventario/manifiesto. La versión del conjunto identifica contenido exacto sin renumerar la arquitectura aceptada o confundirla con revisiones de prestación.

El conjunto integra 100 fuentes e índices Markdown del producto, incluidas 36 plantillas vacías; definición y libro económico; dos vistas Word y manifiesto. La distribución añade ocho herramientas/guías documentales opcionales y una entrada: 114 archivos en total. Las vistas reúnen implementación/alcance/entregas y arquitectura, respectivamente, y se regeneran desde sus fuentes actuales. No son nuevas fuentes normativas.

La capacidad declarada cubre A/B en B2B, rutas directa, intermediada, autoservicio y combinaciones, con reglas de servicio/proyecto, producto físico, licencia/recurrencia, consumo y ofertas combinadas. Las relaciones económicas generales y protocolos guían su materialización en una prestación; el libro automatiza únicamente su dominio explícito. B2C, operación permanente, desarrollos completos del producto del cliente y trabajos especializados no acordados quedan fuera del alcance inicial.

La entrada operativa y los enlaces del paquete son autónomos de los maestros y del archivo histórico. La procedencia metodológica se conserva en las correspondencias, con sus límites de lectura. Las instrucciones históricas no se vuelven vigentes; el conjunto no añade plataforma, integración instalada ni un plan maestro.

La base está lista para comenzar una implementación autorizada dentro de ese alcance, con información, recursos y medios propios del encargo. El cierre es de construcción y conserva la ausencia de pruebas; no equivale a sistema de un cliente preparado, compatibilidad entre proveedores o resultados comerciales acreditados.

## Conversación y autonomía

La operación del método está definida por la entrada común y las instrucciones sustantivas. El consultor formula tareas en lenguaje natural; las rutas determinan qué fuentes, análisis y decisiones necesita cada tarea. La memoria del chat no es la única copia de una futura prestación.

El método y sus contratos son comunes entre proveedores de LLM. Las instrucciones de adaptación resuelven lectura, investigación, cálculo, escritura y permisos por capacidad, sin cambiar reglas de negocio. Si falta una capacidad, se utiliza una alternativa suficiente o se limita la tarea. No se construye una plataforma, API o sistema propio de enrutamiento para satisfacer este requisito.

La primera versión incluye archivos editables, índice de entregables, versión del conjunto e instrucciones de continuidad. La comprobación de su comportamiento entre entornos se situará después de la construcción completa; durante esta etapa se especifican las capacidades y los procedimientos.

## Responsabilidades y cierre

El consultor responde por análisis y prestación. El asistente investiga, calcula, redacta y propone dentro del alcance. El patrocinador decide compromisos del negocio; el operador aporta disponibilidad y confirma uso; los especialistas resuelven materias que exijan su competencia. La autoridad se asigna por compromiso, sin una aprobación por nodo.

La futura prestación distingue evaluación cerrada, sistema diseñado/preparado, actuaciones reales observadas y entrega parcial o condicionada. El cierre conserva fuentes, decisiones, límites, responsables y siguiente acción. La continuidad posterior termina donde termine el acompañamiento contratado.

El cierre documental de construcción reúne las instrucciones, plantillas, modelos, protocolos y guías del alcance publicado. Su estado sigue siendo teórico y sus pruebas no se han iniciado. El [Plan](Go2Rev_plan_de_trabajo_v0.48_2026-09-11.md) mantiene el cierre y cualquier revisión de construcción que se justifique después.

## Decisiones vigentes

Se conservan el foco inicial B2B, los recorridos A y B, la responsabilidad de diseño y preparación comprobada, la salida Diagnostic prevista desde contratación, el acompañamiento acotado, la autonomía de RevOS y la neutralidad de LLM.

El 10 de septiembre de 2026 Carlos aceptó la arquitectura presentada y estableció la construcción fundacional completa antes de probar el método. Esta decisión gobierna proceso, backlog y todos los formatos del producto. Las referencias metodológicas aportan conceptos y reglas generales; sus contextos de aplicación no forman parte de la base.

Esta versión sustituye la v0.36 e incorpora FND08 y el cierre documental del conjunto fundacional v0.1. Se conservan alcance aceptado, diecisiete nodos, investigación externa sustantiva y estado teórico. Las versiones sustituidas permanecen en el archivo de procedencia; no se ejecuta la metodología ni se reactiva captación por cerrar su construcción.
