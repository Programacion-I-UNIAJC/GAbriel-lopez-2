# Ejercicio 04: Condicional Anidada

## Variante B: CORREGIR ERRORES

## Enunciado

Escribe un programa que solicite al usuario:
1. El tipo de circuito: "C" (corriente continua) o "A" (corriente alterna).
2. El valor del voltaje medido.

El programa debe clasificar el voltaje según el tipo de circuito:

- Si el circuito es **"C" (CC)**:
  - Si el voltaje es **mayor a 24 V**: mostrar `Peligro en CC`
  - Si el voltaje es **menor o igual a 24 V**: mostrar `Voltaje CC seguro`

- Si el circuito es **"A" (CA)**:
  - Si el voltaje es **mayor a 220 V**: mostrar `Peligro en CA`
  - Si el voltaje es **menor o igual a 220 V**: mostrar `Voltaje CA seguro`

## Análisis IPO

| Entradas | Proceso | Salidas |
|:---|:---|:---|
| `tipo_circuito` (texto) | Evaluar tipo primero, luego voltaje | Mensaje según el caso |
| `voltaje` (real) | | |

## Orden de entradas

1. Tipo de circuito (C/A)
2. Voltaje (real)

## Ejemplo de ejecución
```
Digite el tipo de circuito (C/A): C
Digite el voltaje medido: 30
Peligro en CC
```
```
Digite el tipo de circuito (C/A): A
Digite el voltaje medido: 110
Voltaje A seguro
```

## Temas evaluados

- Variables
- `input()` y `print()`
- Estructura condicional anidada

## Instrucciones especiales

En este ejercicio, el archivo `programa.py` **contiene errores intencionales**.
Tu tarea es:
1. Leer el código.
2. Identificar qué líneas están mal o sobran.
3. Corregirlas para que el programa funcione.
4. Verificar ejecutando las pruebas.
