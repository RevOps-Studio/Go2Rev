# Go2Rev Evidencias y pruebas v0.47

11 de septiembre de 2026 · Registro de construcción y revisión documental

[Plan v0.51](Go2Rev_plan_de_trabajo_v0.51_2026-09-11.md) · [Producto v0.40](Go2Rev_producto_y_metodo_v0.40_2026-09-11.md)

## Estado y decisiones conservadas

Base teórica, sin clientes. El conjunto 0.4 incorpora la revisión autorizada de eficiencia de lectura e higiene. La autorización de Carlos permite construir los cambios; no acredita aceptación del resultado ni integración en main. Se conservan B2B, A/B, salida económica de Diagnostic prevista desde contratación, preparación comprobada con acompañamiento acotado, autonomía de RevOS y operación independiente del LLM. La arquitectura de diecisiete nodos fue aceptada el 10 de septiembre. Sus protocolos de prestación no se ejecutan en esta revisión.

## Procedencia

La [correspondencia de originales](procedencia/LEEME.md) conserva las lecturas Go2Rev, RevOS 4.4.0, GTM Planner 0.3.0 del commit c03068ce187d264caa6f5e9fc172d46907ccbcca y semillas. La recuperación previa registró 629 archivos del consolidado, 62 fuentes RevOS coincidentes con su ZIP y 45 archivos GTM concordantes con los hashes conservados. Son comprobaciones anteriores; no se repiten recuperación ni PORT-01 ni se atribuye una nueva lectura de esos originales. Back to the plan permanece congelado y fuera de producción.

