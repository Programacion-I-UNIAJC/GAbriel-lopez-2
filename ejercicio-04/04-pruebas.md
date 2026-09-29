# Ejercicio 04: Pruebas

## Casos de prueba

| # | Entrada | Salida esperada |
|:---:|:---|:---|
| 1 | C, 30 | Peligro en CC |
| 2 | C, 12 | Voltaje CC seguro |
| 3 | A, 250 | Peligro en CA |
| 4 | A, 110 | Voltaje CA seguro |
| 5 | C, 24 | Voltaje CC seguro |

## ¿Cómo probar tu programa?

### Opción 1: Ejecución manual

Abre la terminal y ejecuta:
```
python programa.py
```
Luego ingresa el tipo de circuito y el voltaje según la tabla, y verifica que la salida coincida.

### Opción 2: Pruebas automáticas

Ejecuta:
```bash
python -m pytest test_programa.py -v
```
Si todas las pruebas pasan, verás algo como:
```
test_programa.py::test_cc_peligro PASSED
test_programa.py::test_cc_seguro PASSED
test_programa.py::test_ca_peligro PASSED
test_programa.py::test_ca_seguro PASSED
```
## ¿Qué hacer si una prueba falla?

1. Lee el mensaje de error.
2. Verifica que la estructura anidada esté bien indentada.
3. Verifica que los umbrales sean correctos (24 para CC, 220 para CA).
4. Corrige y vuelve a ejecutar las pruebas.
