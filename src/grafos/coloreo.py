def colorear_grafo(grafo):
    colores = {}  # Acá se van a guardar los vértices con su color asignado
    
    for vertice in grafo:
        # Por cada vértice se verifican los colores de sus vecinos
        colores_vecinos = set()
        for vecino in grafo[vertice]:
            if vecino in colores:
                colores_vecinos.add(colores[vecino])
        
        # Se busca el primer color disponible que no esté siendo usado por los vecinos
        color_asignado = 0
        while color_asignado in colores_vecinos:
            color_asignado += 1
        
        colores[vertice] = color_asignado
    
    return colores

def verificar_coloreo(grafo, colores):
    for vertice in grafo:
        for vecino in grafo[vertice]:
            if colores[vertice] == colores[vecino]:
                return False
    return True

def resumen_coloreo(colores):
    grupos = {}
    for vertice, color in colores.items():
        grupos.setdefault(color, []).append(vertice)
    
    print(f"Se usaron {len(grupos)} colores:")
    for color, vertices in grupos.items():
        print(f"  Color {color}: {vertices}")

grafo_conflicto = {
    "A": {"B": 1, "C": 1},
    "B": {"A": 1, "C": 1},
    "C": {"A": 1, "B": 1, "D": 1},
    "D": {"C": 1}
}

resultado = colorear_grafo(grafo_conflicto)
print(resultado)
verificar_coloreo(grafo_conflicto,resultado)
resumen_coloreo(resultado)
