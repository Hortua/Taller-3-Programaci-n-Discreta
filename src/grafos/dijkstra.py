def dijkstra(grafo, origen, destino):
    # Se inicializan las distancias como imfinito
    distancias = {vertice: float('inf') for vertice in grafo}
    #Se inicializa la distancia del origen como 0
    distancias[origen] = 0                                    
    
    visitados = set()
    # Se guarda el vértice desde donde se llega para mostrar la ruta al final
    previo = {vertice: None for vertice in grafo}              

    # Se busca el vértice no visitado con menor distancia
    while len(visitados) < len(grafo):                               
        vertice_actual = None
        menor_distancia = float('inf')
        for vertice in grafo:
            if vertice not in visitados and distancias[vertice] < menor_distancia:
                menor_distancia = distancias[vertice]
                vertice_actual = vertice
        # Se rompe el bucle si no hay más vértices que se puedan visitar
        if vertice_actual is None:                                 
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


