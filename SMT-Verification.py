from z3 import *

def verify(graph, isolation_level="SER"):
    solver = Solver()
    order = {}

    for node in graph.nodes():
        order[node] = Int(f"ord_{node}")

    for u, v, data in graph.edges(data=True):
        dep_type = data.get("type", "")

        # WR, WW, SO always impose a strict ordering constraint
        if dep_type in ("WR", "WW", "SO"):
            solver.add(order[u] < order[v])

        # RW (anti-dependency): only forces ordering under full serializability.
        # Under snapshot isolation, RW edges do not directly impose order.
        elif dep_type == "RW":
            if isolation_level == "SER":
                solver.add(order[u] < order[v])

        # Predicate hyperedges: treat as ordering constraints regardless of level
        elif dep_type.startswith("PH:"):
            solver.add(order[u] < order[v])

    if solver.check() == sat:
        return "Serializable"
    return "Isolation Violation"
