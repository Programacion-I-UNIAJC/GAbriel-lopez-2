# Ejercicio 04: Algoritmo

## Pseudocódigo
```
INICIO
Leer tipo_circuito
Leer voltaje
Si (tipo_circuito == "C") entonces
Si (voltaje > 24) entonces
Escribir "Peligro en CC"
Sino
Escribir "Voltaje CC seguro"
FinSi
Sino
Si (voltaje > 220) entonces
Escribir "Peligro en CA"
Sino
Escribir "Voltaje CA seguro"
FinSi
FinSi
FIN
```

## Diagrama de flujo

```mermaid
flowchart TD
    A([INICIO]) --> B[Leer tipo_circuito]
    B --> C[Leer voltaje]
    C --> D{tipo_circuito == C?}
    D -->|Sí| E{voltaje > 24?}
    D -->|No| F{voltaje > 220?}
    E -->|Sí| G[Peligro en CC]
    E -->|No| H[Voltaje CC seguro]
    F -->|Sí| I[Peligro en CA]
    F -->|No| J[Voltaje CA seguro]
    G --> K([FIN])
    H --> K
    I --> K
    J --> K
```
## Variables utilizadas
| Variable | Tipo | Descripción |
|:---|:---|:---|
| `tipo_circuito` | Texto (`str`) | Tipo de circuito: "C" o "A" |
| `voltaje` | Real (`float`) | Valor de voltaje medido |

### Explicación
El programa solicita el tipo de circuito y el voltaje.

Si el tipo es "C", evalúa si el voltaje supera 24 V.

Si el tipo es "A", evalúa si el voltaje supera 220 V.

Muestra el mensaje correspondiente según el caso.
