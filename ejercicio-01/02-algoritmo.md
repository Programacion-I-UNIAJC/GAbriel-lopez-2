# Ejercicio 01: Algoritmo

## Pseudocódigo
```
INICIO
Leer voltaje
Si (voltaje > 220) entonces
Escribir "¡Peligro! Voltaje excesivo"
FinSi
FIN
```
## Diagrama de flujo
```mermaid
flowchart TD
    A([INICIO]) --> B[Leer voltaje]
    B --> C{voltaje > 220?}
    C -->|Sí| D[¡Peligro! Voltaje excesivo]
    C -->|No| E([FIN])
    D --> E
```
## Variables utilizadas

| Variable | Tipo | Descripción |
|:---|:---|:---|
| `voltaje` | Real (`float`) | Valor de voltaje medido |

## Explicación

1. El programa solicita al usuario un valor de voltaje.
2. Convierte el valor a número real (`float`).
3. Compara si el voltaje es mayor a 220.
4. Si la condición es verdadera, muestra el mensaje de peligro.
5. Si la condición es falsa, no hace nada.
