"""
Ejercicio 02: Pruebas automáticas
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


def test_voltaje_seguro():
    """Voltaje 110 debe mostrar 'Voltaje dentro del rango'."""
    salida = ejecutar_programa("110\n")
    assert "rango" in salida.lower(), f"Esperaba 'rango' pero obtuve: {salida}"


def test_voltaje_limite():
    """Voltaje 220 debe mostrar 'Voltaje dentro del rango'."""
    salida = ejecutar_programa("220\n")
    assert "rango" in salida.lower(), f"Esperaba 'rango' pero obtuve: {salida}"


def test_voltaje_muy_alto():
    """Voltaje 300 debe mostrar mensaje de peligro."""
    salida = ejecutar_programa("300\n")
    assert "Peligro" in salida, f"Esperaba 'Peligro' pero obtuve: {salida}"


def test_no_pide_temperatura():
    """El programa NO debe pedir temperatura."""
    salida = ejecutar_programa("250\n")
    assert "temperatura" not in salida.lower(), f"No debe pedir temperatura: {salida}"
