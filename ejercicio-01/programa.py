"""
Ejercicio 01: Clasificador de Voltaje (Simple)
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
    # Pista: el voltaje es un número real (puede tener decimales)
    voltaje = ___(input("Digite el voltaje medido: "))
    
    # --- PROCESO Y SALIDAS ---
    # Pista: compara si el voltaje es MAYOR que 220
    if voltaje ___ 220:
        print("___")


if __name__ == "__main__":
    main()
