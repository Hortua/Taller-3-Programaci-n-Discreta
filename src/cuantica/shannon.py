import math
import heapq
from collections import Counter



def frecuencias(texto):
    """Cuenta cuantas veces aparece cada simbolo en el texto."""
    return dict(Counter(texto))


def probabilidades(frecs, total):
    """Convierte frecuencias en probabilidades (frecuencia / total)."""
    return {simbolo: cuenta / total for simbolo, cuenta in frecs.items()}



def entropia(probs):
    """
    H = - sum(p_i * log2(p_i))
    Cada termino mide, en bits, cuanta informacion aporta en promedio
    ese simbolo. Se usa log2 porque el bit es la unidad natural de
    informacion (una pregunta de si/no).
    """
    return -sum(p * math.log2(p) for p in probs.values() if p > 0)



def analizar_texto(texto, nombre="Texto"):
    total = len(texto)
    frecs = frecuencias(texto)
    probs = probabilidades(frecs, total)
    H = entropia(probs)

    print(f"\n{nombre}: {texto!r}  (longitud = {total})")
    print("Simbolo | Frecuencia | Probabilidad")
    for simbolo in sorted(frecs):
        print(f"  {simbolo!r:>5} | {frecs[simbolo]:>10} | {probs[simbolo]:.4f}")
    print(f"Entropia H = {H:.4f} bits/simbolo")

    return H, frecs, probs


def comparar(texto1, texto2):
    """Calcula la entropia de dos textos y explica cual es mas variado."""
    H1, _, _ = analizar_texto(texto1, "Texto 1")
    H2, _, _ = analizar_texto(texto2, "Texto 2")

    print("\nComparacion:")
    if H1 > H2:
        print(f"Texto 1 tiene mayor entropia ({H1:.4f} > {H2:.4f}): "
              "es mas impredecible, sus simbolos estan mas repartidos.")
    elif H2 > H1:
        print(f"Texto 2 tiene mayor entropia ({H2:.4f} > {H1:.4f}): "
              "es mas impredecible, sus simbolos estan mas repartidos.")
    else:
        print(f"Ambos textos tienen la misma entropia ({H1:.4f}).")



class NodoHuffman:
    """Nodo del arbol de Huffman. simbolo=None en nodos internos."""
    def __init__(self, peso, simbolo=None, izq=None, der=None):
        self.peso = peso
        self.simbolo = simbolo
        self.izq = izq
        self.der = der

    def __lt__(self, otro):
        # necesario para que heapq pueda comparar nodos por peso
        return self.peso < otro.peso


def arbol_huffman(frecs):

    heap = [NodoHuffman(peso, simbolo) for simbolo, peso in frecs.items()]
    heapq.heapify(heap)

    # caso especial: un solo simbolo distinto en el texto
    if len(heap) == 1:
        unico = heap[0]
        return NodoHuffman(unico.peso, izq=unico)

    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        nuevo = NodoHuffman(a.peso + b.peso, izq=a, der=b)
        heapq.heappush(heap, nuevo)

    return heap[0]


def generar_codigos(nodo, prefijo="", codigos=None):
    if codigos is None:
        codigos = {}
    if nodo.simbolo is not None:
        codigos[nodo.simbolo] = prefijo or "0"  # caso de un solo simbolo
        return codigos
    if nodo.izq:
        generar_codigos(nodo.izq, prefijo + "0", codigos)
    if nodo.der:
        generar_codigos(nodo.der, prefijo + "1", codigos)
    return codigos


def longitud_promedio_huffman(frecs, codigos, total):
    return sum(frecs[s] * len(codigos[s]) for s in frecs) / total


def analizar_huffman(texto):
    total = len(texto)
    frecs = frecuencias(texto)
    probs = probabilidades(frecs, total)
    H = entropia(probs)

    arbol = arbol_huffman(frecs)
    codigos = generar_codigos(arbol)
    L = longitud_promedio_huffman(frecs, codigos, total)

    print(f"\nCodigo de Huffman para {texto!r}:")
    for simbolo in sorted(codigos):
        print(f"  {simbolo!r}: {codigos[simbolo]}")
    print(f"Longitud promedio del codigo Huffman = {L:.4f} bits/simbolo")
    print(f"Entropia teorica H = {H:.4f} bits/simbolo")
    print("(Huffman siempre da una longitud promedio >= H; "
          "se acerca al limite teorico de Shannon)")



texto_repetitivo = "AAAAAAAAAA"
texto_variado = "el veloz murcielago hindu comia feliz cardillo y kiwi"

comparar(texto_repetitivo, texto_variado)

print("\n" + "=" * 60)
print("Extension opcional: codigo de Huffman")
print("=" * 60)
analizar_huffman(texto_repetitivo)
analizar_huffman(texto_variado)
