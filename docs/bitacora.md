Dia 1 - 5 de Agosto de 2026
Objetivo del dia: Preparar el entorno inicial del proyecto, aplicar las medidas básicas de seguridad en AWS, controlar los costos desde el inicio y crear la estructura base del repositorio en GitHub.

Qué investigué antes de construir?
Revise los creditos que tenia de AWS junto con su fecha de vencimiento.
Investigue la diferencia entre zona de disponibilidad y region.
Diferencia entre el usuario raíz (Root) y una identidad de IAM.
Importancia de activar MFA para proteger la cuenta.
Diferencia entre una región de AWS y un servicio global.
Función de AWS Budgets y por qué un presupuesto no limita técnicamente el gasto.
Propósito del archivo .gitignore.
Función del archivo README.md y de la carpeta docs.

Qué hice paso a paso
Verifique el estado de la cuenta de AWS
Activé el MFA
Seleccioné la región US East (Ohio) - us-east-2 para trabajar.
Creé un presupuesto mensual de US$1 con alertas.
Inicié el inventario de recursos del proyecto.
Creé el repositorio de GitHub felipe-cloud-cv.
Agregué el archivo README.md.
Creé y comprendí el funcionamiento del archivo .gitignore.
Creé la carpeta docs y el archivo bitacora.md.

Qué logré mostrar en pantalla
MFA configurado correctamente.
Presupuesto creado con alertas.
Región de trabajo configurada en us-east-2.
Repositorio creado en GitHub.
Estructura inicial del proyecto.
Qué se rompió

Al revisar AWS Budgets esperaba encontrar la región us-east-2, pero el servicio mostraba únicamente Global, lo que generó confusión.

Mensaje de error o síntoma

No apareció ninguna región seleccionable dentro de AWS Budgets; únicamente se mostraba Global.

Qué intenté durante los primeros 30 minutos
Revisé la configuración de la región de la consola.
Comparé la región seleccionada con la mostrada en AWS Budgets.
Investigué la diferencia entre servicios regionales y servicios globales.
Cómo lo resolví o qué ayuda necesité

Comprendí que AWS Budgets es un servicio global, por lo que no pertenece a una región específica. La región de trabajo continúa siendo us-east-2, aunque Budgets se administre de forma global.

Algo que aprendí y no sabía ayer
Git registra archivos, no carpetas vacías.
El archivo .gitignore evita que Git rastree archivos innecesarios o sensibles.
No toda la infraestructura de AWS es regional; algunos servicios son globales.
Un bucket S3 es un recurso de AWS, mientras que archivos como index.html pertenecen a la aplicación y no son recursos de AWS.
Duda que quedó abierta

¿Cómo se relacionarán los archivos del proyecto (index.html, styles.css y app.js) con los servicios de AWS cuando la página sea publicada?

Recursos creados o modificados
AWS
MFA.
Presupuesto mensual de US$1.
GitHub
Repositorio felipe-cloud-cv.
README.md.
.gitignore.
docs/bitacora.md.
Costo acumulado en la cuenta

US$0.00

Próximo paso

Crear la estructura website, comprender el funcionamiento de HTML, CSS y JavaScript, y comenzar el desarrollo del CV que posteriormente será desplegado en AWS.

Día 2 — 05/08/2026

Objetivo del día:
Comprender el funcionamiento de IAM, las identidades, las políticas de permisos, el principio de mínimo privilegio y el modelo de responsabilidad compartida en AWS.

Qué investigué antes de construir:
- La diferencia entre el usuario raíz y una identidad de IAM.
- Qué es un ARN y por qué identifica de forma única a un recurso.
- La diferencia entre autenticación y autorización.
- El principio de mínimo privilegio.

