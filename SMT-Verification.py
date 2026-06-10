from z3 import *

def verify(graph):

    solver = Solver()

    order = {}

    for node in graph.nodes():

        order[node] = Int(
            f"ord_{node}"
        )

    for u, v in graph.edges():

        solver.add(
            order[u] < order[v]
        )

    if solver.check() == sat:
        return "Serializable"

    return "Isolation Violation"
