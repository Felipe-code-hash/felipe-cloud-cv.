# Responsabilidad Compartida en AWS

Esta tabla resume las responsabilidades de AWS y del cliente (Felipe) para los servicios que se utilizarán durante el proyecto del CV en la nube.

| Servicio | AWS | Felipe |
|----------|-----|---------|
| S3 | Mantiene la infraestructura física, el almacenamiento, la disponibilidad y el funcionamiento del servicio. | Administra el contenido del bucket, los permisos de acceso, la configuración y la seguridad de los datos almacenados. |
| CloudFront | Mantiene la infraestructura global, la red de distribución de contenido (CDN) y la disponibilidad del servicio. | Configura la distribución, define qué contenido se entrega y controla el comportamiento de la caché y los permisos. |
| Lambda | Administra la infraestructura, los servidores, el sistema operativo y el entorno donde se ejecuta el código. | Desarrolla el código, corrige errores, configura la función y define los permisos necesarios para ejecutarla. |
| API Gateway | Mantiene la infraestructura y la disponibilidad del servicio de API. | Diseña la API, configura las rutas, métodos, autorizaciones e integra los servicios necesarios. |
| DynamoDB | Administra la infraestructura, el almacenamiento y la disponibilidad de la base de datos. | Diseña las tablas, administra los datos, controla los permisos y define la estructura de la información. |
| IAM | Mantiene el servicio de administración de identidades y su infraestructura. | Crea y administra usuarios, roles, políticas y aplica el principio de mínimo privilegio. |
| CloudWatch | Mantiene el servicio de monitoreo y la infraestructura que recopila métricas y registros. | Configura alarmas, métricas, registros (logs) y analiza la información para supervisar la aplicación. |

## Conclusión

AWS es responsable de la seguridad **de la nube** (Security OF the Cloud), incluyendo la infraestructura física y la disponibilidad de los servicios.

El cliente es responsable de la seguridad **en la nube** (Security IN the Cloud), incluyendo la configuración de los servicios, los permisos, el código y la información almacenada.