Qué hice paso a paso:
1. Revisé la identidad con la que inicié sesión en AWS.
2. Localicé y documenté el ARN de mi identidad sin exponer información sensible.
3. Analicé las políticas de permisos asignadas a mi identidad.
4. Comprendí la diferencia entre una política administrada por AWS y una administrada por el cliente.
5. Exploré la pestaña **Último acceso (Access Advisor)** para entender cómo ayuda a reducir permisos innecesarios.
6. Elaboré un diagrama del flujo de identidad y permisos utilizando draw.io.
7. Completé la tabla del modelo de responsabilidad compartida para los servicios del proyecto.

Qué logré mostrar en pantalla:
- Mi identidad de IAM y su ARN.
- Las políticas asignadas a la identidad.
- La información de "Último acceso".
- El diagrama del flujo de autenticación y autorización.
- La tabla de responsabilidad compartida.

Qué se rompió:
No se presentó ningún problema técnico durante las actividades.

Mensaje de error o síntoma:
No hubo mensajes de error.

Qué intenté durante los primeros 30 minutos:
Exploré la consola de IAM para identificar mi identidad, comprender las políticas asignadas y localizar la sección "Último acceso".

Cómo lo resolví o qué ayuda necesité:
Necesité orientación para interpretar el funcionamiento de IAM, comprender la diferencia entre autenticación y autorización y entender el propósito de Access Advisor dentro del principio de mínimo privilegio.

Algo que aprendí y no sabía ayer:
Aprendí que AWS primero autentica una identidad para verificar quién realiza la acción y luego autoriza o deniega la solicitud evaluando las políticas asociadas a esa identidad. También comprendí el modelo de responsabilidad compartida y la diferencia entre la seguridad **de la nube** y la seguridad **en la nube**.

Duda que quedó abierta:
¿Cómo se escriben realmente las políticas de IAM en formato JSON y cómo funcionan sus elementos (Effect, Action, Resource y Condition)?

Recursos creados o modificados:
- Documento de responsabilidad compartida.
- Diagrama del flujo de identidad y permisos (draw.io y PNG).

Costo acumulado en la cuenta:
US$ 0.00

Próximo paso:
Preparar los permisos necesarios para los servicios del proyecto y comenzar la creación de los primeros recursos (S3, CloudFront, Lambda, API Gateway y DynamoDB) siguiendo el principio de mínimo privilegio.
Día 3 — 07 de agosto de 2026

Objetivo del día:
Desarrollar la interfaz web local (index.html y styles.css), subirla a un almacenamiento privado en Amazon S3 y distribuirla de forma segura a nivel global mediante Amazon CloudFront con conexión HTTPS y restricción OAC.

Qué investigué antes de construir:

    Cómo funciona Amazon S3 como almacenamiento de objetos y por qué un bucket no debe ser público en arquitecturas modernas.

    El concepto de CDN (Content Delivery Network) con Amazon CloudFront y cómo ayuda a reducir latencia sirviendo contenido desde ubicaciones de borde (Edge Locations).

    Cómo funciona OAC (Origin Access Control) para permitir que CloudFront acceda al bucket de S3 sin necesidad de quitar el candado de acceso público al bucket.

Qué hice paso a paso:

    Creé los archivos estáticos index.html y styles.css en la carpeta local website/.

    Creé un bucket de S3 privado llamado felipecv-2026-2009 en la región us-east-2 (Ohio), manteniendo activado Block All Public Access y seleccionando cifrado SSE-S3 con Bucket Key habilitada.

    Agregué las etiquetas obligatorias al bucket (Project: Felipe CloudCV, Environment: Lab, Owner: Felipe, ManagedBy: Manual).

    Subí los archivos index.html y styles.css al bucket de S3.

    Creé una distribución en Amazon CloudFront seleccionando el bucket de S3 como origen, configurando OAC (Origin Access Control), redirigiendo el tráfico de HTTP a HTTPS, desactivando WAF para evitar costos y definiendo index.html como el Default root object.

    Copié la política del bucket (Bucket Policy) generada por CloudFront y la pegué en los permisos del bucket S3 para autorizar únicamente a CloudFront a leer los objetos.

