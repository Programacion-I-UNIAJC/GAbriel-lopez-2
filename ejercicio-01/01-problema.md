# Ejercicio 01: Clasificador de Voltaje (Simple)

## Enunciado

Escribe un programa que solicite al usuario un valor de voltaje y determine si es peligroso.

- Si el voltaje es **mayor a 220 V**, el programa debe mostrar: `¡Peligro! Voltaje excesivo`
- Si el voltaje es **menor o igual a 220 V**, el programa **no debe mostrar nada**.

## Análisis IPO

| Entradas | Proceso | Salidas |
|:---|:---|:---|
| `voltaje` (real) | Comparar si `voltaje > 220` | Mensaje `"¡Peligro! Voltaje excesivo"` (si aplica) |

## Orden de entradas

1. Voltaje (real)

## Ejemplo de ejecución
Digite el voltaje medido: 250
¡Peligro! Voltaje excesivo
text
Digite el voltaje medido: 110
(sin salida)

## Temas evaluados

- Variables
- `input()` y `print()`
- Estructura `if` simple
