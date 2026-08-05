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
