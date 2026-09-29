"""
Ejercicio 03: Pruebas automáticas
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


def test_voltaje_peligroso():
    """Voltaje 250 debe mostrar mensaje de peligro."""
    salida = ejecutar_programa("250\n")
    assert "Peligro" in salida, f"Esperaba 'Peligro' pero obtuve: {salida}"


def test_voltaje_rango_alto():
    """Voltaje 150 debe mostrar 'Voltaje dentro del rango'."""
    salida = ejecutar_programa("150\n")
    assert "rango" in salida.lower(), f"Esperaba 'rango' pero obtuve: {salida}"


def test_voltaje_rango_limite():
    """Voltaje 110 debe mostrar 'Voltaje dentro del rango'."""
    salida = ejecutar_programa("110\n")
    assert "rango" in salida.lower(), f"Esperaba 'rango' pero obtuve: {salida}"


def test_voltaje_insuficiente():
    """Voltaje 50 debe mostrar 'Voltaje insuficiente'."""
    salida = ejecutar_programa("50\n")
    assert "insuficiente" in salida.lower(), f"Esperaba 'insuficiente' pero obtuve: {salida}"


def test_voltaje_limite_superior():
    """Voltaje 220 debe mostrar 'Voltaje dentro del rango'."""
    salida = ejecutar_programa("220\n")
    assert "rango" in salida.lower(), f"Esperaba 'rango' pero obtuve: {salida}"
  
