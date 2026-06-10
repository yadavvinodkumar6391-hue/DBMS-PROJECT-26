class HyperPolygraph:

    def __init__(self):
        self.vertices = set()
        self.edges = []
        self.hyperedges = []

    def add_vertex(self, txn):
        self.vertices.add(txn)

    def add_edge(self, source, target, dep_type):
        self.edges.append(
            (source, target, dep_type)
        )

    def add_hyperedge(self, choices):
        self.hyperedges.append(choices)
