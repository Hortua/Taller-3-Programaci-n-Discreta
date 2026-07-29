import copy

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




def cerrar_vertice(grafo, vertice_cerrado):
    grafo_nuevo = copy.deepcopy(grafo)
    grafo_nuevo.pop(vertice_cerrado)
    
    # Eliminamos la referencia al vertice eliminado de sus vecinos
    for v in grafo_nuevo:
        if vertice_cerrado in grafo_nuevo[v]:
            grafo_nuevo[v].pop(vertice_cerrado)
    
    return grafo_nuevo

def comparar_cierre(grafo, vertice_cerrado, pares):
    grafo_cerrado = cerrar_vertice(grafo, vertice_cerrado)
    
    print(f"{'Origen':<20}{'Destino':<20}{'Antes':<10}{'Después':<10}{'Diferencia':<12}{'Estado'}")
    
    for origen, destino in pares:
        dist_antes, _ = dijkstra(grafo, origen, destino)
        
        # Verificamos que ni el origen ni el destino sean el vertice cerrado, si
        # es así, saltamos esta iteración del ciclo
        if origen == vertice_cerrado or destino == vertice_cerrado:
            print(f"{origen:<20}{destino:<20}{dist_antes:<10}{'N/A':<10}{'N/A':<12}{'Vértice cerrado'}")
            continue
        
        dist_despues, _ = dijkstra(grafo_cerrado, origen, destino)
        
        if dist_despues == float('inf'):                    #Manejamos el caso donde dos puntos quedan desconectados, imprimimos 'Desconectado' en lugar de infinito
            print(f"{origen:<20}{destino:<20}{dist_antes:<10}{'inf':<10}{'N/A':<12}{'Desconectado'}")
        else:
            diferencia = dist_despues - dist_antes
            print(f"{origen:<20}{destino:<20}{dist_antes:<10}{dist_despues:<10}{diferencia:<12}{'Conectado'}")

