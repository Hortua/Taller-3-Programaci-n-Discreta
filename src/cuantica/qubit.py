import math
import random


ESTADO_0 = [1.0, 0.0]   # |0>
ESTADO_1 = [0.0, 1.0]   # |1>

# Matrices de representación de compuertas cuánticas clásicas
X = [[0, 1],
     [1, 0]]

Z = [[1, 0],
     [0, -1]]

RAIZ2 = math.sqrt(2)
H = [[1 / RAIZ2, 1 / RAIZ2],
     [1 / RAIZ2, -1 / RAIZ2]]



def aplicar_compuerta(matriz, estado):
    # Multiplicación matriz-vector para transformar la amplitud de probabilidad
    nuevo_alpha = matriz[0][0] * estado[0] + matriz[0][1] * estado[1]
    nuevo_beta = matriz[1][0] * estado[0] + matriz[1][1] * estado[1]
    return [nuevo_alpha, nuevo_beta]


def probabilidades(estado):
    #P(0) = |alpha|^2, P(1) = |beta|^2.
    p0 = estado[0] ** 2
    p1 = estado[1] ** 2
    return p0, p1



def simular_mediciones(p0, n=1000):
    #Se simula el colapso del estado cuántico mediante un muestreo estocástico
    conteo_0 = 0
    conteo_1 = 0
    for _ in range(n):
        if random.random() < p0:
            conteo_0 += 1
        else:
            conteo_1 += 1
    return conteo_0, conteo_1



def mostrar_estado(nombre, estado):
    #Se imprime analíticamente el estado, sus probabilidades y simula el colapso
    p0, p1 = probabilidades(estado)
    print(f"\n{nombre}: estado = [{estado[0]:.4f}, {estado[1]:.4f}]")
    print(f"  P(0) = {p0:.4f}   P(1) = {p1:.4f}")
    c0, c1 = simular_mediciones(p0, 1000)
    print(f"  1000 mediciones simuladas -> 0: {c0}  1: {c1}  "
          f"(frecuencias: {c0/1000:.3f} / {c1/1000:.3f})")
    return estado




