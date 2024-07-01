from typing import Union

import networkx as nx
import heapq
import matplotlib.pyplot as plt

def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    ...  # TODO c помощью функции из модуля networkx найти стоимость кратчайшего пути до последней лестницы
    distances = {node: float('inf') for node in graph.nodes}
    distances[0] = 0
    predecessor = {node: None for node in graph.nodes}

    queue = [(0, 0)]
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight['weight']
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessor[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))
    return distances[max(distances.keys())]


def stairway_graph_maker(stairway):
    stairway_graph = [(0, 1, stairway[0])]
    for i in range(1, len(stairway)):
        stairway_graph.append((i, i + 1, stairway[i]))
        stairway_graph.append((i - 1, i + 1, stairway[i]))
    graph = nx.DiGraph()
    graph.add_weighted_edges_from(stairway_graph)
    return graph


if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)

    stairway_graph = stairway_graph_maker(stairway)  # TODO записать взвешенный граф, а лучше написать функцию, которая формирует граф по стоимости ступеней

    # nx.draw_networkx(stairway_graph)
    # plt.show()
    print(stairway_path(stairway_graph))  # 72
