
def sim_rank_one_iter(graph, sim):
    for node1 in graph.nodes:
        for node2 in graph.nodes:
            new_SimRank = sim.calculate_SimRank(node1, node2)
            sim.update_sim_value(node1, node2, new_SimRank)
            # print(node1.label, node2.label, new_SimRank)

    sim.replace_sim()


def SimRank(graph, sim, iteration=100):
    x=0
    while x < iteration:
        x+=1 
        sim_rank_one_iter(graph, sim)
