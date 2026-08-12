# CV en AWS

## 1. Descripción del proyecto

Este proyecto consiste en el despliegue de un sitio web de CV personal utilizando servicios administrados de Amazon Web Services (AWS).

El sitio permite consultar el CV desde Internet mediante una distribución de Amazon CloudFront y utiliza un contador de visitas como componente dinámico.

### URL pública

https://d1dkxi70hbq20p.cloudfront.net

### Objetivos del proyecto

* Publicar un sitio web mediante infraestructura cloud.
* Utilizar una arquitectura segura y de bajo costo.
* Implementar HTTPS mediante CloudFront.
* Mantener los archivos del sitio en un bucket S3 privado.
* Implementar un contador de visitas utilizando API Gateway, Lambda y DynamoDB.
* Aplicar el principio de mínimo privilegio mediante IAM.
* Monitorear las ejecuciones de Lambda mediante CloudWatch.
* Analizar rendimiento, seguridad y costos.

---

## 2. Arquitectura

La arquitectura del proyecto está dividida en dos flujos principales.

### Flujo del sitio web

```text
Usuario
   │
   │ HTTPS
   ▼
CloudFront
   │
   │ OAC
   ▼
S3 privado
```

CloudFront funciona como CDN y distribuye los archivos estáticos del CV. El bucket S3 permanece privado y CloudFront accede a los objetos mediante Origin Access Control (OAC).

### Flujo del contador de visitas

```text
Usuario
   │
   │ GET /visits
   ▼
API Gateway
   │
   ▼
Lambda
felipe-cv-counter
   │
   ▼
DynamoDB
felipe-cv-visits
```

Lambda registra la actualización del contador en DynamoDB mediante el permiso `dynamodb:UpdateItem`.

CloudWatch registra información de las ejecuciones de Lambda.

---

## 3. Servicios utilizados y motivo de cada decisión

### Amazon S3

Se utiliza para almacenar los archivos estáticos del sitio web, como HTML y CSS.

El bucket utilizado es:

`felipe-cv-2026-2009`

El bucket permanece privado y no permite acceso público directo.

### Amazon CloudFront

Se utiliza como CDN para distribuir el sitio web desde ubicaciones cercanas a los usuarios y mejorar los tiempos de respuesta.

También proporciona acceso mediante HTTPS.

La política de acceso del comportamiento principal utiliza:

`Redirect HTTP to HTTPS`

CloudFront accede al bucket S3 mediante Origin Access Control (OAC).

### Amazon API Gateway

Se utiliza para proporcionar el endpoint del contador de visitas:

`GET /visits`

API Gateway recibe la solicitud y la dirige hacia la función Lambda correspondiente.

### AWS Lambda

La función:

`felipe-cv-counter`

ejecuta la lógica del contador sin necesidad de mantener un servidor permanentemente activo.

### Amazon DynamoDB

La tabla:

`felipe-cv-visits`

almacena el contador de visitas.

La función Lambda tiene únicamente el permiso necesario para actualizar el elemento:

`dynamodb:UpdateItem`

### Amazon CloudWatch

Se utiliza para observabilidad y registro de las ejecuciones de Lambda.

Se revisaron métricas como:

* Invocations
* Duration
* Errors
* Throttles

También se revisaron los registros `START`, `END` y `REPORT` generados por Lambda.

### AWS IAM

Se utiliza para controlar los permisos de los recursos y aplicar el principio de mínimo privilegio.


## Mejoras adicionales posteriores al proyecto

Después de completar las etapas principales del proyecto, se implementaron mejoras adicionales orientadas a fortalecer la seguridad, observabilidad y control de la infraestructura.

### Observabilidad y monitoreo

Se implementó un dashboard de Amazon CloudWatch para supervisar el comportamiento de la función Lambda `felipe-cv-counter`.

Se añadieron métricas para:

- Invocations
- Errors
- Duration
- Throttles

También se crearon tres alarmas:

