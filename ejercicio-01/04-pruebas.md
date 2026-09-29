# Ejercicio 01: Pruebas

## Casos de prueba

| # | Entrada | Salida esperada |
|:---:|:---|:---|
| 1 | 250 | ¡Peligro! Voltaje excesivo |
| 2 | 110 | (sin salida) |
| 3 | 220 | (sin salida) |
| 4 | 300 | ¡Peligro! Voltaje excesivo |
| 5 | 50 | (sin salida) |

## ¿Cómo probar tu programa?

### Opción 1: Ejecución manual

Abre la terminal y ejecuta:
```bash
python programa.py
```

Luego ingresa cada valor de la tabla y verifica que la salida coincida.

### Opción 2: Pruebas automáticas

Abre la terminal y ejecuta:
```bash
python -m pytest test_programa.py -v
```
Si todas las pruebas pasan, verás algo como:
```
test_programa.py::test_voltaje_peligroso PASSED
test_programa.py::test_voltaje_seguro PASSED
test_programa.py::test_voltaje_limite PASSED
```
## ¿Qué hacer si una prueba falla?

1. Lee el mensaje de error.
2. Verifica que tu código esté comparando con > y no con < o >=.
3. Verifica que el mensaje sea exactamente ¡Peligro! Voltaje excesivo.
4. Corrige y vuelve a ejecutar las pruebas.
