On-demand

La tabla utiliza capacidad On-demand, lo que permite que DynamoDB gestione automáticamente la capacidad necesaria según las solicitudes, sin tener que establecer previamente unidades de lectura y escritura.

Esto es adecuado para el laboratorio porque no necesitamos planificar una capacidad fija y el tráfico puede variar.

Actualización atómica

Una actualización atómica permite incrementar el contador directamente en DynamoDB, evitando el patrón de leer el valor, sumarlo en el programa y escribirlo nuevamente.

Esto reduce el riesgo de condiciones de carrera y de perder incrementos cuando varias solicitudes actualizan el contador simultáneamente.
