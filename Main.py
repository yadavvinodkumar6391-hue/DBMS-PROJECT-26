from dependency_graph import DependencyGraph
from cycle_detection import detect_cycle
from smt_verifier import verify

G = DependencyGraph()

G.add_dependency("T1","T2","WR")
G.add_dependency("T2","T3","RW")
G.add_dependency("T3","T1","WR")

graph = G.get_graph()

cycle = detect_cycle(graph)

if cycle:
    print("Cycle Found")
    print(cycle)

print(
    verify(graph)
)
