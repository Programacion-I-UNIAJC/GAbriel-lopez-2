# Ejercicio 05: Algoritmo

## Pseudocódigo
```
INICIO
Leer num_mediciones
suma <- 0
Para i <- 1 Hasta num_mediciones Hacer
Leer valor
suma <- suma + valor
FinPara
promedio <- suma / num_mediciones
Escribir promedio
FIN
```

## Diagrama de flujo

```mermaid
flowchart TD
    A([INICIO]) --> B[Leer num_mediciones]
    B --> C[suma = 0]
    C --> D{i <= num_mediciones?}
    D -->|Sí| E[Leer valor]
    E --> F[suma = suma + valor]
    F --> G[i = i + 1]
    G --> D
    D -->|No| H[promedio = suma / num_mediciones]
    H --> I[Escribir promedio]
    I --> J([FIN])
```
## Variables utilizadas
| Variable | Tipo | Descripción |
|:---|:---|:---|
| `num_mediciones` | Entero (`int`) | Cantidad de mediciones a ingresar |
| `suma` | Real (`float`) | Acumulador de las mediciones |
| `valor` | Real (`float`) | Cada medición ingresada |
| `i` | Entero (`int`) | Contador del ciclo |
| `promedio` | Real (`float`) | Resultado final |

## Explicación
El programa solicita el número de mediciones.

1. Inicializa el acumulador suma en 0.

2. Repite num_mediciones veces:

3. Lee un valor.

4. Lo suma al acumulador.

5. Calcula el promedio dividiendo suma entre num_mediciones.

5. Muestra el promedio.
