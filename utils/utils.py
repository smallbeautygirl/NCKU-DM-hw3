from utils.Graph import Graph


def init_graph(fname):
    with open(fname) as f:
        lines = f.readlines()

    graph = Graph()

    for line in lines:
        [parent, child] = line.strip().split(',')
        print([parent, child])
        graph.add_edge(parent, child)

    graph.sort_nodes()

    return graph