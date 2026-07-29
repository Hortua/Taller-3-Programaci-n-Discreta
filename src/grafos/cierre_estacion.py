import copy

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

pares = [
    ("Portal Norte", "Portal Eldorado"),
    ("Toberin", "Museo"),
    ("Calle85", "Calle26"),
    ("Calle100", "Portal Eldorado"),
    ("Portal Norte", "Museo")
]

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

comparar_cierre(grafo_transmilenio, "Heroes", pares)
print("---------------------------------------------------------------------------")
comparar_cierre(grafo_transmilenio, "Calle100", pares)
print("---------------------------------------------------------------------------")
comparar_cierre(grafo_transmilenio, "Portal Eldorado", pares)

