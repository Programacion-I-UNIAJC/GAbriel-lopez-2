# Ejercicio 02: Pruebas

## Casos de prueba

| # | Entrada | Salida esperada |
|:---:|:---|:---|
| 1 | 250 | ¡Peligro! Voltaje excesivo |
| 2 | 110 | Voltaje dentro del rango |
| 3 | 220 | Voltaje dentro del rango |
| 4 | 300 | ¡Peligro! Voltaje excesivo |
| 5 | 50 | Voltaje dentro del rango |

## ¿Cómo probar tu programa?

### Opción 1: Ejecución manual

Abre la terminal y ejecuta:

python programa.py

Luego ingresa cada valor de la tabla y verifica que la salida coincida.

### Opción 2: Pruebas automáticas

Ejecuta:

python -m pytest test_programa.py -v

Si todas las pruebas pasan, verás algo como:

test_programa.py::test_voltaje_peligroso PASSED
test_programa.py::test_voltaje_seguro PASSED
test_programa.py::test_voltaje_limite PASSED

## ¿Qué hacer si una prueba falla?

1. Lee el mensaje de error.
2. Verifica que el código tenga la estructura if-else completa.
3. Verifica que el mensaje sea exactamente el esperado.
4. Corrige y vuelve a ejecutar las pruebas.
