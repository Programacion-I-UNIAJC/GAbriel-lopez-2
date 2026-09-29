"""
Ejercicio 04: Pruebas automáticas
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


def test_cc_peligro():
    """Circuito CC con voltaje 30 debe mostrar 'Peligro en CC'."""
    salida = ejecutar_programa("C\n30\n")
    assert "Peligro en CC" in salida, f"Esperaba 'Peligro en CC' pero obtuve: {salida}"


def test_cc_seguro():
    """Circuito CC con voltaje 12 debe mostrar 'Voltaje CC seguro'."""
    salida = ejecutar_programa("C\n12\n")
    assert "CC seguro" in salida, f"Esperaba 'CC seguro' pero obtuve: {salida}"


def test_ca_peligro():
    """Circuito CA con voltaje 250 debe mostrar 'Peligro en CA'."""
    salida = ejecutar_programa("A\n250\n")
    assert "Peligro en CA" in salida, f"Esperaba 'Peligro en CA' pero obtuve: {salida}"


def test_ca_seguro():
    """Circuito CA con voltaje 110 debe mostrar 'Voltaje CA seguro'."""
    salida = ejecutar_programa("A\n110\n")
    assert "CA seguro" in salida, f"Esperaba 'CA seguro' pero obtuve: {salida}"


def test_no_pide_resistencia():
    """El programa NO debe pedir resistencia."""
    salida = ejecutar_programa("C\n30\n")
    assert "resistencia" not in salida.lower(), f"No debe pedir resistencia: {salida}"
