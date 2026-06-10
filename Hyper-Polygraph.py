import networkx as nx

class HyperPolygraph:
    def __init__(self):
        self.vertices = set()
        self.edges = []
        self.hyperedges = []

    def add_vertex(self, txn):
        self.vertices.add(txn)

    def add_edge(self, source, target, dep_type):
        self.edges.append((source, target, dep_type))

    def add_hyperedge(self, choices):
        self.hyperedges.append(choices)

    def to_networkx(self):
        """
        Export to a nx.DiGraph for use with verify().
        Hyperedges are over-approximated: all candidate edges are added,
        which is conservative (may report violations that don't exist, but
        never misses real ones).
        """
        G = nx.DiGraph()
        for v in self.vertices:
            G.add_node(v)
        for src, tgt, dep_type in self.edges:
            G.add_edge(src, tgt, type=dep_type)
        for choices in self.hyperedges:
            for src, tgt, dep_type in choices:
                G.add_edge(src, tgt, type=dep_type)
        return G


def add_predicate_hyperedge(hp, reader, writer, predicate):
    hp.add_edge(reader, writer, f"PH:{predicate}")
