
def page_rank_one_iter(graph, damping_factor:float):
    # damping factor 阻尼係數
    for node in graph.nodes:
        node.update_pagerank(damping_factor, len(graph.nodes))
    graph.normalize_pagerank()

def PageRank(graph, damping_factor:float, iteration=50):
    x=0
    while x < iteration:
        x+=1 
        page_rank_one_iter(graph, damping_factor)


