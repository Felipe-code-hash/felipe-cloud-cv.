# MEJORAS ADICIONALES POSTERIORES AL PROYECTO

Una vez finalizadas las etapas principales del proyecto, se realizaron mejoras adicionales con el objetivo de fortalecer la observabilidad, seguridad y control de la arquitectura AWS, manteniendo como prioridad evitar costos innecesarios.

## 1. Mejoras de observabilidad con CloudWatch

Se creó un dashboard personalizado de Amazon CloudWatch para supervisar el comportamiento de la función Lambda `felipe-cv-counter`.

Se añadieron las métricas:

- Invocations
- Errors
- Duration
- Throttles

Esto permite visualizar el comportamiento de la función y detectar problemas de errores, tiempos elevados de ejecución o limitaciones de concurrencia.

### Alarmas configuradas

Se crearon tres alarmas para complementar el monitoreo:

| Alarma | Métrica | Estadística | Condición | Período |
|---|---|---|---|---|
| `felipe-cv-lambda-errors` | Errors | Sum | ≥ 1 | 5 minutos |
| `felipe-cv-lambda-duration` | Duration | Average | ≥ 1000 ms | 5 minutos |
| `felipe-cv-lambda-throttles` | Throttles | Sum | ≥ 1 | 5 minutos |

Las tres alarmas utilizan el tema SNS `felipe-cv-alertas` para el envío de notificaciones.

Las suscripciones por correo creadas para el tema quedaron pendientes de confirmación, por lo que las notificaciones por email requieren confirmar previamente el punto de enlace.

---

## 2. Mejoras de seguridad en CloudFront

Se evaluó la incorporación de AWS WAF para proteger la distribución de CloudFront frente a amenazas web.

Debido a que AWS WAF tradicional utiliza un modelo de cobro independiente y el objetivo del proyecto es mantener los costos lo más cercanos posible a $0, se decidió no habilitar una Web ACL tradicional.

En su lugar, se aprovecharon mecanismos de seguridad nativos y gratuitos de CloudFront.

### Restricción geográfica

Se configuró una restricción geográfica mediante una lista de permitidos (`Allow list`) para **Costa Rica**.

Esto limita el acceso al CV a solicitudes provenientes de Costa Rica.

### Protección DDoS

Se verificó que la distribución de CloudFront cuenta con **AWS Shield Standard**, que proporciona protección DDoS básica de forma automática.

### Response Headers Policy

Se creó la política personalizada:

`felipe-cv-security-headers`

y se asoció al comportamiento de CloudFront.

La política incorpora:

- `Strict-Transport-Security` (HSTS)
- `Content-Security-Policy` (CSP)
- `X-Content-Type-Options: nosniff`
- `Referrer-Policy: strict-origin-when-cross-origin`
- `X-Frame-Options: DENY`

La CSP fue configurada para permitir los recursos locales del CV y las conexiones necesarias hacia la API de API Gateway utilizada por el contador de visitas.

Después de aplicar la política se verificó que el sitio continuara funcionando correctamente.

---

## 3. Protección de API Gateway

Se implementaron controles adicionales sobre la HTTP API `felipe-cv-api`.

### Throttling

Se configuró limitación controlada de tráfico en la etapa `$default`:

- Límite de tasa: **10 solicitudes por segundo**
- Límite de ampliación (Burst): **20 solicitudes**

Esto permite controlar una cantidad excesiva de solicitudes simultáneas y evitar que un volumen elevado de tráfico llegue directamente a Lambda y DynamoDB.

Cuando se supera el límite, API Gateway puede responder con `429 Too Many Requests`.

### CORS

Se configuró CORS para restringir las solicitudes realizadas desde navegadores.

La API permite solicitudes desde el dominio de CloudFront utilizado por el CV:

`https://d1dkxi70hbq20p.cloudfront.net`

Configuración principal:

