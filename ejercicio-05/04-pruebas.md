# Ejercicio 05: Pruebas

## Casos de prueba

| # | Entrada | Salida esperada |
|:---:|:---|:---|
| 1 | 3, 10, 20, 30 | 20.00 |
| 2 | 2, 5, 15 | 10.00 |
| 3 | 1, 7 | 7.00 |
| 4 | 4, 10, 10, 10, 10 | 10.00 |
| 5 | 3, 0, 0, 0 | 0.00 |

## ¿Cómo probar tu programa?

### Opción 1: Ejecución manual

Abre la terminal y ejecuta:
```
python programa.py
```
Luego ingresa el número de mediciones y cada valor según la tabla, y verifica que la salida coincida.

### Opción 2: Pruebas automáticas

Ejecuta:
```
python -m pytest test_programa.py -v
```
Si todas las pruebas pasan, verás algo como:
```
test_programa.py::test_promedio_basico PASSED
test_programa.py::test_promedio_dos PASSED
test_programa.py::test_promedio_uno PASSED
```
## ¿Qué hacer si una prueba falla?

1. Lee el mensaje de error.
2. Verifica que el acumulador `suma` inicie en 0.
3. Verifica que uses `range(num_mediciones)` para el ciclo.
4. Verifica que uses `+=` para acumular.
5. Corrige y vuelve a ejecutar las pruebas.
