### 6. Comparación de resultados

Se realizaron cinco mediciones desde la red A y cinco desde la red B utilizando las herramientas de desarrollo del navegador y observando el tiempo de respuesta de `index.html`.

#### Red A.

- **Promedio:** 331.6 ms
- **Mínimo:** 218 ms
- **Máximo:** 447 ms
- **x-cache:** Hit en las cinco mediciones
- **Edge Location (POP):** MIA3-P5

#### Red B.

- **Promedio:** 100.6 ms
- **Mínimo:** 50 ms
- **Máximo:** 174 ms
- **x-cache:** Hit en las cinco mediciones
- **Edge Location (POP):** MIA3-P5

#### Comparación

La red B presentó un tiempo promedio de **100.6 ms**, mientras que la red A presentó un promedio de **331.6 ms**. Esto representa una reducción aproximada del **69.7 %** en el tiempo promedio de respuesta.

Sin embargo, estos resultados no permiten concluir que CloudFront sea por sí solo la causa de la mejora. Ambas pruebas fueron atendidas por la misma ubicación de borde (`MIA3-P5`), por lo que la diferencia puede estar relacionada con las características de cada conexión de red, la latencia, la congestión, el navegador y el comportamiento de la caché.

Además, en las mediciones de la red B se observaron respuestas `304 Not Modified`, mientras que las mediciones de la red A fueron `200`. Esto también puede influir en los tiempos registrados.

Por lo tanto, las mediciones permiten comprobar que **el rendimiento percibido puede variar considerablemente según la red utilizada por el cliente**, pero no permiten atribuir toda la diferencia exclusivamente a CloudFront.

#### Variables que pueden alterar el resultado

- Tipo y calidad de la conexión a Internet.
- Latencia entre el cliente y la infraestructura de red.
- Congestión de la red.
- Velocidad y estabilidad de la conexión móvil o Wi-Fi.
- Caché del navegador.
- Caché de CloudFront.
- Ubicación del usuario.
- Edge Location utilizada por CloudFront.
- Carga de trabajo de la red en el momento de realizar la prueba.
- Estado de la conexión entre CloudFront y el origen S3.