| Alarma | Métrica | Estadística | Umbral | Período |
|---|---|---|---|---|
| `felipe-cv-lambda-errors` | Errors | Sum | ≥ 1 | 5 minutos |
| `felipe-cv-lambda-duration` | Duration | Average | ≥ 1000 ms | 5 minutos |
| `felipe-cv-lambda-throttles` | Throttles | Sum | ≥ 1 | 5 minutos |

Las alarmas utilizan el tema de Amazon SNS `felipe-cv-alertas` como destino para las notificaciones.

### Seguridad adicional en CloudFront

Se reforzó la seguridad de la distribución de CloudFront mediante diferentes mecanismos nativos:

- HTTPS para las comunicaciones.
- Origin Access Control (OAC) para mantener el bucket S3 privado.
- AWS Shield Standard para protección DDoS básica.
- Restricción geográfica mediante CloudFront para permitir el acceso únicamente desde Costa Rica.
- Response Headers Policy personalizada denominada `felipe-cv-security-headers`.

La política de headers incluye:

- `Strict-Transport-Security` (HSTS)
- `Content-Security-Policy` (CSP)
- `X-Content-Type-Options: nosniff`
- `Referrer-Policy: strict-origin-when-cross-origin`
- `X-Frame-Options: DENY`

La Content Security Policy permite que el sitio cargue recursos desde su propio origen y permite específicamente las conexiones necesarias hacia la API de API Gateway utilizada por el contador de visitas.

### Protección de API Gateway

Se implementaron controles adicionales sobre la HTTP API `felipe-cv-api`.

#### Throttling

Se configuró limitación de solicitudes para proteger los recursos posteriores de la arquitectura:

- Rate limit: **10 solicitudes por segundo**
- Burst limit: **20 solicitudes**

Cuando se supera el límite establecido, API Gateway puede responder con `429 Too Many Requests`, evitando que un volumen excesivo de solicitudes llegue directamente a Lambda y DynamoDB.

#### CORS

Se configuró CORS para permitir solicitudes desde el dominio de CloudFront utilizado por el CV.

Configuración principal:

- Allowed Origin: dominio de CloudFront del proyecto.
- Allowed Method: `GET`
- Allowed Credentials: `No`
- Max Age: `300 segundos`

Esto limita las solicitudes CORS realizadas desde navegadores a la aplicación web del proyecto.

### Evaluación de AWS WAF

Como parte de las mejoras de seguridad se evaluó la implementación de AWS WAF sobre CloudFront.

Se decidió no habilitar una Web ACL tradicional debido a que AWS WAF utiliza un modelo de precios independiente y el objetivo del proyecto es mantener los costos lo más cercanos posible a $0.

En su lugar, se aprovecharon mecanismos de seguridad nativos y gratuitos de CloudFront, como Shield Standard y las restricciones geográficas.

### Verificación final

Después de implementar las mejoras se verificó que:

- El sitio continúa funcionando correctamente.
- El contador de visitas continúa realizando solicitudes hacia API Gateway.
- Lambda continúa ejecutándose correctamente.
- DynamoDB continúa almacenando el contador.
- Las nuevas políticas de seguridad no interrumpieron el funcionamiento del sitio.
- El throttling quedó configurado para limitar tráfico excesivo hacia la API.

---

## 4. Región y resultados de latencia

La región principal utilizada para los recursos de AWS es:

**US East (Ohio) - ****`us-east-2`**

Durante las pruebas de rendimiento se realizaron mediciones desde diferentes redes.

### Red A

Se realizaron 5 pruebas:

* 418 ms
* 447 ms
* 282 ms
* 293 ms
* 218 ms

Resultados:

* Promedio: **331,6 ms**
* Mínimo: **218 ms**
* Máximo: **447 ms**
* Respuestas HTTP: **200**
* CloudFront: **Hit**
* POP observado: **MIA3-P5**

### Red B

Se realizaron pruebas utilizando otra red.

