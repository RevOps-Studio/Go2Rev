# Definición de formatos Go2Rev

Versión 0.1 · Fuente editable documental

[plantillas.json](plantillas.json) define las 37 plantillas: texto de contexto, bloques repetibles, matrices, campos, reglas y condiciones. Sus identificadores estables permiten citar un campo sin repetir su regla. Las plantillas Markdown son vistas vacías regeneradas; el consultor utiliza copias en el encargo y puede agruparlas en documentos legibles.

La definición conserva la regla sustantiva en lenguaje natural. `momento_explicito` localiza EVAL/CONTR/USO cuando aparece en el título o campo; una lista vacía conserva el momento que indique su contexto y el uso del resultado. `exigibilidad: regla_y_contexto` exige leer ambos. Las condiciones no son un programa que decida automáticamente cuándo basta la evidencia.

`nucleo` identifica campos de la plantilla principal. Se interpreta junto a condición, momento y uso: origen y destino son necesarios en A; el bloque de magnitud de K03 se activa cuando informa una decisión; una magnitud decisiva desconocida limita la conclusión. Las plantillas auxiliares pueden ser indispensables. La estrella orienta la lectura, sin sustituir los contratos ni reducirlos a un formulario mínimo.

La cabecera común se registra una vez por artefacto. Los campos de identidad presentes en los bloques remiten a ella; los registros con identidad propia, como FUE y AF, conservan sus metadatos. Una plantilla contiene reglas y espacios vacíos; no contiene resultados empresariales.

## Autoridad de cada fuente

| Contenido | Lugar de edición |
|---|---|
| Reglas transversales | [Invariantes](../../operacion_conversacional/v0.3/13_invariantes.md) |
| Pasos, fundamento, fórmulas y variantes | Instrucciones Markdown de la capacidad |
| Campos y condiciones de plantillas | plantillas.json; las tablas de contratos describen interfaces, no redefinen campos |
| Entrada, salida, consumidor, cierre y condición de lectura | [Rutas](../../operacion_conversacional/v0.3/rutas_de_lectura.json) |
| Vistas de plantilla, primera pasada, cargas y JSON Schema | Generadores; se regeneran después de corregir las fuentes |

## Intercambio opcional

`json_schema/K01.schema.json` a `K17.schema.json` describen una representación textual opcional con una cabecera y colecciones de bloques. Cada bloque admite registros repetidos. Sus propiedades conservan los identificadores de la definición y admiten texto o ausencia explícita. Las matrices mantienen sus columnas.

Estos esquemas comprueban estructura, no verdad, suficiencia, obligatoriedad condicional, cálculo, autoridad ni recepción. Aceptar un JSON vacío estructuralmente correcto no acredita un K completo. El trabajo ordinario puede permanecer en Markdown, Word u otros formatos adecuados; no necesita un validador ni una plataforma propia.

La [herramienta documental](../../../../herramientas/paquete/LEEME.md) regenera las vistas desde estas fuentes. La regeneración comprueba integridad de identidades y cobertura de formatos, sin aplicar la metodología.
