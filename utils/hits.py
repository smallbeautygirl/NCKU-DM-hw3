
def hits_one_iter(graph):

    for node in graph.nodes:
        node.update_auth()

    for node in graph.nodes:
        node.update_hub()

    graph.normalize_auth_hub()


def HITS(graph, iteration=50):
    x=0
    while x < iteration:
        x+=1 
        hits_one_iter(graph)
