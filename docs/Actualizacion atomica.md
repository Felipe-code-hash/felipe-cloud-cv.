Se investigó la diferencia entre incrementar el contador mediante una lectura y escritura separadas y realizar una actualización atómica directamente en DynamoDB.
Un método no atómico podría funcionar de la siguiente manera:
1. Lambda lee el valor actual.
2. El programa suma 1.
3. Lambda escribe el nuevo valor.

Esto puede producir una condición de carrera si dos solicitudes ocurren prácticamente al mismo tiempo.

Por ejemplo:
Valor inicial: 5

Visita A → lee 5
Visita B → lee 5

Visita A → suma 1 → 6
Visita B → suma 1 → 6

Resultado: 6

Aunque llegaron dos visitas, una de ellas se perdió.

Con una actualización atómica, DynamoDB puede realizar directamente una operación equivalente a:

visits = visits + 1

De esta manera, las actualizaciones se realizan sobre el valor almacenado sin depender de que el programa lea primero el valor, lo modifique y posteriormente lo escriba.

Por ejemplo:

Valor inicial: 5

Visita A → 6
Visita B → 7

La actualización atómica es más segura para este contador porque reduce el riesgo de perder incrementos cuando existen solicitudes simultáneas.
