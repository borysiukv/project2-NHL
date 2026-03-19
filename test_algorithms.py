from math import dist

import pytest

from graph_paths.algorithms import WeightedGraph, a_star_shortest_path, dijkstra_shortest_paths


@pytest.fixture
def sample_graph() -> WeightedGraph[str]:
    graph: WeightedGraph[str] = WeightedGraph()
    graph.add_edge("A", "B", 4)
    graph.add_edge("A", "C", 1)
    graph.add_edge("C", "B", 2)
    graph.add_edge("B", "D", 1)
    graph.add_edge("C", "D", 5)
    return graph


def test_dijkstra_distances(sample_graph: WeightedGraph[str]) -> None:
    distances, predecessors = dijkstra_shortest_paths(sample_graph, "A")
    assert distances["A"] == 0
    assert distances["B"] == 3
    assert distances["D"] == 4
    assert predecessors["B"] == "C"
    assert predecessors["D"] == "B"


def test_negative_weight_rejected() -> None:
    graph: WeightedGraph[str] = WeightedGraph()
    with pytest.raises(ValueError):
        graph.add_edge("A", "B", -1)


def test_a_star_returns_shortest_path() -> None:
    graph: WeightedGraph[tuple[int, int]] = WeightedGraph()
    edges = [
        ((0, 0), (1, 0), 1),
        ((1, 0), (2, 0), 1),
        ((0, 0), (0, 1), 1),
        ((0, 1), (1, 1), 1),
        ((1, 1), (2, 1), 1),
        ((2, 0), (2, 1), 1),
    ]
    for source, target, weight in edges:
        graph.add_edge(source, target, weight)
        graph.add_edge(target, source, weight)

    heuristic = lambda a, b: dist(a, b)
    cost, path = a_star_shortest_path(graph, (0, 0), (2, 1), heuristic)

    assert cost == 3
    assert path[0] == (0, 0)
    assert path[-1] == (2, 1)


def test_a_star_raises_if_unreachable() -> None:
    graph: WeightedGraph[str] = WeightedGraph()
    graph.add_edge("A", "B", 1)
    with pytest.raises(ValueError):
        a_star_shortest_path(graph, "A", "Z", lambda _a, _b: 0)
