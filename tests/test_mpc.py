import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.cripto.mpc import repartir_notas, calcular_suma, calcular_promedio

M = 1000003

print("--- CASO 1: EJEMPLO MÍNIMO OBLIGATORIO ---")
notas1 = [40, 35, 50, 25]
s1, s2, s3 = repartir_notas(notas1, M)
suma1 = calcular_suma(s1, s2, s3, M)
print(f"Suma: {suma1} (Esperado: 150)")
print(f"Promedio: {calcular_promedio(suma1, len(notas1))} (Esperado: 37.5)")

print("\n--- CASO 2: NOTAS EN EXTREMOS (VALORES LÍMITE) ---")
notas2 = [0, 50, 0, 50]
s1_2, s2_2, s3_2 = repartir_notas(notas2, M)
suma2 = calcular_suma(s1_2, s2_2, s3_2, M)
print(f"Suma: {suma2} | Promedio: {calcular_promedio(suma2, len(notas2))}")

print("\n--- CASO 3: LISTA GRANDE DE ESTUDIANTES ---")
notas3 = [45, 30, 20, 15, 50, 48, 33, 41, 29, 35]
s1_3, s2_3, s3_3 = repartir_notas(notas3, M)
suma3 = calcular_suma(s1_3, s2_3, s3_3, M)
print(f"Cantidad de notas: {len(notas3)}")
print(f"Suma: {suma3} | Promedio: {calcular_promedio(suma3, len(notas3))}")
