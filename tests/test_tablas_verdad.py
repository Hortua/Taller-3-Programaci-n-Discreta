import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.boole.tablas_verdad import expr1, expr2, expr3, tabla_verdad, evaluar

expresiones = [
    ("(A and B) or (not C)", expr1, ["A", "B", "C"]),
    ("(A xor B) and C", expr2, ["A", "B", "C"]),
    ("(A or B) and (not A or C)", expr3, ["A", "B", "C"]),
]

print("=== CASO 1: GENERACIÓN DE TABLAS DE VERDAD COMPLETAS ===")
for nombre, func, variables in expresiones:
    print(f"\nTabla de verdad de: {nombre}")
    tabla_verdad(func, variables)
 
print("\n=== CASO 2: EVALUACIÓN PUNTUAL EN CASOS LÍMITE (TODO EN 0) ===")
print("expr1(A=0, B=0, C=0) =", evaluar(expr1, A=0, B=0, C=0))
print("expr2(A=0, B=0, C=0) =", evaluar(expr2, A=0, B=0, C=0))
print("expr3(A=0, B=0, C=0) =", evaluar(expr3, A=0, B=0, C=0))

print("\n=== CASO 3: EVALUACIÓN PUNTUAL EN CASOS LÍMITE (TODO EN 1) ===")
print("expr1(A=1, B=1, C=1) =", evaluar(expr1, A=1, B=1, C=1))
print("expr2(A=1, B=1, C=1) =", evaluar(expr2, A=1, B=1, C=1))
print("expr3(A=1, B=1, C=1) =", evaluar(expr3, A=1, B=1, C=1))
