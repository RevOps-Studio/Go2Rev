# Go2Rev Paquete fundacional

Versión de conjunto 0.2 · 11 de septiembre de 2026 · paquete de implementación

Esta es la entrada del producto Go2Rev para preparar su primera implementación. Reúne la arquitectura de diecisiete nodos, las instrucciones sustantivas, los contratos, treinta y seis plantillas de método y un índice vacío de encargo y el modelo económico editable. La base está construida y revisada documentalmente por el asistente. Su estado es teórico: no ha habido clientes ni pruebas de la metodología. La versión identifica contenido disponible, no resultados de uso.

## Empezar

El consultor comienza por la [guía de implementación](01_guia_de_implementacion.md), que explica cómo encuadrar el servicio y conducir Diagnostic, Design y Despliegue. El [alcance y las variantes](02_alcance_y_variantes.md) delimitan qué se puede comprometer. La [composición de entregables](03_entregables_y_recepcion.md) explica cómo convertir el trabajo en entregas recibibles.

Para trabajar con un asistente, proporcionar la [entrada común Go2Rev](../../metodo/operacion_conversacional/v0.2/ENTRADA_GO2REV.md) y acceso a las fuentes pertinentes del producto. El [mapa de tareas](../../metodo/operacion_conversacional/v0.2/02_rutas_y_lectura.md) abre las instrucciones de N01–N17. No se necesita aprender los códigos ni cargar todo el paquete en cada conversación. El consultor puede utilizar directamente las mismas instrucciones sin LLM.

## Qué contiene el paquete

| Componente | Versión base | Entrada |
|---|---|---|
| Arquitectura aceptada y correspondencia con once pasos | 0.2 | [Arquitectura](../../arquitectura/v0.2/01_arquitectura_metodologica.md) |
| Encargo y conocimiento | 0.1 | [N01 y N02](../../metodo/encargo_y_conocimiento/v0.1/LEEME.md) |
| Investigación y recomendación Diagnostic | 0.2 | [N03–N06](../../metodo/investigacion_y_diagnostic/v0.2/LEEME.md) |
| Oferta, entrega y economía | 0.1 | [N08, N11 y N12](../../metodo/oferta_entrega_y_economia/v0.1/LEEME.md) |
| Posicionamiento, demanda y conversión | 0.1 | [N07, N09 y N10](../../metodo/posicionamiento_demanda_y_conversion/v0.1/LEEME.md) |
| Medición, preparación y transferencia | 0.1 | [N13–N17](../../metodo/medicion_preparacion_y_transferencia/v0.1/LEEME.md) |
| Operación conversacional y entorno | 0.2 | [Entrada y continuidad](../../metodo/operacion_conversacional/v0.2/LEEME.md) |
| Integración y uso del conjunto | 0.2 | Esta guía y sus archivos asociados |

La versión del conjunto fija la combinación exacta de archivos. Las versiones base de los componentes no se hacen iguales entre sí ni se confunden con una revisión de prestación. El [inventario](INVENTARIO.md) identifica todos los archivos distribuidos; el [manifiesto](manifiesto.json) conserva tamaño, función y huella de su contenido. Las reglas de actualización están en [versiones y mantenimiento](05_versiones_y_mantenimiento.md).

## Fuentes y vistas

Los Markdown son fuentes metodológicas editables. El [libro vacío](../../metodo/oferta_entrega_y_economia/v0.1/modelo/Go2Rev_modelo_economico_v0.1.xlsx) es el soporte editable de cálculo para una prestación; su definición general y dominio se conservan junto a él. La [guía en Word](Go2Rev_guia_de_implementacion_v0.2.docx) reúne guía, alcance y composición de entregas. La [vista de arquitectura](../../arquitectura/v0.2/Go2Rev_arquitectura_metodologica_v0.2.docx) facilita su lectura. Corregir primero las fuentes y regenerar las vistas; una compilación no adquiere autoridad propia.

Las correspondencias de fuentes conservan procedencia y límites de lectura. Los originales históricos no se distribuyen ni son necesarios para aplicar estas instrucciones. Tampoco lo son los tres maestros de desarrollo. La [cobertura e integración](04_cobertura_e_integracion.md) muestra cómo los componentes satisfacen la arquitectura y sus interfaces.

## Condición de uso

Listo para implementar significa que la metodología general necesaria para comenzar una prestación está construida. Cada encargo deberá aportar su autoridad, información exclusiva, recursos y medios; el asistente producirá la investigación y el diseño propios. Las comprobaciones previstas se realizarán dentro del alcance autorizado y podrán formar parte de la primera implementación autorizada. Este paquete no inicia esa actividad por sí mismo.

Las fuentes generales y sus campos vacíos se conservan intactos durante el uso. La información, decisiones y observaciones de cada prestación se guardan en su espacio separado. El acompañamiento y los derechos de uso se rigen por el encargo; no se exige contratar RevOS ni adoptar una plataforma o proveedor de LLM.


## Preparación práctica

1. Abrir [uso por entorno](../../metodo/operacion_conversacional/v0.2/09_uso_por_entorno.md) y [glosario](../../metodo/operacion_conversacional/v0.2/00_glosario.md).
2. Preparar una raíz del encargo con la [estructura vacía](Go2Rev_estructura_vacia_v0.2.zip); recuperar la existente si es una continuación.
3. Cargar [INICIO](lecturas/CARGA_INICIO.md) y la lectura del nodo pertinente, comenzando por [N01](lecturas/CARGA_N01.md) para un nuevo encargo. Las cargas son compilaciones derivadas, con originales y dependencias identificados.
4. Aplicar [primera pasada](../../metodo/operacion_conversacional/v0.2/10_primera_pasada.md), guardar y actualizar el índice. Un chat sin escritura entrega archivos para incorporar al espacio persistente.