La rama `mejora/arranque-y-lectura` parte de a6f1d97, sobre la mejora del modelo portable. Las solicitudes de [puesta en marcha](https://github.com/RevOps-Studio/Go2Rev/pull/1) y [modelo](https://github.com/RevOps-Studio/Go2Rev/pull/2) conservan su dependencia. La publicación de la rama actual está preparada. Los [maestros del conjunto 0.3](procedencia/maestros_integracion_v0.3/LEEME.md) conservan las versiones 0.50/0.39/0.46; los anteriores archivos de procedencia y las distribuciones 0.1–0.3 siguen disponibles.

## Tratamiento de la revisión adicional

Documento recibido: Go2Rev_recomendaciones_v0.4_codificacion_e_higiene.md, aportado desde Descargas. Se contrasta con archivos físicos del producto. Las afirmaciones del documento sobre ejecuciones de otro modelo no se incorporan como pruebas nuestras ni como fuentes empresariales.

| Recomendación | Decisión aplicada |
|---|---|
| A1/A5: reducir carga | Entrada, carga común y nodos con límites conjuntos; extensiones conservan contenido completo y se abren por condición. Un fragmento no sustituye el archivo entero. |
| A2: invariantes | 20 reglas en una fuente común; recordatorios y aplicaciones locales conservan contexto. Se evita usar el número de prohibiciones como criterio de calidad. |
| A3: formatos | JSON estructurado con bloques, matrices, campos, reglas y contexto; generación de 37 plantillas, primera pasada y 17 JSON Schema documentales opcionales. Exigibilidad y suficiencia permanecen sustantivas. |
| A4: pasos | Cuatro pasos iniciales por nodo y referencia sustantiva conservada. Se localizan bloques y condiciones; no se eliminan reglas por un límite de página. |
| B1–B5: higiene y entorno | Retirada de avisos temporales del desarrollo en instrucciones operativas, nombre personal fuera de Word, dependencias explícitas, conversor LibreOffice y vigencia de la guía por plataforma. |
| B6: geografía | Patrón de búsqueda por país y semillas reales de España/Portugal, sin hacer obligatorio un catálogo de herramientas. |
| B7: evidencia intermedia | N04/N06 ya enlazaban suficiencia; ahora sus pasos abren explícitamente hipótesis sustentada y conversación exploratoria breve. |
| B8: jerarquía de fuentes | Se conserva suficiencia por proposición y uso, con contraste independiente cuando es material. No se adopta una jerarquía universal de credibilidad. |
| B9: libro | Sin cambios; automatizaciones de escenarios y bases temporales diferidas. |
| B10: versiones | Secuencia 0.1, 0.2, 0.3 y 0.4 documentada; existe distribución 0.2. |

No se adopta la ejecución de un recorrido con información inventada. La revisión de equivalencia, tamaño, dependencias e integridad utiliza exclusivamente archivos metodológicos vacíos.

## Equivalencia e integridad documental

La importación a la definición estructurada conserva el texto y las celdas de K01/K03 y se extiende a las 37 plantillas. La comparación final contra a6f1d97 conserva los 965 campos Valor vacíos: 960 en tablas Campo/Regla/Valor y cinco en la cabecera del índice. Se mantienen etiquetas, reglas y matrices; el único cambio semántico en celdas retira el perímetro de desarrollo de Go2Rev de la plantilla económica operativa. Las otras retiradas son avisos de gobierno de construcción, documentados en el cambio de archivos.

La estrella señala campos del resultado principal; no vuelve incondicional un bloque. Origen/destino mantiene aplicabilidad A, intención/capacidad mantiene B y magnitud K03 depende de la decisión. El esquema conserva contexto y momento; los JSON Schema solo validan estructura textual, no suficiencia ni permisos. Sus 17 definiciones se comprobaron con jsonschema 4.25.1, sin artefactos empresariales cumplimentados.

Se conservan diecisiete nodos, contratos, fórmulas y desarrollo sustantivo. La regla de transición E/O de la primera pasada anterior se conserva en el contrato de operación. Se revisan 1316 enlaces locales del producto y herramientas, sin ausencias. El paquete contiene 177 archivos y 176 huellas verificadas; excluye maestros, procedencia, dependencias instaladas y temporales.

El libro v0.2 y su definición permanecen idénticos a a6f1d97. SHA256 del libro: `643b757b81c899744fc1d3b353394a918a1b6f84ae5867a77811ac1e7d3b0fbf`. Sus anteriores comprobaciones de fórmulas y apertura vacía no se presentan como nuevas pruebas de aplicación.

## Carga de lectura

| Medida | Conjunto 0.3 | Conjunto 0.4 |
|---|---:|---:|
| Entrada | 1318 | 509 |
| Carga común | 4628 | 1981 |
| Común + N01 inicial | 10126 | 4018 |
| Común + N03 inicial | 16741 | 3438 |

La [medición distribuida](producto/paquete_fundacional/v0.4/lecturas/carga_documental.json) cuenta palabras separadas por espacios, incluidos encabezados, tablas y localizadores. Los totales iniciales de los diecisiete nodos van de 2895 a 4080. No mide tiempo, tokens ni calidad del análisis: las extensiones y los originales de evidencia se leen cuando correspondan. Se comprobó que un límite de lectura excedido provoca rechazo antes de sobrescribir las cargas, en una copia documental aislada.

## Regeneración, presentación y fuentes técnicas

Se extrajo la distribución en otra carpeta y se regeneraron libro, plantillas, primera pasada, esquemas, cargas, estructura vacía, dos Word y ZIP. La distribución reconstruida coincide byte a byte usando las mismas versiones del entorno Windows. Esto acredita autonomía de las dependencias de producción en ese entorno, no comportamiento entre proveedores ni aplicación del método.

Se inspeccionaron todas las páginas de la guía (17) y arquitectura (26), renderizadas con Word en Windows. El nombre personal se ha retirado del generador y no aparece en el contenido distribuido. El renderizador LibreOffice sigue sus [opciones oficiales](https://help.libreoffice.org/latest/en-US/text/shared/guide/start_parameters.html?DbPAR=SHARED), consultadas el 11 de septiembre; usa un perfil temporal y comprueba que el PDF sea nuevo. No había Linux/LibreOffice disponible: se implementa y revisa su ruta, sin atribuir ejecución Linux ni identidad entre motores.

El catálogo utiliza portales de sus editores: INE, ICEX, BORME y contratación pública para España; INE Portugal, AICEP, Registo Comercial y BASE para Portugal. La identificación de INE Portugal está respaldada por publicaciones oficiales; su recuperación automática y la lectura del portal español de contratación fueron limitadas. Los enlaces y límites quedan en el [catálogo](producto/metodo/investigacion_y_diagnostic/v0.2/10_catalogo_inicial_de_fuentes.md). No se leen expedientes de clientes, no se instala MCP ni se atribuyen datos de mercado a esas visitas. La guía de plataformas conserva documentación oficial consultada al 11 de septiembre y declara revisión temporal y por cambio de capacidad.

## Límites del cierre

Revisión documental del asistente; no independiente. Sin clientes, campañas, entrevistas, parámetros empresariales, conexiones instaladas ni pruebas de la metodología. Captación y validación comercial siguen diferidas. La decisión de integrar las ramas corresponde a Carlos sobre el resultado revisable; main permanece estable.
