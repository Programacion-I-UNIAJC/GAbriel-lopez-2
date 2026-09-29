# Ejercicio 03: Pruebas

## Casos de prueba

| # | Entrada | Salida esperada |
|:---:|:---|:---|
| 1 | 250 | ¡Peligro! Voltaje excesivo |
| 2 | 150 | Voltaje dentro del rango |
| 3 | 110 | Voltaje dentro del rango |
| 4 | 50 | Voltaje insuficiente |
| 5 | 220 | Voltaje dentro del rango |

## ¿Cómo probar tu programa?

### Opción 1: Ejecución manual

Abre la terminal y ejecuta:
```bash
python programa.py
```
Luego ingresa cada valor de la tabla y verifica que la salida coincida.

### Opción 2: Pruebas automáticas

Ejecuta:
```bash
python -m pytest test_programa.py -v
```
Si todas las pruebas pasan, verás algo como:
```
test_programa.py::test_voltaje_peligroso PASSED
test_programa.py::test_voltaje_rango PASSED
test_programa.py::test_voltaje_insuficiente PASSED
```
## ¿Qué hacer si una prueba falla?

1. Lee el mensaje de error.
2. Verifica que las condiciones estén en el orden correcto (de mayor a menor).
3. Verifica que uses elif para la segunda condición.
4. Corrige y vuelve a ejecutar las pruebas.
