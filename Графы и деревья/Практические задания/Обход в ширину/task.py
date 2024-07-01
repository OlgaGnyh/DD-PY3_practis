from typing import Hashable, List
from collections import deque

import networkx as nx
import matplotlib.pyplot as plt

def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Функция выполняет обход в ширину и возвращает список узлов в порядке посещения.
    В данной задаче порядок обхода графа левосторонний или правосторонний не важен,
    главное соблюсти порядок обхода в ширину.

    :param g: Граф NetworkX, по которому нужно совершить обход
    :param start_node: Стартовый узел, откуда нужно начать обход
    :return: Список узлов в порядке посещения.
    """
    ...  # TODO реализовать обход в ширину
    visited = {i: False for i in g.nodes}
    d = deque()
    path = []

    d.append(start_node)
    visited[start_node] = True

    while d:
        current_node = d.popleft()    #если убрать left то будет обход в шлубину
        path.append(current_node)

        for neighbor in g.neighbors(current_node):
            if not visited[neighbor]:
                d.append(neighbor)
                visited[neighbor] = True
    return path


if __name__ == '__main__':
    # TODO записать граф с помощью модуля networkx и прверить обход в ширину
    graph = nx.Graph()
    # graph.add_nodes_from('ABCDEFGIHJ')
    graph.add_edges_from([
        ('A', 'B'),
        ('A', 'F'),
        ('B', 'G'),
        ('F', 'G'),
        ('G', 'C'),
        ('G', 'H'),
        ('G', 'I'),
        ('C', 'H'),
        ('H', 'J'),
        ('H', 'I'),
        ('H', 'E'),
        ('H', 'D'),
        ('E', 'D')

    ])
    nx.draw_networkx(graph)
    plt.show()
    print(bfs(graph, 'A'))
