import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.boole.simplificacion import simplificar_minterminos, expresion_simplificada_texto, verificar_equivalencia

casos = [
    {
        "nombre_prueba": "Caso 1: Minitérminos impares (3 variables)",
        "minterminos": [1, 3, 5, 7], 
        "n_vars": 3, 
        "nombres": ["A", "B", "C"]
    },
    {
        "nombre_prueba": "Caso 2: Minitérminos pares (4 variables)",
        "minterminos": [0, 2, 4, 6, 8, 10, 12, 14], 
        "n_vars": 4, 
        "nombres": ["A", "B", "C", "D"]
    },
    {
        "nombre_prueba": "Caso 3: Entrada límite - Todo activo (3 variables)",
        "minterminos":[0, 1, 2, 3, 4, 5, 6, 7], 
        "n_vars":3, 
        "nombres": ["X", "Y", "Z"]
    }
]

print("==================================================")
print("          PRUEBAS: SIMPLIFICACIÓN BOOLEANA        ")
print("==================================================\n")

for caso in casos:
    print(f"--- {caso['nombre_prueba']} ---")
    minterms = caso["minterminos"]
    n_vars = caso["n_vars"]
    nombres = caso["nombres"]

    implicantes = simplificar_minterminos(minterms, n_vars)
    expresion = expresion_simplificada_texto(implicantes, nombres)
    es_equivalente = verificar_equivalencia(minterms, implicantes, n_vars)

    print(f"Minterminos originales: {minterms}")
    print(f"Implicantes binarios:   {implicantes}")
    print(f"Expresión simplificada: {expresion}")
    print(f"¿Tablas equivalentes?:  {es_equivalente}\n")
