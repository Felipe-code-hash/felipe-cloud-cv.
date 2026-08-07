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