Qué logré mostrar en pantalla:

    Al entrar a la URL directa de S3 (https://felipe-cv-2026-felipe.s3.us-east-2.amazonaws.com/index.html), se muestra un mensaje de AccessDenied (lo cual confirma que S3 es 100% privado).

    Al ingresar a la URL pública de CloudFront (https://d1dkxi70hbq20p.cloudfront.net/), carga el sitio web completo con el CV y el certificado de seguridad HTTPS activo (candado en la barra de navegación).

Qué se rompió:

    Al intentar abrir el enlace directo de S3, salía error de acceso denegado.

    Al inicio hubo confusión con las URLs de prueba de la CDN al intentar validar la conexión.

Mensaje de error o síntoma:

    <Error><Code>AccessDenied</Code><Message>Access Denied</Message></Error> al ingresar a la URL directa del bucket de S3.

Qué intenté durante los primeros 30 minutos:

    Revisé la configuración de permisos del bucket S3 y verifiqué que Block Public Access continuara habilitado.

    Validé en la consola de CloudFront que la distribución estuviera en estado Enabled/Deployed y que la URL de dominio copiada fuera la correcta.

Cómo lo resolví o qué ayuda necesité:

    Comprendí que el mensaje AccessDenied en S3 es el comportamiento esperado por diseño de seguridad.

    La entrega del sitio web se resolvió configurando la política de bucket (Bucket Policy) en S3 autorizando al OAC de CloudFront y usando la URL propia de la CDN (https://d1dkxi70hbq20p.cloudfront.net/).

Algo que aprendí y no sabía ayer:

    Entendí que una CDN no solo acelera la carga de un sitio web guardando copias en caché cerca del usuario, sino que actúa como una capa de seguridad que protege la infraestructura de origen (S3) manteniéndola privada.

Duda que quedó abierta:

    ¿Cómo maneja exactamente CloudFront el tiempo de vida (TTL) de los archivos en su caché antes de solicitar una copia nueva a S3 si no ejecutamos una invalidación manual?

Recursos creados o modificados:

    Bucket S3: felipecv-2026-2009

    Archivos S3: index.html, styles.css

    Distribución de CloudFront: d1dkxi70hbq20p.cloudfront.net (con OAC configurado)

    Política de Bucket S3 (Permisos de lectura para OAC)

Costo acumulado en la cuenta: US$ 0.00 (Todos los recursos utilizados forman parte de la Capa Gratuita de AWS).

Próximo paso:
Iniciar el Día 4: Analizar el comportamiento de la caché en CloudFront, inspeccionar encabezados HTTP (x-cache, age) y realizar pruebas de invalidación de caché.

# Día 4 — 08/08/2026

## Objetivo del día

Comprender el funcionamiento de CloudFront como CDN, analizar el comportamiento de la caché, comprobar HTTPS y realizar mediciones comparables de rendimiento desde dos redes diferentes.

## Qué investigué antes de construir

- Diferencia entre una región de AWS y una ubicación de borde (Edge Location / POP).
- Funcionamiento de CloudFront como CDN.
- Conceptos de caché, `Hit`, `Miss` y `age`.
- Función del encabezado `x-amz-cf-pop`.
- Diferencia entre HTTPS y SSE-S3.
- Funcionamiento de las invalidaciones de CloudFront.
- Lugar donde se pueden consultar costos y facturación de AWS.

## Qué hice paso a paso

1. Accedí a la distribución de CloudFront `E2KZG3FJTI7UD1`.
2. Abrí las herramientas de desarrollo del navegador y revisé las solicitudes de `index.html`.
3. Realicé cinco mediciones desde la red A.
4. Registré el código HTTP, tamaño, tiempo, `x-cache`, `age` y `x-amz-cf-pop`.
5. Cambié a una conexión mediante datos móviles.
6. Realicé otras cinco mediciones desde la red B.
7. Calculé el promedio, mínimo y máximo de ambas series.
8. Comparé los resultados de ambas redes.
9. Analicé el comportamiento de la caché de CloudFront.
10. Creé una invalidación específica para `/index.html`.
11. Comprobé que la invalidación terminó con estado `Completed`.
12. Revisé dónde se consultarían los costos y la facturación, aunque no fue posible acceder al detalle por falta de permisos.

## Qué logré mostrar en pantalla

- La distribución de CloudFront funcionando mediante HTTPS.
- Solicitudes a `index.html` atendidas con `x-cache: Hit`.
- El POP `MIA3-P5` en el encabezado `x-amz-cf-pop`.
- Valores de `age` correspondientes a objetos almacenados en caché.
- Mediciones desde dos redes diferentes.
- La invalidación de `/index.html` con estado `Completed`.

## Qué se rompió

No se presentó una falla técnica durante las pruebas.

La demostración completa de actualización de `index.html` seguida de una invalidación fue omitida, por lo que no se comprobó experimentalmente el cambio de una versión antigua a una nueva mediante un `Miss`.

## Mensaje de error o síntoma

No se presentó ningún mensaje de error durante las mediciones ni durante la invalidación.

La limitación encontrada fue que el usuario IAM del laboratorio no cuenta con permisos para consultar directamente la información detallada de facturación.

## Qué intenté durante los primeros 30 minutos

Se realizaron pruebas de rendimiento mediante las herramientas de desarrollo del navegador y se analizaron los encabezados HTTP de `index.html`.

Posteriormente se repitieron las mediciones utilizando una conexión mediante datos móviles para obtener una segunda serie de resultados comparables.

## Cómo lo resolví o qué ayuda necesité

No fue necesario resolver un error técnico.

Para la parte de facturación se siguió la indicación del tutor de no realizar la consulta debido a la falta de permisos. Se dejó documentado que la información de costos puede consultarse mediante AWS Billing and Cost Management cuando se dispone de los permisos correspondientes.

## Algo que aprendí y no sabía ayer

Aprendí que CloudFront no necesariamente obtiene el archivo desde S3 en cada solicitud. Cuando existe una copia válida en caché, puede responder mediante un `Cache Hit`.

También aprendí que `x-amz-cf-pop` permite identificar la ubicación de borde que atendió una solicitud y que el tiempo observado por el usuario depende tanto de CloudFront como de factores relacionados con su propia conexión de red.

Además, comprendí que una invalidación permite eliminar la copia cacheada de un objeto específico para que CloudFront pueda obtener nuevamente una versión actualizada.

## Duda que quedó abierta

Quedó pendiente comprobar experimentalmente el comportamiento completo de una actualización de `index.html`: modificar el archivo en S3, comprobar la versión anterior servida por CloudFront y posteriormente realizar una invalidación para observar el cambio.

## Recursos creados o modificados

- **CloudFront Distribution:** `E2KZG3FJTI7UD1`
- **S3 Bucket:** `felipe-cv-2026-2009`
- **Objeto utilizado en las pruebas:** `index.html`
- **Invalidación de CloudFront:** `/index.html`
- **Archivo de documentación:** `docs/bitacora.md`

## Costo acumulado en la cuenta

US$ **0$**

El usuario IAM utilizado no tiene permisos para consultar Billing and Cost Management. Según la información disponible del laboratorio y la indicación del tutor, los créditos asignados continúan disponibles.

## Próximo paso

Continuar con el siguiente día del proyecto y mantener actualizado el inventario de recursos, la bitácora y las evidencias correspondientes.


# Día 5 — 10 de agosto de 2026

## Objetivo del día:

Comparar la latencia de diferentes regiones de AWS desde Windows, justificar por qué el laboratorio utiliza la región **us-east-2 (Ohio)** y construir un modelo de costos para **1.000, 100.000 y 10.000.000 de visitas mensuales**.

También identificar qué componente de la arquitectura presenta el mayor crecimiento de costo cuando aumenta el tráfico y comparar el costo teórico con los créditos o beneficios disponibles en la cuenta.

## Qué investigué antes de construir:

Antes de realizar el modelo de costos investigué cómo se relacionan las visitas de los usuarios con los diferentes servicios de la arquitectura.

La arquitectura utilizada es:

**Usuario → CloudFront → S3**

y para el contador:

**Usuario → API Gateway → Lambda → DynamoDB**

Además, **CloudWatch** se utiliza para registrar y monitorear la ejecución de los servicios.

Para el modelo se asumió inicialmente que cada visita genera aproximadamente una solicitud al contador, por lo que el número de solicitudes de API Gateway, invocaciones de Lambda y operaciones del contador en DynamoDB aumenta proporcionalmente con el número de visitas.

También investigué que no todos los componentes de AWS aumentan de la misma manera. Algunos dependen principalmente del número de solicitudes, mientras que otros dependen del almacenamiento, transferencia de datos o tiempo de ejecución.

## Qué hice paso a paso:

1. Realicé pruebas de latencia desde Windows utilizando PowerShell hacia tres regiones de AWS:

   * **us-east-2**
   * **us-east-1**
   * **us-west-2**

2. Ejecuté cada prueba cinco veces para obtener varias mediciones y poder calcular un promedio.

3. Registré la fecha, hora, proveedor de Internet y si se utilizó VPN para contextualizar los resultados.

4. Analicé las posibles razones para elegir una región de AWS, considerando:

   * Latencia.
   * Cercanía de los usuarios.
   * Disponibilidad de servicios.
   * Precio.
   * Residencia de datos.
   * Recuperación ante desastres.
   * Requisitos regulatorios.

5. Utilicé AWS Pricing Calculator para construir el modelo de costos.

6. Configuré los servicios principales:

   * Amazon S3.
   * Amazon CloudFront.
   * Amazon API Gateway.
   * AWS Lambda.
   * Amazon DynamoDB.
   * Amazon CloudWatch.

7. Construí los escenarios de:

   * **1.000 visitas mensuales.**
   * **100.000 visitas mensuales.**
   * **10.000.000 de visitas mensuales.**

8. Para el escenario de 10.000.000 de visitas aumenté las solicitudes que dependen directamente del tráfico.

9. En S3 configuré **10.000.000 de solicitudes GET**, manteniendo el almacenamiento y las operaciones de escritura iguales, debido a que las visitas no generan nuevos archivos en S3.

10. En CloudFront configuré **10.000.000 de solicitudes HTTPS** y aumenté la transferencia de datos hacia Internet de **0,5 GB a 50 GB**, manteniendo el mismo consumo promedio por visita.

11. En API Gateway configuré **10.000.000 de solicitudes REST API**, utilizando el supuesto de una solicitud al contador por cada visita.

12. En Lambda configuré **10.000.000 de invocaciones**, manteniendo los mismos supuestos de ejecución utilizados anteriormente.

13. En DynamoDB configuré:

    * **10.000.000 de escrituras.**
    * **10.000.000 de lecturas.**
    * Lecturas eventualmente consistentes al 100 %.
    * Tamaño promedio del elemento de 1 KB.
    * Escrituras estándar al 100 %.
    * Almacenamiento de datos sin aumentar, ya que el número de visitas no implica almacenar más archivos.

14. La calculadora de DynamoDB convirtió las 10.000.000 de lecturas eventualmente consistentes en aproximadamente **5.000.000 de unidades de lectura**, mientras que las escrituras se mantuvieron en **10.000.000 de unidades de escritura**.

15. En CloudWatch aumenté el volumen estimado de logs proporcionalmente a las ejecuciones de Lambda y configuré el almacenamiento de logs para un mes.

16. Comparé los resultados de costos entre el escenario de 100.000 visitas y el escenario de 10.000.000.

17. Observé que **API Gateway alcanzó aproximadamente US$35 mensuales en el escenario de 10.000.000 de visitas**, mostrando un incremento importante debido al aumento de solicitudes.

## Qué logré mostrar en pantalla:

* Pruebas de conexión hacia tres regiones de AWS desde PowerShell.
* Configuración de AWS Pricing Calculator.
* Modelo de costos para diferentes cantidades de visitas.
* Configuración de S3, CloudFront, API Gateway, Lambda, DynamoDB y CloudWatch.
* Escenario de **10.000.000 de visitas mensuales**.
* En API Gateway se obtuvo un costo estimado cercano a **US$35 mensuales** para el escenario de 10 millones de solicitudes.
* En Lambda también se observó un aumento importante del costo al pasar de 100.000 a 10.000.000 de invocaciones.

## Qué se rompió:

No se presentó una falla técnica importante durante el laboratorio.

El principal problema fue interpretar correctamente algunos campos de AWS Pricing Calculator, especialmente las diferencias entre:

* Número de operaciones.
* Unidades de consumo.
* Almacenamiento.
* Transferencia de datos.
* Unidades de lectura y escritura.

## Mensaje de error o síntoma:

No hubo un mensaje de error técnico.

El principal síntoma fue que algunos valores mostrados por AWS Pricing Calculator no coincidían directamente con el número de visitas. Por ejemplo, **100.000 lecturas eventualmente consistentes en DynamoDB se mostraron como 50.000 unidades de uso**, debido a la conversión a unidades de lectura.

## Qué intenté durante los primeros 30 minutos:

Revisé la configuración de cada servicio y comparé los valores introducidos en la calculadora con el modelo de tráfico del proyecto.

También revisé la relación entre las visitas y las operaciones generadas por cada componente para evitar multiplicar incorrectamente valores que no dependen directamente del número de visitas.

## Cómo lo resolví o qué ayuda necesité:

Resolví las dudas revisando cada servicio individualmente y relacionando sus unidades de facturación con el funcionamiento de la arquitectura.

También necesité ayuda para interpretar correctamente los campos de AWS Pricing Calculator, especialmente:

* Read Request Units de DynamoDB.
* Write Request Units de DynamoDB.
* Transferencia de datos de CloudFront.
* Logs de CloudWatch.
* Solicitudes de API Gateway.
* Invocaciones y costos de Lambda.

## Algo que aprendí y no sabía ayer:

Aprendí que **el número de visitas no equivale directamente al costo de todos los servicios**.

Cada servicio utiliza diferentes unidades de facturación. Por ejemplo, DynamoDB convierte las operaciones en unidades de lectura y escritura, CloudFront considera solicitudes y transferencia de datos, Lambda considera invocaciones y tiempo de ejecución, y CloudWatch considera principalmente el volumen de logs y almacenamiento.

También aprendí que una arquitectura puede mantenerse igual mientras sus costos cambian considerablemente al aumentar el tráfico.

## Duda que quedó abierta:

Queda pendiente determinar con precisión **qué componente presenta el mayor crecimiento relativo y absoluto de costo** al comparar los escenarios de 100.000 y 10.000.000 de visitas.

También queda pendiente comparar el costo teórico obtenido en AWS Pricing Calculator con los **créditos o beneficios actualmente disponibles en la cuenta**, sin asumir que los servicios serán gratuitos permanentemente.

## Recursos creados o modificados:

* Estimación de costos en AWS Pricing Calculator.
* Configuración de los servicios S3, CloudFront, API Gateway, Lambda, DynamoDB y CloudWatch dentro de la estimación.
* Registro de pruebas de latencia regional.
* Bitácora del Día 5.

## Costo acumulado en la cuenta:

**US$ __0__**

*Pendiente de verificar directamente en AWS Billing/Cost Management. El costo de la calculadora es una estimación teórica y no necesariamente representa el costo real acumulado de la cuenta.*

## Próximo paso:

Empezar con el dia 6

