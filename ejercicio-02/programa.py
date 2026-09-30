"""
Ejercicio 02: Clasificador de Voltaje (Doble)
Programación I — UNIAJC
Variante B: CORREGIR ERRORES

INSTRUCCIONES:
Este código tiene errores intencionales. Tu tarea es:
1. Leerlo con atención.
2. Identificar qué líneas están mal o sobran.
3. Corregirlas para que el programa funcione.
4. Ejecutar las pruebas para verificar:
       python -m pytest test_programa.py -v

PISTA: Hay 3 errores en este código.
"""


def main():
    # --- ENTRADAS ---
    voltaje = float(input("Digite el voltaje medido: "))

    
    # --- PROCESO Y SALIDAS ---
    if voltaje>220:
        print("¡Peligro! Voltaje excesivo")
    else:
        print("Voltaje dentro del rango")
        
    
5


if __name__ == "__main__":
    main()
