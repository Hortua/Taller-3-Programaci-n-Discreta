import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.grafos.coloreo import colorear_grafo, verificar_coloreo, resumen_coloreo

print("=== CASO 1: GRAFO DE CONFLICTO ORIGINAL ===")
grafo1 = {
    "A": ["B", "C"],
    "B": ["A", "C"],
    "C": ["A", "B", "D"],
    "D": ["C"]
}
res1 = colorear_grafo(grafo1)
print(f"Resultado: {res1}")
print(f"¿Es válido?: {verificar_coloreo(grafo1, res1)}")
resumen_coloreo(res1)

print("\n=== CASO 2: GRAFO CÍCLICO IMPAR (K3 / TRIÁNGULO) ===")
# Matemáticamente requiere exactamente 3 colores
grafo2 = {
    "V1": ["V2", "V3"],
    "V2": ["V1", "V3"],
    "V3": ["V1", "V2"]
}
res2 = colorear_grafo(grafo2)
print(f"Resultado: {res2}")
print(f"¿Es válido?: {verificar_coloreo(grafo2, res2)}")
resumen_coloreo(res2)

print("\n=== CASO 3: ENTRADA LÍMITE (VÉRTICES AISLADOS) ===")
# Al no haber conexiones, todos deberían poder usar el Color 0
grafo3 = {
    "X": [],
    "Y": [],
    "Z": []
}
res3 = colorear_grafo(grafo3)
print(f"Resultado: {res3}")
print(f"¿Es válido?: {verificar_coloreo(grafo3, res3)}")
resumen_coloreo(res3)
