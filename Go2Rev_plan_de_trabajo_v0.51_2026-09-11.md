# Go2Rev Plan de trabajo v0.51

11 de septiembre de 2026 · Responsable de producto Carlos Estrada

[Producto v0.40](Go2Rev_producto_y_metodo_v0.40_2026-09-11.md) · [Evidencias v0.47](Go2Rev_evidencias_y_pruebas_v0.47_2026-09-11.md)

## Objetivo y estado

Mantener una primera metodología completa, lista para implementar en el primer cliente dentro del alcance declarado. La base v0.1 cerró su construcción documental. El [conjunto 0.4](producto/paquete_fundacional/v0.4/LEEME.md) incorpora las mejoras autorizadas sobre esa base. Go2Rev sigue teórico y sin clientes; esta revisión no ejecuta protocolos de prestación ni acredita resultados comerciales.

La mejora actual está publicada en `mejora/arranque-y-lectura`, desde el commit a6f1d97 de `mejora/modelo-economico-portable`. La puesta en marcha está en la [solicitud 1](https://github.com/RevOps-Studio/Go2Rev/pull/1), el modelo portable en la [solicitud 2](https://github.com/RevOps-Studio/Go2Rev/pull/2) y el arranque/lectura en la [solicitud 3](https://github.com/RevOps-Studio/Go2Rev/pull/3). La tercera mejora depende de la segunda y contiene la implementación a557569. Revisión y decisión de integración pendientes. `main` y la etiqueta `base-fundacional-v0.1` conservan la base inicial.

## Componentes conservados

| Tarea | Componente vigente |
|---|---|
| FND01 | Arquitectura aceptada de diecisiete nodos y correspondencia con once pasos |
| FND02 | Encargo, conocimiento, transferencia A y capacidades B |
| FND03 | Investigación externa/interna y recomendación Diagnostic |
| FND04 | Oferta, entrega y economía; libro v0.2 y generación portable |
| FND05 | Posicionamiento, demanda y conversión |
| FND06 | Medición, preparación, comprobación y transferencia |
| FND07 | Operación v0.3: entrada, invariantes, pasos, lecturas y continuidad |
| FND08 | Paquete v0.4: fuentes, formatos generados, herramientas, guía y distribución |

## Mejora actual construida

| Trabajo | Resultado revisable | Estado |
|---|---|---|
| Lecturas escalonadas | Entrada de 509 palabras; común de 1981; común+nodo entre 2895 y 4080; condiciones de ampliación explícitas | Construido y revisado documentalmente |
| Codificación de formatos | Fuente estructurada, 37 plantillas vacías, primera pasada y 17 esquemas de estructura opcional; campos y matrices conservados | Construido y regenerable |
| Procedimientos y reglas | Pasos breves en 17 nodos, referencias sustantivas conservadas, 20 invariantes comunes | Construido |
| Diagnostic | Hipótesis y conversación breve conectadas desde N04/N06; patrón de fuentes por geografía con semillas reales de España/Portugal | Construido; sin investigación de una empresa ni conexiones instaladas |
| Higiene y mantenimiento | Gobierno de construcción retirado de instrucciones operativas, nombre personal retirado de Word, dependencias, vigencia de entornos e historial del conjunto | Construido |
| Renderizado alternativo | Conversor con LibreOffice y guía de dependencias | Implementado; ejecución Linux/LibreOffice pendiente de un entorno disponible |
| Integración estable | Fuentes, derivados y maestros publicados en la rama dependiente | Carlos revisa el resultado antes de integrar; no se ha modificado main |

## Siguiente decisión y límites

Revisar e integrar las mejoras en orden de dependencia: puesta en marcha, modelo portable y arranque/lectura. La autorización de construir no se registra como aceptación de producto ni como autorización de merge. La revisión actual no requiere un ejercicio empresarial ni pruebas de la metodología.

La comprobación de la ruta Linux/LibreOffice queda pendiente; no se instala un sistema operativo para este cierre ni se atribuye portabilidad ejecutada. El DOCX se genera con las dependencias declaradas y la presentación está revisada con Word en Windows.

Se difiere decidir si el libro necesita un selector simultáneo de escenarios y una relación automática entre periodo y horizonte de caja. El alcance y las relaciones necesarias ya están declarados en su guía; se revisará esa automatización con una necesidad de implementación fundada. El libro no cambia en esta rama.

Captación y validación comercial continúan diferidas. Carlos dedica 4–5 horas semanales a decisiones de producto y arquitectura; el asistente produce el trabajo. Esa dedicación no es capacidad de prestación. Los protocolos se aplicarán solo después de la construcción y dentro del encargo autorizado. Se mantienen tres maestros vivos y se archivan sus versiones sustituidas.
