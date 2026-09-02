import time
import random
from dijkstra import dijkstra_array, dijkstra_heap

def generate_graph(V, E):
    graph = [[] for _ in range(V)]
    edges = set()
    while len(edges) < E:
        u = random.randint(0, V - 1)
        v = random.randint(0, V - 1)
        if u != v and (u, v) not in edges:
            edges.add((u, v))
            weight = random.randint(1, 100)
            graph[u].append((v, weight))
    return graph

def benchmark():
    sizes = [
        (100, 500, "Разреженный (E=5V)"),
        (500, 2500, "Разреженный (E=5V)"),
        (1000, 5000, "Разреженный (E=5V)"),
        (2000, 10000, "Разреженный (E=5V)"),
        
        (100, 4000, "Плотный (E=0.4V^2)"),
        (500, 100000, "Плотный (E=0.4V^2)"),
        (1000, 400000, "Плотный (E=0.4V^2)"),
        (2000, 1600000, "Плотный (E=0.4V^2)")
    ]
    
    print(f"{'V':<6} {'E':<10} {'Тип графа':<22} {'Array (мс)':<12} {'Heap (мс)':<12}")
    print("-" * 65)
    
    for V, E, desc in sizes:
        graph = generate_graph(V, E)
        start_node = 0
        
        # Test Array
        t0 = time.perf_counter()
        dijkstra_array(graph, start_node)
        t1 = time.perf_counter()
        time_arr = (t1 - t0) * 1000
        
        # Test Heap
        t0 = time.perf_counter()
        dijkstra_heap(graph, start_node)
        t1 = time.perf_counter()
        time_heap = (t1 - t0) * 1000
        
        print(f"{V:<6} {E:<10} {desc:<22} {time_arr:<12.2f} {time_heap:<12.2f}")

if __name__ == '__main__':
    random.seed(100)
    benchmark()
