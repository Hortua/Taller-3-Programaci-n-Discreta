import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.cripto.rsa import calcular_n, calcular_phi, calcular_d, cifrado, descifrado

print("--- CASO 1: PARÁMETROS OBLIGATORIOS ---")
p, q, e, M = 61, 53, 17, 65
n = calcular_n(p, q)
phi = calcular_phi(p, q)
d = calcular_d(e, phi)
C = cifrado(M, e, n)

print(f"n={n}, phi={phi}, d={d}, C={C}, M={descifrado(C, d, n)}")

print("\n--- CASO 2: ERROR CON E INVÁLIDO ---")
try:
    calcular_d(15, phi)  # gcd(15, 3120) != 1
except ValueError as error:
    print(f"Error esperado: {error}")

print("\n--- CASO 3: ENTRADA LÍMITE ---")
M_limite = 1
C_limite = cifrado(M_limite, e, n)
print(f"M={M_limite} -> C={C_limite} -> M={descifrado(C_limite, d, n)}")