**Resultados:** 

* **Promedio:** 100.6 ms
* **Mínimo:** 50 ms
* **Máximo:** 174 ms
* **x-cache:** Hit en las cinco mediciones
* **Edge Location (POP):** MIA3-P5

Las pruebas permitieron comparar el comportamiento del sitio desde diferentes condiciones de red.

---

## 5. Cómo desplegar una actualización del sitio

El despliegue utilizado durante el proyecto fue manual.

### Procedimiento

1. Modificar los archivos del sitio localmente.
2. Guardar los cambios.
3. Acceder a Amazon S3.
4. Entrar al bucket `felipe-cv-2026-2009`.
5. Subir los archivos actualizados.
6. Verificar que los archivos estén almacenados correctamente.
7. Acceder al sitio mediante la URL pública de CloudFront.
8. Comprobar que la versión actualizada sea visible.

Si el contenido está almacenado en caché por CloudFront, puede ser necesario esperar a que expire la caché o realizar una invalidación cuando corresponda.

---

## 6. Cómo probar el backend

El backend se puede probar utilizando el endpoint:

`GET /visits`

El flujo esperado es:

```text
GET /visits
      ↓
API Gateway
      ↓
Lambda felipe-cv-counter
      ↓
DynamoDB felipe-cv-visits
```

Para verificar el funcionamiento:

1. Realizar una solicitud `GET` al endpoint.
2. Comprobar que la respuesta sea exitosa.
3. Revisar la ejecución de Lambda.
4. Revisar los logs en CloudWatch.
5. Comprobar que el valor almacenado en DynamoDB se actualice correctamente.

---

## 7. Permisos del rol de Lambda

El rol de ejecución de Lambda fue revisado aplicando el principio de mínimo privilegio.

La función posee permisos relacionados con CloudWatch Logs para registrar sus ejecuciones.

Para DynamoDB posee específicamente:

`dynamodb:UpdateItem`

El recurso está limitado a:

`arn:aws:dynamodb:us-east-2:450653396200:table/felipe-cv-visits`

Por lo tanto, Lambda no tiene permisos generales sobre todas las tablas de DynamoDB.

También se verificó la política basada en recursos de Lambda. API Gateway posee permiso para invocar la función mediante:

`lambda:InvokeFunction`

y la invocación está restringida mediante `AWS:SourceArn` a la API Gateway correspondiente.

---

## 8. Estimación de costos y supuestos

El proyecto fue diseñado procurando mantener los costos lo más bajos posible y evitando pruebas innecesarias que generen consumo.

Las estimaciones realizadas para diferentes cantidades de solicitudes fueron:

| Cantidad de solicitudes | Costo estimado |
| ----------------------: | -------------: |
|                   1.000 |          $0,10 |
|                 100.000 |          $0,72 |
|              10.000.000 |         $75,00 |

Estas cantidades corresponden a escenarios de estimación y no representan necesariamente el costo real acumulado de la cuenta.

El costo real del proyecto debe verificarse directamente en AWS Billing.

**Costo real verificado:** 0$

---

## 9. Errores importantes encontrados y solución

Durante el desarrollo se realizaron diferentes comprobaciones y ajustes de configuración.

Entre los aspectos revisados se encuentran:

* Funcionamiento de Lambda.
* Permisos IAM.
* Integración API Gateway → Lambda.
* Integración Lambda → DynamoDB.
* Acceso privado de S3.
* Integración CloudFront → S3 mediante OAC.
* HTTPS mediante CloudFront.
* Métricas y logs de Lambda.

Uno de los puntos revisados durante la observabilidad fue la ausencia de datos disponibles en algunas métricas de API Gateway (`Count`, `4XXError`, `5XXError` y `Latency`). Debido a que Lambda sí presentaba métricas y registros, y siguiendo la indicación del tutor, esta revisión se dejó sin generar tráfico adicional únicamente para producir datos.

---

