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
    #Dibujo del encabezado de la tabla
    encabezado = " | ".join(variables) + " | Resultado"
    print(encabezado)
    print("-" * len(encabezado))
 
    filas = []
    #Se evaluan todas las 2^n combinaciones binarias posibles 
    for combinacion in product([0, 1], repeat=n):
        valores = dict(zip(variables, combinacion))
        resultado = func(**valores)
        #Se guarda el par de valores de entrada y el resultado
        filas.append((combinacion, resultado))
        #Se crea el String con los valores de entrada y salida
        fila_texto = " | ".join(str(v) for v in combinacion) + f" | {resultado}"
        print(fila_texto)
 
    return filas

def evaluar(func, **valores):
    return func(**valores)


