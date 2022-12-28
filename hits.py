import argparse
import networkx as nx
import matplotlib.pyplot as plt
import os

def use_library(graph_file_with_path:str):
    graph = nx.DiGraph()

    with open(graph_file_with_path) as f:
        lines = f.readlines()

    edges = [(line.split(',')[0],line.split(',')[-1].replace('\n','')) for line in lines]
    print(edges)

    graph.add_edges_from(edges)

    plt.figure(figsize =(10, 10))
    nx.draw_networkx(graph, with_labels = True)
    
    hubs, authorities = nx.hits(graph, max_iter = 1, normalized = True)
    # The in-built hits function returns two dictionaries keyed by nodes
    # containing hub scores and authority scores respectively.
    
    print("Hub Scores: ", hubs)
    print("Authority Scores: ", authorities)


if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser()

    parser.add_argument('--dataset', type=str, default='hw3dataset/graph_1.txt',
                        help='Dataset to use, please include the extension')

    args = parser.parse_args()    

    use_library(args.dataset)

