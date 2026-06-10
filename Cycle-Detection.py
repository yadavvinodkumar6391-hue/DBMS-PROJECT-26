import networkx as nx

def detect_cycle(graph):

    try:
        cycle = nx.find_cycle(graph)
        return cycle

    except nx.NetworkXNoCycle:
        return None
