# Oferta, entrega y economía

Versión 0.1 · FND04 · N08, N11 y N12 · Construcción fundacional

Este componente contiene instrucciones sustantivas, contratos, plantillas vacías y un modelo editable para una futura prestación. La base es teórica. Durante su construcción se revisan contenido, interfaces, fórmulas y legibilidad; la metodología se probará después de completar Go2Rev.

## Lectura por tarea

| Tarea del consultor en una prestación | Instrucción | Salida |
|---|---|---|
| Representar una oferta o revisar su precio | [Oferta y precio](01_oferta_y_precio.md) | K08, con unidad, compromisos y condiciones |
| Diseñar cómo cumplir, aceptar, facturar y cobrar | [Entrega y cobro](02_entrega_y_cobro.md) | K11, trabajo, traspasos, recursos y eventos |
| Examinar sostenibilidad y restricciones | [Economía y capacidad](03_economia_y_capacidad.md) y [fórmulas](04_formulas_y_dominio.md) | K12 delimitado y reproducible |
| Resolver diferencias por tipo de oferta o canal | [Variantes](05_variantes_de_oferta_y_operacion.md) | Reglas pertinentes incorporadas a K08/K11/K12 |
| Comparar cambios y emitir una recomendación | [Comparación y umbrales](06_comparacion_y_umbrales.md) | Razón de preferencia, límite y evidencia necesaria |
| Recibir entradas o revisar un cambio | [Contratos](07_contratos_y_revision.md) | Consumo admitido, limitado o devuelto por campo |
| Preparar la fuente de cálculo | [Guía del modelo](08_guia_del_modelo.md) | Libro y documentación de K12 coherentes |

El asistente comienza por la decisión solicitada, recupera K01 y las versiones de los campos necesarios, construye el análisis y presenta recomendación, alternativas y límites. El consultor revisa calidad; quien tiene autoridad decide compromisos. No se pide al cliente que diseñe el análisis ni resuelva cálculos para poder redactarlo.

## Entrada exploratoria y diseño

Para Diagnostic, N08 E parte de K02/K04/K05, N11 E descompone esa oferta y N12 E recibe la combinación con acceso y compra E. **K06 final no es prerrequisito de esas representaciones.** Se aplica el [intercambio exploratorio de Diagnostic](../../investigacion_y_diagnostic/v0.2/06_contratos_y_economia_exploratoria.md). Tras una decisión de continuidad, las mismas piezas se desarrollan para el alcance habilitado; cambiar su uso no aumenta su evidencia.

El [contraste externo e interno](../../investigacion_y_diagnostic/v0.2/08_investigacion_externa_y_contraste.md) aporta conclusiones a oferta, condiciones, costes, recursos y plazos. Una referencia publicada sirve para analizar una hipótesis; su transformación en un parámetro propio exige explicar comparabilidad, mecanismo, fuente y límite. Los huecos materiales activan la [rutina de fuentes y acceso](../../investigacion_y_diagnostic/v0.2/09_rutina_de_fuentes_y_acceso.md), incluida la posible propuesta de MCP. Este componente no exige conexiones.

## Archivos editables

- [Ficha de oferta](plantillas/01_oferta.md).
- [Cumplimiento y traspaso](plantillas/02_entrega_y_traspaso.md).
- [Partidas y recursos](plantillas/03_partidas_y_recursos.md).
- [Eventos y condiciones de cobro/pago](plantillas/04_eventos_de_caja.md).
- [Contrato y conclusión del modelo](plantillas/05_modelo_y_conclusion.md).
- [Comparación y umbral](plantillas/06_comparacion.md).
- [Modelo general vacío](modelo/Go2Rev_modelo_economico_v0.1.xlsx).

Las plantillas son secciones agrupables, no siete entregables obligatorios. Los IDs y la semántica son los del [diccionario común](../../encargo_y_conocimiento/v0.1/03_contratos_y_diccionario.md). La especificación de fórmulas es independiente del proveedor y del libro; permite conservar el cálculo en otro medio suficiente sin alterar el contrato.

La [correspondencia de fuentes](09_fuentes_y_correspondencia.md) conserva procedencia y límites de reutilización. No es una dependencia de operación. El estado global y las siguientes tareas pertenecen exclusivamente al Plan vigente de la raíz.
