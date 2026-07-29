import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.grafos.cierre_estacion import comparar_cierre

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

pares_tm = [
    ("Portal Norte", "Portal Eldorado"),
    ("Toberin", "Museo"),
    ("Calle85", "Calle26")
]

print("=== CASO 1: TRANSMILENIO - CIERRE DE NODO CRÍTICO ===")
comparar_cierre(grafo_tm, "Heroes", pares_tm)

print("\n=== CASO 2: TRANSMILENIO - CIERRE DE NODO INTERMEDIO ===")
comparar_cierre(grafo_tm, "Calle100", pares_tm)

print("\n=== CASO 3: RED VIAL URBANA CON CAMINOS ALTERNOS ===")
grafo_ciudad = {
    "Zona_A": {"Zona_B": 2, "Zona_C": 4},
    "Zona_B": {"Zona_A": 2, "Zona_C": 1, "Zona_D": 7},
    "Zona_C": {"Zona_A": 4, "Zona_B": 1, "Zona_D": 3},
    "Zona_D": {"Zona_B": 7, "Zona_C": 3}
}

pares_ciudad = [("Zona_A", "Zona_D")]
comparar_cierre(grafo_ciudad, "Zona_C", pares_ciudad)
