import networkx as nx

class DependencyGraph:

    def __init__(self):
        self.graph = nx.DiGraph()

    def add_dependency(self, source, target, dep_type):
        self.graph.add_edge(
            source,
            target,
            type=dep_type
        )

    def get_graph(self):
        return self.graph
