import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.boole.shannon import comparar, analizar_huffman

# Cadenas para los escenarios de prueba
t1 = "AAAAAAAAAA"
t2 = "el veloz murcielago hindu comia feliz cardillo y kiwi"
t3 = "0101010101010101"

print("==================================================")
print("       PRUEBAS: ENTROPÍA Y CÓDIGO HUFFMAN         ")
print("==================================================\n")

print("--- CASO 1 Y 2: COMPARACIÓN DE ENTROPÍA (TEXTO PLANO VS TEXTO COMPLEJO) ---")
comparar(t1, t2)

print("\n" + "=" * 50)
print("ANÁLISIS DE EFICIENCIA DE CODIFICACIÓN")
print("=" * 50)

print(f"\n>> Escenario A (Entropía nula):")
analizar_huffman(t1)

print(f"\n>> Escenario B (Alta entropía):")
analizar_huffman(t2)

print(f"\n--- CASO 3: CASO LÍMITE (CADENA BINARIA BALANCEADA) ---")
print("Evaluación de secuencia periódica pura (máxima incertidumbre binaria):")
analizar_huffman(t3)
