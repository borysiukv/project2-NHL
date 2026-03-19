[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "graph-paths"
version = "0.1.0"
description = "Personal Python project with Dijkstra and A* shortest path algorithms"
readme = "README.md"
authors = [{ name = "Your Name" }]
requires-python = ">=3.11"
dependencies = []

[project.optional-dependencies]
dev = ["pytest>=8.0"]

[tool.pytest.ini_options]
pythonpath = ["src"]
testpaths = ["tests"]

[tool.setuptools.packages.find]
where = ["src"]
