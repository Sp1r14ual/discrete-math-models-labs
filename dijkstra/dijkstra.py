import heapq

def dijkstra_array(graph, start):
    """
    Алгоритм Дейкстры с использованием массива для поиска минимума.
    Асимптотика: O(V^2 + E), где V - количество вершин, E - количество ребер.
    graph: список смежности, graph[u] = [(v, weight), ...]
    start: начальная вершина
    """
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    visited = [False] * n

    for _ in range(n):
        # Поиск вершины с минимальным расстоянием среди непосещенных
        u = -1
        min_d = float('inf')
        for i in range(n):
            if not visited[i] and dist[i] < min_d:
                min_d = dist[i]
                u = i
                
        if u == -1:
            break
            
        visited[u] = True
        
        # Релаксация ребер
        for v, weight in graph[u]:
            if not visited[v] and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                
    return dist

def dijkstra_heap(graph, start):
    """
    Алгоритм Дейкстры с использованием двоичной кучи (binary heap).
    Асимптотика: O((V + E) log V), что лучше для разреженных графов.
    graph: список смежности, graph[u] = [(v, weight), ...]
    start: начальная вершина
    """
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    
    # В куче храним кортежи (текущее_расстояние, вершина)
    heap = [(0, start)]
    
    while heap:
        d, u = heapq.heappop(heap)
        
        # Если извлеченное расстояние больше текущего минимального, пропускаем
        # (это старая запись, которая уже не актуальна)
        if d > dist[u]:
            continue
            
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(heap, (dist[v], v))
                
    return dist
