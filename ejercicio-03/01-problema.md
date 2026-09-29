# Ejercicio 03: Clasificador de Voltaje (Múltiple)

## Variante A: COMPLETAR

## Enunciado

Escribe un programa que solicite al usuario un valor de voltaje y lo clasifique en tres categorías:

- Si el voltaje es **mayor a 220 V**: mostrar `¡Peligro! Voltaje excesivo`
- Si el voltaje está **entre 110 V y 220 V** (incluyendo 110): mostrar `Voltaje dentro del rango`
- Si el voltaje es **menor a 110 V**: mostrar `Voltaje insuficiente`

## Análisis IPO

| Entradas | Proceso | Salidas |
|:---|:---|:---|
| `voltaje` (real) | Comparar voltaje en tres rangos | Mensaje según el rango |

## Orden de entradas

1. Voltaje (real)

## Ejemplo de ejecución
```
Digite el voltaje medido: 250
¡Peligro! Voltaje excesivo
```
```
Digite el voltaje medido: 150
Voltaje dentro del rango
```
```
Digite el voltaje medido: 50
Voltaje insuficiente
```
