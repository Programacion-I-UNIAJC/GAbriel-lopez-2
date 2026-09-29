# Ejercicio 05: Promedio de Mediciones

## Variante A: COMPLETAR

## Enunciado

Escribe un programa que solicite al usuario:
1. El número de mediciones a ingresar.
2. Cada una de las mediciones.

Al final, el programa debe calcular y mostrar el **promedio** de las mediciones.

## Análisis IPO

| Entradas | Proceso | Salidas |
|:---|:---|:---|
| `num_mediciones` (entero) | Acumular cada valor en `suma` | `promedio` |
| `valor` (real) | Dividir `suma` entre `num_mediciones` | |

## Orden de entradas

1. Número de mediciones (entero)
2. Cada medición (real)

## Ejemplo de ejecución
```
Digite el número de mediciones: 3
Digite la medición 1: 10
Digite la medición 2: 20
Digite la medición 3: 30
El promedio de las mediciones es: 20.00
```
## Temas evaluados

- Variables
- `input()` y `print()`
- Estructura `for` con `range()`
- Operadores de asignación compuesta (`+=`)

## Instrucciones especiales

En este ejercicio, el archivo `programa.py` **tiene partes marcadas con `___`**.
Tu tarea es completarlas para que el programa funcione correctamente.

Al terminar, ejecuta las pruebas:
```python
    python -m pytest test_programa.py -v
```
