import math
import random


ESTADO_0 = [1.0, 0.0]   # |0>
ESTADO_1 = [0.0, 1.0]   # |1>

X = [[0, 1],
     [1, 0]]

Z = [[1, 0],
     [0, -1]]

RAIZ2 = math.sqrt(2)
H = [[1 / RAIZ2, 1 / RAIZ2],
     [1 / RAIZ2, -1 / RAIZ2]]



def aplicar_compuerta(matriz, estado):
    nuevo_alpha = matriz[0][0] * estado[0] + matriz[0][1] * estado[1]
    nuevo_beta = matriz[1][0] * estado[0] + matriz[1][1] * estado[1]
    return [nuevo_alpha, nuevo_beta]


def probabilidades(estado):
    #P(0) = |alpha|^2, P(1) = |beta|^2.
    p0 = estado[0] ** 2
    p1 = estado[1] ** 2
    return p0, p1



def simular_mediciones(p0, n=1000):
    conteo_0 = 0
    conteo_1 = 0
    for _ in range(n):
        if random.random() < p0:
            conteo_0 += 1
        else:
            conteo_1 += 1
    return conteo_0, conteo_1



def mostrar_estado(nombre, estado):
    p0, p1 = probabilidades(estado)
    print(f"\n{nombre}: estado = [{estado[0]:.4f}, {estado[1]:.4f}]")
    print(f"  P(0) = {p0:.4f}   P(1) = {p1:.4f}")
    c0, c1 = simular_mediciones(p0, 1000)
    print(f"  1000 mediciones simuladas -> 0: {c0}  1: {c1}  "
          f"(frecuencias: {c0/1000:.3f} / {c1/1000:.3f})")
    return estado




print("=== Aplicando compuertas a |0> ===")

estado_X = aplicar_compuerta(X, ESTADO_0)
mostrar_estado("X|0>", estado_X)

estado_Z = aplicar_compuerta(Z, ESTADO_0)
mostrar_estado("Z|0>", estado_Z)

estado_H = aplicar_compuerta(H, ESTADO_0)
mostrar_estado("H|0>", estado_H)

estado_HH = aplicar_compuerta(H, estado_H)
mostrar_estado("HH|0>", estado_HH)

print("\n=== Casos de prueba obligatorios ===")

# Caso 1: X|0> = |1>
assert estado_X == ESTADO_1, "Fallo: X|0> deberia ser |1>"
print("OK: X|0> = |1>")

# Caso 2: H|0> da probabilidades cercanas a 50%/50%
p0_H, p1_H = probabilidades(estado_H)
assert abs(p0_H - 0.5) < 1e-9 and abs(p1_H - 0.5) < 1e-9, \
    "Fallo: H|0> deberia dar 50%/50%"
print(f"OK: H|0> da P(0)={p0_H:.4f}, P(1)={p1_H:.4f} (cercanas a 50%/50%)")

# Caso 3: HH|0> = |0> (salvo errores numericos pequeños)
tolerancia = 1e-9
assert abs(estado_HH[0] - ESTADO_0[0]) < tolerancia, "Fallo en HH|0>[0]"
assert abs(estado_HH[1] - ESTADO_0[1]) < tolerancia, "Fallo en HH|0>[1]"
print(f"OK: HH|0> = [{estado_HH[0]:.10f}, {estado_HH[1]:.10f}] ~= |0>")
