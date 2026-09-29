"""
Ejercicio 04: Condicional Anidada
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
    tipo_circuito = input("Digite el tipo de circuito (C/A): ")
    voltaje = float(input("Digite el voltaje medido: "))
    resistencia = float(input("Digite la resistencia: "))
    
    # --- PROCESO Y SALIDAS ---
    if tipo_circuito == "C":
        if voltaje > 220:
            print("Peligro en CC")
        else:
            print("Voltaje CC seguro")
    else:
        if voltaje > 24:
            print("Peligro en CA")
        else:
            print("Voltaje CA seguro")
    
    print(f"La resistencia es {resistencia}")


if __name__ == "__main__":
    main()
