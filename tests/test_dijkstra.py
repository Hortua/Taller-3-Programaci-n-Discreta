import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.grafos.dijkstra import dijkstra

print("--- CASO 1: GRAFO ACADÉMICO BÁSICO ---")
grafo_simple = {
    "A": {"B": 4, "C": 1},
    "B": {"A": 4, "C": 2, "D": 5},
    "C": {"A": 1, "B": 2, "D": 8},
    "D": {"B": 5, "C": 8}
}
dist1, ruta1 = dijkstra(grafo_simple, "A", "D")
print(f"Distancia: {dist1} | Ruta: {ruta1}")

print("\n--- CASO 2: RED TRANSMILENIO OBLIGATORIA ---")
grafo_tm = {
    "Portal Norte": {"Toberin": 3, "Calle100": 6},
    "Toberin": {"Portal Norte": 3, "Calle100": 4, "Calle85": 5},
    "Calle100": {"Portal Norte": 6, "Toberin": 4, "Calle85": 2, "Heroes": 5},
    "Calle85": {"Toberin": 5, "Calle100": 2, "Heroes": 3},
    "Heroes": {"Calle100": 5, "Calle85": 3, "Calle26": 4, "Museo": 6},
    "Calle26": {"Heroes": 4, "Museo": 2, "Portal Eldorado": 7},
    "Museo": {"Heroes": 6, "Calle26": 2, "Portal Eldorado": 5},
    "Portal Eldorado": {"Calle26": 7, "Museo": 5}
}
dist2, ruta2 = dijkstra(grafo_tm, "Portal Norte", "Portal Eldorado")
print(f"Distancia: {dist2} | Ruta: {ruta2}")

print("\n--- CASO 3: ENTRADA LÍMITE (ESTACIONES DESCONECTADAS) ---")
grafo_incomunicado = {
    "Portal Norte": {"Toberin": 3},
    "Toberin": {"Portal Norte": 3},
    "Portal Eldorado": {}
}
dist3, ruta3 = dijkstra(grafo_incomunicado, "Portal Norte", "Portal Eldorado")
print(f"Distancia: {dist3} (Esperado: inf) | Ruta: {ruta3} (Esperado: ['Portal Eldorado'])")
