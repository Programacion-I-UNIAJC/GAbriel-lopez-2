"""
Ejercicio 05: Promedio de Mediciones
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
    num_mediciones =int(input("Digite el número de mediciones: "))
    
    # --- PROCESO ---
    suma =0
    for i in range(num_mediciones):
        valor = float(input(f"Digite la medición {i+1}: "))
        suma+=valor
    
    promedio = suma/num_mediciones
    
    # --- SALIDAS ---
    print(f"El promedio de las mediciones es: {promedio:.2f}")


if __name__ == "__main__":
    main()
