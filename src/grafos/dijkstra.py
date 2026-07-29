def dijkstra(grafo, origen, destino):
    distancias = {vertice: float('inf') for vertice in grafo} # Se inicializan las distancias como imfinito
    distancias[origen] = 0                                    #Se inicializa la distancia del origen como 0
    
    visitados = set()
    previo = {vertice: None for vertice in grafo}              # Se guarda el vértice desde donde se llega para mostrar la ruta al final
    
    while len(visitados) < len(grafo):                               # Se el vértice no visitado con menor distancia
        vertice_actual = None
        menor_distancia = float('inf')
        for vertice in grafo:
            if vertice not in visitados and distancias[vertice] < menor_distancia:
                menor_distancia = distancias[vertice]
                vertice_actual = vertice
        
        if vertice_actual is None:                                 # Se rompe el bucle si no hay más vértices que se puedan visitar
            break
        
        visitados.add(vertice_actual)
        
        # Se revisan los vecinos del vértice actual para ver si las distancias se pueden reducir
        for vecino, peso in grafo[vertice_actual].items():
            if vecino not in visitados:
                nueva_distancia = distancias[vertice_actual] + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    previo[vecino] = vertice_actual
    
    # Usamos la el diccionario llamado previo para construir la ruta en reversa
    ruta = []
    actual = destino
    while actual is not None:
        ruta.insert(0, actual)
        actual = previo[actual]
    
    return distancias[destino], ruta

grafo = {
    "A": {"B": 4, "C": 1},
    "B": {"A": 4, "C": 2, "D": 5},
    "C": {"A": 1, "B": 2, "D": 8},
    "D": {"B": 5, "C": 8}
}

distancia, ruta = dijkstra(grafo, "A", "D")
print(f"Distancia más corta: {distancia}")  
print(f"Ruta: {ruta}")


grafo_transmilenio = {
    "Portal Norte": {"Toberin": 3, "Calle100": 6},
    "Toberin": {"Portal Norte": 3, "Calle100": 4, "Calle85": 5},
    "Calle100": {"Portal Norte": 6, "Toberin": 4, "Calle85": 2, "Heroes": 5},
    "Calle85": {"Toberin": 5, "Calle100": 2, "Heroes": 3},
    "Heroes": {"Calle100": 5, "Calle85": 3, "Calle26": 4, "Museo": 6},
    "Calle26": {"Heroes": 4, "Museo": 2, "Portal Eldorado": 7},
    "Museo": {"Heroes": 6, "Calle26": 2, "Portal Eldorado": 5},
    "Portal Eldorado": {"Calle26": 7, "Museo": 5}
}

distancia, ruta = dijkstra(grafo_transmilenio, "Portal Norte", "Portal Eldorado")
print(f"Distancia más corta: {distancia}")
print(f"Ruta: {ruta}")

