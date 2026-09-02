import pytest
from dijkstra import dijkstra_array, dijkstra_heap

def get_graph():
    graph = [[] for _ in range(6)]
    graph[0].append((1, 4))
    graph[0].append((2, 2))
    graph[0].append((3, 6))
    
    graph[1].append((2, 1))
    graph[1].append((3, 3))
    graph[1].append((4, 2))
    graph[1].append((5, 4))
    
    graph[2].append((5, 3))
    
    graph[3].append((4, 5))
    
    graph[4].append((5, 1))
    
    return graph

def test_dijkstra_array():
    graph = get_graph()
    dist = dijkstra_array(graph, 0)
    assert dist == [0, 4, 2, 6, 6, 5], "Ожидаемые дистанции не совпали (array)"

def test_dijkstra_heap():
    graph = get_graph()
    dist = dijkstra_heap(graph, 0)
    assert dist == [0, 4, 2, 6, 6, 5], "Ожидаемые дистанции не совпали (heap)"

def test_unreachable():
    graph = [[(1, 1)], [], [(1, 2)]]
    dist_arr = dijkstra_array(graph, 0)
    dist_hp = dijkstra_heap(graph, 0)
    assert dist_arr == [0, 1, float('inf')]
    assert dist_hp == [0, 1, float('inf')]
