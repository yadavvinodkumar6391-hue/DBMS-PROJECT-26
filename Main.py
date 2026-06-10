from dependency_graph import DependencyGraph
from cycle_detection import detect_cycle
from smt_verifier import verify
from hyper_polygraph import HyperPolygraph, add_predicate_hyperedge

# Build the plain dependency graph
G = DependencyGraph()
G.add_dependency("T1", "T2", "WR")
G.add_dependency("T2", "T3", "RW")
G.add_dependency("T3", "T1", "WR")
graph = G.get_graph()

# Cycle detection (structural check)
cycle = detect_cycle(graph)
if cycle:
    print("Cycle Found")
    print(cycle)

# Build HyperPolygraph and populate it from the dependency graph,
# then wire in any predicate hyperedges before verifying
hp = HyperPolygraph()
for node in graph.nodes():
    hp.add_vertex(node)
for u, v, data in graph.edges(data=True):
    hp.add_edge(u, v, data.get("type", ""))

# Example predicate hyperedge (add real ones here as needed)
add_predicate_hyperedge(hp, "T2", "T1", "age > 30")

# Export HyperPolygraph to NetworkX and verify
hp_graph = hp.to_networkx()
print(verify(hp_graph, isolation_level="SER"))
