# Go2Rev Evidencias y pruebas v0.46

11 de septiembre de 2026 · Registro de construcción y revisión documental

[Plan v0.50](Go2Rev_plan_de_trabajo_v0.50_2026-09-11.md) · [Producto v0.39](Go2Rev_producto_y_metodo_v0.39_2026-09-11.md)

## Estado

Base teórica, sin clientes. La base fundacional v0.1 tiene cierre documental del asistente; esta revisión produce el conjunto 0.3 mediante dos ramas de mejora relacionadas. Carlos autorizó ejecutar la valoración de la revisión externa. Esa autorización no se registra como aceptación del resultado todavía ni como autorización de integración a main.

## Decisiones vigentes

Se conservan B2B, recorridos A y B, salida económica de Diagnostic prevista desde contratación, diseño y preparación operativa comprobada con acompañamiento acotado, autonomía de RevOS y operación conversacional independiente del LLM. Los diecisiete nodos fueron aceptados el 10 de septiembre. Primero se construye íntegramente el método; sus pruebas se sitúan después y no se ejecutan en este trabajo. Los archivos actuales contienen solo conocimiento general, decisiones de producto, plantillas vacías y fórmulas generales.

## Procedencia conservada

La comprobación física previa documentó 629 archivos coincidentes con el manifiesto del consolidado, 62 fuentes RevOS 4.4.0 idénticas al ZIP y 45 archivos GTM Planner 0.3.0 concordantes con los hashes conservados del commit c03068ce187d264caa6f5e9fc172d46907ccbcca. Son resultados de la recuperación anterior; no se repite esa operación ni se atribuye una nueva consulta remota. La duplicación de una semilla cuenta como una sola fuente.

Las [correspondencias](procedencia/LEEME.md) conservan originales y límites de lectura por capacidad. Se trasladan fuera de la carga operativa ocho archivos de procedencia/construcción. Los originales de Back to the plan no se modifican ni se incorporan a la distribución. Los [maestros anteriores](procedencia/maestros_base_v0.1/LEEME.md) se conservan en copias exactas del hito inicial; no son vigentes.

## Revisión externa y tratamiento

Documento recibido: Go2Rev_revision_externa_v0.1_2026-09-11.md, aportado por Carlos desde Descargas. Sus afirmaciones sobre recorridos y cálculos ejecutados por otro modelo son resultados reportados por esa revisión; no son ejecuciones nuestras, no se importan sus datos y no se consideran validación del método. Se contrastan recomendaciones con fuentes actuales antes de adoptarlas.

Se adopta una entrada más práctica, carpetas, glosario, primera pasada, suficiencia por uso, cargas por tarea, claridad de aceptación y mejoras del libro. Se conserva el contenido ya existente sobre hipótesis, evidencia directa acotada y costes de adquisición, sin presentarlo como ausente. No se adopta un recorrido obligatorio con información inventada, cuotas universales de fuentes ni una reescritura completa de arquitectura.

## Resultado de construcción autorizado

| Área | Cambio y fundamento |
|---|---|
| Inicio y continuidad | Guías por entorno, seis carpetas, índice vacío, destinos de resultados y guardado comprobado |
| Lectura | Glosario, núcleo N01–N17, vocabulario del consultor y dieciocho cargas derivadas de originales actuales |
| Análisis | Dimensionamiento, valor/segmento, precio, preguntas/seguimiento y correspondencia de registros reforzados |
| Investigación | Catálogo inicial de portales verificados documentalmente y contraste externo/interno hasta la decisión |
| Suficiencia y autoridad | Profundidad por uso, hipótesis con fundamento, protocolos breves y transición E/O conservando contratos |
| Modelo económico | Definición JSON, generación con biblioteca abierta, guía interna, cero visible y explicación de condiciones; fórmulas previas conservadas |
| Distribución | Procedencia fuera de operación, estructura vacía, guía y arquitectura Word regeneradas, inventario y huellas |

La guía de entornos cita documentación oficial de OpenAI y Anthropic consultada al 11 de septiembre de 2026. El catálogo cita portales de sus editores. Acreditan capacidades publicadas y lugares localizables, no ejecución del método, acceso contratado ni MCP instalado.

La revisión documental conserva cobertura de diecisiete nodos y contratos, campos vacíos y distinción de fuentes/derivados. La puesta en marcha está publicada en la [solicitud de integración 1](https://github.com/RevOps-Studio/Go2Rev/pull/1). El modelo y el conjunto 0.3 están publicados en la [solicitud de integración 2](https://github.com/RevOps-Studio/Go2Rev/pull/2), desde `mejora/modelo-economico-portable`. La implementación está en el commit d06654f, construido sobre el 272e830 de la rama anterior; su solicitud se dirige a esa rama y conserva la dependencia entre mejoras.

La definición del libro v0.2 conserva las fórmulas originales leídas del XLSX vacío. La revisión estática registra 546 fórmulas, 988 entradas vacías, ninguna constante numérica empresarial, ningún cambio en las fórmulas previas, referencias válidas y ausencia de ciclos. Se revisaron las reglas de formato condicional, su asociación a estilos y las validaciones. El cero se muestra mediante formato numérico explícito; no se incorporaron importes para demostrarlo.

Excel abrió el libro vacío en solo lectura y recalculó sus siete hojas sin errores de fórmula; cerró sin guardarlo. Se inspeccionaron las diez páginas de su representación documental y se corrigieron cabeceras, explicación de resúmenes y paginación. Esto acredita integridad y legibilidad del formato vacío, **no comportamiento con parámetros empresariales ni aplicación de Go2Rev**. La generación con openpyxl no calcula resultados y deja señalado el recálculo al abrir.

El libro y las herramientas originales sustituidos se conservan con sus bytes en [procedencia del modelo](procedencia/modelo_base_v0.1/LEEME.md). Los maestros 0.49/0.38/0.45 se conservan en [procedencia de la integración 0.2](procedencia/maestros_integracion_v0.2/LEEME.md). Ninguno es dependencia de producción ni contenido del paquete operativo. La herramienta nueva utiliza solo la definición JSON actual y la biblioteca abierta openpyxl 3.1.5.

La revisión de integración registra 717 enlaces locales resolubles, diecisiete nodos, 37 plantillas y 965 campos de columna Valor vacíos. El paquete contiene 136 archivos y 135 huellas verificadas. Se inspeccionaron las 17 páginas de la guía y las 26 de arquitectura regeneradas. Se normalizan las rutas del renderizador de Word para admitir rutas Windows con espacios.

Se extrajo el paquete en otra carpeta de revisión y se regeneraron desde allí el libro, las dieciocho cargas, la estructura vacía, las dos vistas Word y la distribución. El ZIP reconstruido coincide byte a byte con el distribuido usando las mismas versiones del entorno. Esto comprueba la autonomía de sus dependencias de producción y la integridad en ese entorno; no afirma compatibilidad entre motores de cálculo ni aplicaciones del método. Las seis copias archivadas de esta revisión coinciden con los originales del commit 272e830.

## Límites

Sin entrevistas, campañas, datos empresariales, escenarios ejecutados, conexiones instaladas ni pruebas entre proveedores. La revisión es del asistente y no se presenta como evaluación independiente. Captación y validación comercial siguen diferidas. La base inicial permanece recuperable en GitHub con su etiqueta; main no se modifica por esta construcción.
