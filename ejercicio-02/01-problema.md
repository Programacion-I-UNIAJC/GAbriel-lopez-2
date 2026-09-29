# Ejercicio 02: Clasificador de Voltaje (Doble)

## Variante B: CORREGIR ERRORES

## Enunciado

Escribe un programa que solicite al usuario un valor de voltaje y clasifique:

- Si el voltaje es **mayor a 220 V**: mostrar `¡Peligro! Voltaje excesivo`
- Si el voltaje es **menor o igual a 220 V**: mostrar `Voltaje dentro del rango`

## Análisis IPO

| Entradas | Proceso | Salidas |
|:---|:---|:---|
| `voltaje` (real) | Comparar si `voltaje > 220` | Mensaje según el resultado |

## Orden de entradas

1. Voltaje (real)

## Ejemplo de ejecución
```
Digite el voltaje medido: 250
¡Peligro! Voltaje excesivo
```
```
Digite el voltaje medido: 110
Voltaje dentro del rango
```

## Temas evaluados

- Variables
- `input()` y `print()`
- Estructura `if-else`

## Instrucciones especiales

En este ejercicio, el archivo `programa.py` **contiene errores intencionales**.
Tu tarea es:
1. Leer el código.
2. Identificar qué líneas están mal o sobran.
3. Corregirlas para que el programa funcione.
4. Verificar ejecutando las pruebas.
