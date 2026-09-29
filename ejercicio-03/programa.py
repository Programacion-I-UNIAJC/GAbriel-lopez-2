"""
Ejercicio 03: Clasificador de Voltaje (Múltiple)
Programación I — UNIAJC
Variante A: COMPLETAR

INSTRUCCIONES:
Completa las partes marcadas con ___ para que el programa funcione.
Guíate por el análisis IPO y el pseudocódigo del archivo 02-algoritmo.md.

Cuando termines, ejecuta las pruebas:
    python -m pytest test_programa.py -v
"""


def main():
    # --- ENTRADAS ---
    voltaje = float(input("Digite el voltaje medido: "))
    
    # --- PROCESO Y SALIDAS ---
    if voltaje ___ 220:
        print("¡Peligro! Voltaje excesivo")
    ___ voltaje >= 110:
        print("___")
    ___:
        print("Voltaje insuficiente")


if __name__ == "__main__":
    main()
