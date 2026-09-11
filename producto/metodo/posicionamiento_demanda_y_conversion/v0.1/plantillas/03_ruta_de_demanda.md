# Plantilla de ruta de demanda

Vista generada · Corregir la [definición de campos](../../../esquema/v0.1/plantillas.json), no esta vista. ★ = campo de la plantilla principal: aplicar condición y momento; las piezas auxiliares pueden ser indispensables. Cabecera: identidad, versión, ámbito y K01, autor y fecha, ubicación, estado documental, receptor y uso. Registrar una vez por artefacto; los bloques remiten a ella. FUE, AF y otros registros con identidad propia conservan sus metadatos. La aceptación se localiza en DEC.


Versión 0.1 · K09 · Campos empresariales vacíos

Usar con [acceso y demanda](../02_acceso_y_demanda.md) y [costes, cohortes y capacidad](../04_costes_cohortes_y_capacidad.md). Repetir por ruta pertinente dentro de K09. En E basta una representación razonada con carencias explícitas; no requiere K06 final ni K07 adoptado.

## Propósito, población y mecanismo

<a id="k09-t03-b01"></a>

<!-- bloque: K09.T03.B01 -->
| Campo | Regla | Valor |
|---|---|---|
| ★ Referencia | K09/sección/revisión, ubicación, autor, fecha y estado |  |
| ★ Encargo y combinación | K01/revisión, ámbito, uso E/O y combinación K08/K11/K12 |  |
| ★ Decisión de diseño | Pregunta que resuelve esta ruta y consumidor |  |
| ★ Población de compra | K03/K04: situación, criterio de inclusión/exclusión, territorio y periodo pertinentes |  |
| ★ Unidad e identidad | Persona, cuenta, unidad compradora u ocasión según función; enlace y deduplicación |  |
| ★ Oferta representada | K08 E o diseño vigente; valor descriptivo/AF hipotética si no hay K07 definitivo |  |
| ★ Mecanismo | Cómo se espera pasar de origen/acceso a atención, respuesta y decisión |  |
| ★ Canal y función | Medio utilizado y tarea que cumple; separar mecanismo, canal, pieza y evento |  |
| ★ Alternativas examinadas | Otras rutas y consecuencias comparables de acceso, esfuerzo, coste y tiempo |  |
| ★ Fundamento interno | AF/FUE y CAP de relaciones, medios, contenido y experiencia; dominio de transferencia |  |
| ★ Fundamento externo | AF/FUE de comportamiento, lugares, intermediarios o condiciones de acceso; cobertura y actualidad |  |
| ★ Match y conclusión | Comparabilidad, razonamiento, explicación contraria y campo de ruta afectado |  |

## Acceso, secuencia y recepción

<a id="k09-t03-b02"></a>

<!-- bloque: K09.T03.B02 -->
| Campo | Regla | Valor |
|---|---|---|
| ★ Origen de acceso | Lugar, recurso o relación y qué permite obtener realmente |  |
| ★ Disponibilidad | CAP, estado acreditado, vigencia y requisitos por habilitar; acceso identificado no equivale a disponible |  |
| ★ Autorización | Permiso específico para lectura, tratamiento, contacto, publicación o gasto según la acción |  |
| ★ Carencia de investigación | Pregunta y HUE; fuente/herramienta/acceso suficiente propuesto mediante rutina investigación y Diagnostic |  |
| ★ Secuencia causal | Preparación, exposición/contacto, respuesta, cualificación y recepción pertinentes; ramas y precedencias |  |
| ★ Mensaje y pieza | Propósito, decisión, fundamento y referencia K07; representación descriptiva en E |  |
| ★ Evento de respuesta | Condición observable, fuente y diferencia frente a envío, exposición o compra |  |
| ★ Recepción en K10 | Señal, objeto, receptor, autoridad, acuse, condición de devolución y siguiente decisión |  |
| ★ Ausencia de respuesta | Trabajo, espera, criterio de seguimiento/pausa/cierre y reapertura con permiso pertinente |  |
| ★ Secuencia entre rutas | Dependencias, capacidad, condición de activación y revisión; sin calendario universal |  |

## Esfuerzo, comparación y condición de uso

<a id="k09-t03-b03"></a>

<!-- bloque: K09.T03.B03 -->
| Campo | Regla | Valor |
|---|---|---|
| ★ Cohorte y ventana | Entrada, corte, seguimiento, identidad y cobertura de resultados |  |
| ★ Actividades completas | Preparación, repeticiones, atención y devoluciones incluidos intentos sin resultado; frontera N09/N10 |  |
| ★ Costes y recursos | Referencias a actividad/partida/recurso, unidad, periodo, fuente y carga; no duplicar detalle económico |  |
| ★ Hipótesis de tasas y tiempos | Naturaleza, población, fuente, comparabilidad, madurez e incertidumbre; desconocido sin rango inventado |  |
| ★ Restricción K12 | Capacidad por recurso/franja, coste/caja y dominio; efecto sobre emisión y compromiso |  |
| ★ Recomendación | Ruta y motivo frente a alternativas; mantener, condicionar, adaptar o descartar según uso |  |
| ★ Criterio de revisión | Señal, ventana, umbral fundamentado o relación simbólica y decisión que cambiaría |  |
| ★ Carencias y límites | HUE/CON, consecuencia, productor y alcance consumible |  |
| ★ Autoridad y consumidores | DEC, K06/K10/K12–K17 pertinentes, campo/revisión y disposición de recepción |  |

El [bloque de actividad](05_actividad_coste_y_cohorte.md) conserva el coste completo. El [bloque de recepción](06_recepcion_y_seguimiento.md) detalla el traspaso. Una ruta seleccionada sigue sin acreditar respuesta, ventas o preparación efectiva.

## Aplicabilidad de los bloques

Antes de emitir K09, completar el núcleo de [N09 Elegir rutas de demanda](../../../operacion_conversacional/v0.3/10_primera_pasada.md). Las reglas CONTR, EVAL, USO y de variante de esta plantilla mantienen su momento de exigibilidad. Un bloque condicional se completa cuando afecte al resultado; documentar la condición que lo hace aplicable o su exclusión. Una ausencia material queda localizada y limita el uso dependiente. La cabecera común se registra una vez por artefacto.
