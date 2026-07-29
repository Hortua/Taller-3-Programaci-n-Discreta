import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.cuantica.qubit import ESTADO_0, ESTADO_1, X, Z, H, aplicar_compuerta, probabilidades, mostrar_estado

print("==================================================")
print("         PRUEBAS: SIMULADOR CUÁNTICO QUBIT        ")
print("==================================================\n")

print("--- EJECUCIÓN Y TRANSFORMACIÓN DE ESTADOS ---")
estado_X = aplicar_compuerta(X, ESTADO_0)
mostrar_estado("X|0>", estado_X)

estado_Z = aplicar_compuerta(Z, ESTADO_0)
mostrar_estado("Z|0>", estado_Z)

estado_H = aplicar_compuerta(H, ESTADO_0)
mostrar_estado("H|0>", estado_H)

estado_HH = aplicar_compuerta(H, estado_H)
mostrar_estado("HH|0>", estado_HH)

print("\n--- CASOS DE PRUEBA OBLIGATORIOS  ---")

# Caso 1: Negación cuántica (Compuerta NOT / Pauli-X)
assert estado_X == ESTADO_1, "Fallo: X|0> debería ser |1>"
print(f"Caso 1 = X|0> = |1> verificado.")

# Caso 2: Superposición balanceada (Compuerta Hadamard)
p0_H, p1_H = probabilidades(estado_H)
assert abs(p0_H - 0.5) < 1e-9 and abs(p1_H - 0.5) < 1e-9, "Fallo: H|0> debería dar 50%/50%"
print(f"Caso 2 = H|0> genera superposición pura 50%/50% (P(0)={p0_H:.4f}).")

# Caso 3: Propiedad involutiva (H es su propia inversa: H*H = I)
tolerancia = 1e-9
assert abs(estado_HH[0] - ESTADO_0[0]) < tolerancia, "Fallo en la amplitud alpha de HH|0>"
assert abs(estado_HH[1] - ESTADO_0[1]) < tolerancia, "Fallo en la amplitud beta de HH|0>"
print(f"Caso 3 = H(H|0>) revierte al estado base original |0> (Involución cuántica).")