## 10. Procedimiento de limpieza

Al finalizar el proyecto, los recursos creados específicamente para la práctica pueden eliminarse siguiendo un orden controlado.

### Recursos a revisar/eliminar

1. CloudFront.
2. Contenido del bucket S3.
3. Bucket S3.
4. API Gateway.
5. Función Lambda.
6. Tabla DynamoDB.
7. CloudWatch Log Group.
8. Roles y políticas IAM creados exclusivamente para el proyecto.

Antes de eliminar cualquier recurso se debe verificar que no sea utilizado por otro componente.

También se debe comprobar que no existan recursos que continúen generando costos.

---

## 11. Método de detección de una caída

Actualmente el proyecto no implementa un sistema permanente de monitoreo externo.

Como método de detección se propone realizar una comprobación periódica de la URL pública mediante un health check HTTP/HTTPS que permita detectar:

* Sitio inaccesible.
* Respuestas HTTP diferentes de 200.
* Problemas de disponibilidad.

Para este proyecto académico se decidió no agregar un servicio permanente de monitoreo con el objetivo de evitar infraestructura y costos adicionales innecesarios.

---

## 12. Seguridad

Se verificaron las principales configuraciones de seguridad del proyecto.

### S3

* Bucket privado.
* Object Ownership configurado como imposición de propietario del bucket.
* ACL deshabilitadas.
* Acceso mediante CloudFront.
* Permiso `s3:GetObject` limitado al servicio CloudFront.
* Política restringida mediante `AWS:SourceArn`.

### CloudFront

* Origin apuntando al bucket S3.
* Origin Access Control configurado.
* HTTP redirigido a HTTPS.

### Lambda

* Permisos de ejecución revisados.
* Acceso a DynamoDB limitado a `dynamodb:UpdateItem`.
* Recurso limitado a `felipe-cv-visits`.
* Invocación desde API Gateway restringida mediante `SourceArn`.

### API Gateway

* Ruta `GET /visits`.
* Throttling de cuenta revisado.
* La ruta no utiliza autorizador porque el contador debe ser accesible públicamente desde el CV.

---

## 13. Observabilidad

CloudWatch se utilizó para revisar el comportamiento de Lambda.

Se analizaron:

* Invocations.
* Duration.
* Errors.
* Throttles.
* Logs de ejecución.

Los logs contienen registros `START`, `END` y `REPORT`, permitiendo verificar que las ejecuciones se están registrando correctamente.

El grupo de logs utilizado es:

`/aws/lambda/felipe-cv-counter`

La retención actual de los logs se encuentra configurada como:

**No vence nunca**

Esta configuración queda identificada como un punto susceptible de optimización para controlar el almacenamiento a largo plazo.

---

## 14. Recursos principales

| Servicio    | Recurso                         |
| ----------- | ------------------------------- |
| S3          | `felipe-cv-2026-2009`           |
| CloudFront  | `E2KZG3FJTI7UD1`                |
| API Gateway | `felipe-cv-api`                 |
| API Gateway | `GET /visits`                   |
| Lambda      | `felipe-cv-counter`             |
| DynamoDB    | `felipe-cv-visits`              |
| CloudWatch  | `/aws/lambda/felipe-cv-counter` |
| Región      | `us-east-2`                     |

---

## 15. Qué haría diferente con más tiempo

Con más tiempo se podrían implementar mejoras como:

* Automatizar el despliegue mediante un pipeline CI/CD.
* Implementar un sistema permanente de monitoreo y alertas.
* Mejorar la automatización de invalidaciones de CloudFront.
* Automatizar pruebas del backend.
* Utilizar infraestructura como código.
* Establecer una política de retención de logs optimizada.
* Incorporar métricas y dashboards personalizados.
* Automatizar la limpieza de recursos de pruebas.

Estas mejoras permitirían reducir tareas manuales, aumentar la observabilidad y facilitar el mantenimiento del proyecto a largo plazo.
