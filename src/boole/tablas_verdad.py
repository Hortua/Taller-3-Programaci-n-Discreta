from itertools import product
def expr1(A, B, C, D=None):
    #(A AND B) OR (NOT C)
    return int((A and B) or (not C))
 
 
def expr2(A, B, C, D=None):
    #(A XOR B) AND C
    return int((A != B) and C)
 
 
def expr3(A, B, C, D=None):
    #(A OR B) AND (NOT A OR C)
    return int((A or B) and ((not A) or C))

expresiones = [
    ("(A and B) or (not C)", expr1, ["A", "B", "C"]),
    ("(A xor B) and C", expr2, ["A", "B", "C"]),
    ("(A or B) and (not A or C)", expr3, ["A", "B", "C"]),
]

def tabla_verdad(func, variables):
    n = len(variables)
    encabezado = " | ".join(variables) + " | Resultado"
    print(encabezado)
    print("-" * len(encabezado))
 
    filas = []
    for combinacion in product([0, 1], repeat=n):
        valores = dict(zip(variables, combinacion))
        resultado = func(**valores)
        filas.append((combinacion, resultado))
        fila_texto = " | ".join(str(v) for v in combinacion) + f" | {resultado}"
        print(fila_texto)
 
    return filas

def evaluar(func, **valores):
    return func(**valores)

for nombre, func, variables in expresiones:
        print(f"\nTabla de verdad de: {nombre}")
        tabla_verdad(func, variables)
 
print("\nEjemplo de evaluacion puntual:")
print("expr1(A=1, B=0, C=0) =", evaluar(expr1, A=1, B=0, C=0))
print("expr2(A=1, B=1, C=1) =", evaluar(expr2, A=1, B=1, C=1))
print("expr3(A=0, B=0, C=1) =", evaluar(expr3, A=0, B=0, C=1))