- Allowed Origin: dominio de CloudFront
- Allowed Method: `GET`
- Allowed Headers: sin encabezados adicionales
- Credentials: `No`
- Max Age: `300 segundos`

Después de aplicar la configuración se verificó que el contador continuara funcionando correctamente.

---

## 4. Verificación final

Después de implementar las mejoras adicionales se realizaron pruebas para comprobar que la aplicación continuara funcionando correctamente.

Se verificó que:

- El CV continúa siendo accesible mediante CloudFront.
- HTTPS continúa funcionando.
- El contador de visitas continúa realizando solicitudes a API Gateway.
- API Gateway continúa invocando Lambda.
- Lambda continúa interactuando con DynamoDB.
- CORS no impide el funcionamiento del contador.
- La CSP no bloquea los recursos necesarios.
- Los nuevos headers de seguridad no afectan la presentación del sitio.
- El throttling queda configurado para controlar tráfico excesivo.
- Las alarmas de CloudWatch permanecen asociadas al monitoreo de Lambda.

Estas mejoras se realizaron como una etapa adicional posterior a la finalización de los nueve días principales del proyecto, con el propósito de fortalecer la arquitectura y demostrar prácticas adicionales de seguridad, observabilidad y control de tráfico.



## Actividad adicional — Actualización y mejora del CV en la nube

Como actividad adicional al desarrollo del proyecto, se realizó una actualización del contenido y diseño del CV web, con el objetivo de mejorar su presentación profesional y reflejar nuevos avances obtenidos durante el desarrollo del proyecto.

Se modificó el frontend utilizando **HTML y CSS**, manteniendo el diseño visual original y la estructura general de la página. Se incorporó una nueva sección de **Experiencia profesional**, donde se registró la pasantía realizada en **Arkkosoft del 3 al 14 de agosto de 2026**, relacionada con el desarrollo del CV en la nube y el uso de servicios de AWS.

También se agregó una sección de **Certificaciones**, incorporando las certificaciones obtenidas mediante **Cisco Networking Academy**: Introducción al Internet de las Cosas, CSS Essentials y HTML Essentials. Para mejorar la presentación visual, se utilizaron los badges oficiales proporcionados mediante Credly y se organizaron dentro de una carpeta `badges/` en el proyecto.

Antes de actualizar el sitio público, se realizaron pruebas localmente en Visual Studio Code para comprobar que los nuevos elementos se mostraran correctamente, que el diseño responsive continuara funcionando y que el contador de visitas mantuviera su estructura y funcionamiento.

Posteriormente, se actualizaron los archivos correspondientes en **Amazon S3**, incluyendo el nuevo `index.html`, `styles.css` y los tres badges. No fue necesario modificar `app.js`, Lambda, API Gateway ni DynamoDB, debido a que la lógica del contador de visitas no sufrió cambios.

Finalmente, se realizó una **invalidación selectiva de CloudFront** para los archivos modificados y agregados:

```text
/index.html
/styles.css
/badges/iot-badge.png
/badges/css-essentials-badge.png
/badges/html-essentials-badge.png
```

Se decidió realizar una invalidación específica en lugar de utilizar `/*`, evitando eliminar innecesariamente de la caché otros archivos que no habían sido modificados.

### Resultado

El CV quedó actualizado y disponible mediante CloudFront, incorporando la experiencia profesional de la pasantía, las certificaciones de Cisco Networking Academy y sus respectivos badges, manteniendo al mismo tiempo la arquitectura cloud y las funcionalidades previamente implementadas.

### Aprendizaje

Esta actividad permitió reforzar el proceso de actualización de aplicaciones web desplegadas en la nube, comprendiendo la relación entre los archivos estáticos almacenados en **S3**, la distribución mediante **CloudFront** y la necesidad de utilizar invalidaciones de caché cuando se actualiza contenido. También permitió practicar la organización de recursos estáticos y la integración de nuevos elementos visuales sin afectar los componentes funcionales existentes.

