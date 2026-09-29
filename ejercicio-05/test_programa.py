"""
Ejercicio 05: Pruebas automáticas
Programación I — UNIAJC

Ejecuta estas pruebas con:
    python -m pytest test_programa.py -v
"""

import subprocess
import sys


def ejecutar_programa(entrada):
    """Ejecuta programa.py con la entrada dada y devuelve la salida."""
    resultado = subprocess.run(
        [sys.executable, "programa.py"],
        input=entrada,
        capture_output=True,
        text=True,
        timeout=10
    )
    return resultado.stdout


def test_promedio_basico():
    """3 mediciones: 10, 20, 30 debe dar 20.00."""
    salida = ejecutar_programa("3\n10\n20\n30\n")
    assert "20.00" in salida, f"Esperaba 20.00 pero obtuve: {salida}"


def test_promedio_dos():
    """2 mediciones: 5, 15 debe dar 10.00."""
    salida = ejecutar_programa("2\n5\n15\n")
    assert "10.00" in salida, f"Esperaba 10.00 pero obtuve: {salida}"


def test_promedio_uno():
    """1 medición: 7 debe dar 7.00."""
    salida = ejecutar_programa("1\n7\n")
    assert "7.00" in salida, f"Esperaba 7.00 pero obtuve: {salida}"


def test_promedio_cuatro():
    """4 mediciones iguales: 10 debe dar 10.00."""
    salida = ejecutar_programa("4\n10\n10\n10\n10\n")
    assert "10.00" in salida, f"Esperaba 10.00 pero obtuve: {salida}"


def test_promedio_ceros():
    """3 mediciones: 0, 0, 0 debe dar 0.00."""
    salida = ejecutar_programa("3\n0\n0\n0\n")
    assert "0.00" in salida, f"Esperaba 0.00 pero obtuve: {salida}"
