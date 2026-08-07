# Permisos previstos

## Objetivo

Registrar las acciones que podrían ser necesarias durante el proyecto,
aplicando el principio de mínimo privilegio.

> **Importante:** Esta lista no es una política IAM. Son permisos
> previstos para evaluar y solicitar únicamente cuando sean necesarios.

---

## S3

| Acción | Motivo |
|---|---|
| `s3:GetObject` | Leer archivos del sitio almacenados en S3 |
| `s3:PutObject` | Subir o actualizar archivos del proyecto |
| `s3:ListBucket` | Consultar los objetos existentes en el bucket |

**Alcance esperado:** únicamente el bucket utilizado por el proyecto.

---

## CloudFront

| Acción | Motivo |
|---|---|
| Crear invalidación | Actualizar contenido almacenado en caché cuando sea necesario |

**Alcance esperado:** únicamente la distribución del proyecto.

---

## DynamoDB

| Acción | Motivo |
|---|---|
| `dynamodb:GetItem` | Leer un registro específico de la tabla |
| `dynamodb:PutItem` | Crear registros necesarios para el proyecto |

**Alcance esperado:** únicamente la tabla específica del proyecto.

---

## Lambda

| Acción | Motivo |
|---|---|
| `lambda:InvokeFunction` | Ejecutar una función Lambda necesaria para el proyecto |

**Alcance esperado:** únicamente las funciones utilizadas por el proyecto.

---

## API Gateway

| Acción | Motivo |
|---|---|
| Administrar rutas de la API | Configurar los endpoints necesarios para la aplicación |
| Ejecutar la API | Permitir las solicitudes necesarias de la aplicación |

**Alcance esperado:** únicamente la API del proyecto.

---

## CloudWatch

| Acción | Motivo |
|---|---|
| Leer logs | Revisar el funcionamiento y posibles errores |
| Consultar métricas | Supervisar el comportamiento de los servicios |

**Alcance esperado:** únicamente los recursos de monitoreo del proyecto.

---

## Principio de mínimo privilegio

Los permisos deberán cumplir las siguientes condiciones:

- Otorgar únicamente las acciones necesarias.
- Limitar el acceso a los recursos específicos del proyecto.
- Evitar permisos administrativos generales.
- No crear llaves de acceso para este laboratorio.
- Revisar los permisos antes de utilizarlos.
- Retirar permisos que dejen de ser necesarios.

## Estado

**Planificación:** permisos identificados, todavía no implementados como
una política IAM completa.
