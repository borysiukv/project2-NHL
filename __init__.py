# Graph Paths: Dijkstra and A* in Python

## Overview
This project demonstrates advanced algorithmic programming in Python through two classic shortest-path algorithms:
- **Dijkstra's algorithm** for single-source shortest paths in weighted graphs with non-negative edges;
- **A\*** search for efficient goal-directed pathfinding using heuristics.

The code is written in a clean, modular, and Pythonic style. It avoids frontend, database, and UI-oriented code, focusing entirely on algorithm design and implementation quality.

## Features
- Weighted graph abstraction with adjacency lists
- Dijkstra shortest-path computation
- A* pathfinding with pluggable heuristics
- Type hints, docstrings, and dataclasses
- Unit tests with `pytest`
- Lightweight CLI demo

## Project Structure
```text
second_project/
├── src/
│   └── graph_paths/
│       ├── __init__.py
│       ├── algorithms.py
│       └── cli.py
├── tests/
│   └── test_algorithms.py
├── pyproject.toml
└── README.md
```

## Installation
```bash
git clone https://github.com/YOUR_USERNAME/second_project.git
cd second_project
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
pip install -e .[dev]
```

## Example Usage

### Dijkstra
```python
from graph_paths.algorithms import WeightedGraph, dijkstra_shortest_paths

graph = WeightedGraph[str]()
graph.add_edge("A", "B", 4)
graph.add_edge("A", "C", 1)
graph.add_edge("C", "B", 2)
graph.add_edge("B", "D", 1)

distances, predecessors = dijkstra_shortest_paths(graph, "A")
print(distances["D"])  # 4.0
```

### A*
```python
from math import dist
from graph_paths.algorithms import WeightedGraph, a_star_shortest_path

graph = WeightedGraph[tuple[int, int]]()
graph.add_edge((0, 0), (1, 0), 1)
graph.add_edge((1, 0), (1, 1), 1)
graph.add_edge((1, 1), (2, 1), 1)

def heuristic(a: tuple[int, int], b: tuple[int, int]) -> float:
    return dist(a, b)

cost, path = a_star_shortest_path(graph, (0, 0), (2, 1), heuristic)
print(cost)
print(path)
```

## CLI Demo
```bash
python -m graph_paths.cli 0 0 3 1
```

## Complexity
- **Dijkstra**: `O((V + E) log V)` using a priority queue
- **A***: depends on the heuristic, but typically explores fewer states than Dijkstra when the heuristic is informative

## Quality Notes
This repository demonstrates:
- algorithmic problem solving;
- modular project structure;
- readable and maintainable code;
- adherence to Python best practices.

## Author
Your Name
