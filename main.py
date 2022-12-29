import time
from utils.utils import init_graph
from utils.hits import HITS
from utils.page_rank import PageRank
from utils.sim_rank import SimRank
from utils.simiarity import Similarity

import numpy as np
import os
import argparse

def output_HITS(iteration, graph, result_dir, fname):
    authority_fname = '_HITS_authority.txt'
    hub_fname = '_HITS_hub.txt'

    HITS(graph, iteration)
    auth_list, hub_list = graph.get_auth_hub_list()
    print()
    print('Authority:')
    print(auth_list)
    path = os.path.join(result_dir, fname)
    os.makedirs(path, exist_ok=True)
    np.savetxt(os.path.join(path, fname + authority_fname), auth_list, fmt='%.3f', newline=" ")
    print('Hub:')
    print(hub_list)
    print()
    np.savetxt(os.path.join(path, fname + hub_fname), hub_list, fmt='%.3f', newline=" ")


def output_PageRank(iteration, graph, damping_factor, result_dir, fname):
    pagerank_fname = '_PageRank.txt'

    PageRank(graph, damping_factor, iteration)
    pagerank_list = graph.get_pagerank_list()
    print('PageRank:')
    print(pagerank_list)
    print()
    path = os.path.join(result_dir, fname)
    os.makedirs(path, exist_ok=True)
    np.savetxt(os.path.join(path, fname + pagerank_fname), pagerank_list, fmt='%.3f', newline=" ")


def output_SimRank(iteration, graph, decay_factor, result_dir, fname):
    simrank_fname = '_SimRank.txt'

    SimRank(graph, sim, iteration)
    ans = sim.get_sim_matrix()
    print('SimRank:')
    print(ans)
    print()
    path = os.path.join(result_dir, fname)
    os.makedirs(path, exist_ok=True)
    np.savetxt(os.path.join(path, fname + simrank_fname), ans, delimiter=' ', fmt='%.3f')


if __name__ == '__main__':
    # Parse command line arguments
    parser = argparse.ArgumentParser()

    parser.add_argument('--dataset', type=str, default='hw3dataset/graph_1.txt',
                        help='Dataset to use, please include the extension')
    parser.add_argument('--damping_factor', type=float, default=0.15,
                        help='Damping factor (float)')
    parser.add_argument('--decay_factor', type=float, default=0.9,
                        help='Decay factor (float)')
    parser.add_argument('--iteration', type=int, default=1,
                        help='Iteration (int)')
    parser.add_argument('--output', type=int, default=50,
                        help='Iteration (int)')
    args = parser.parse_args() 

    graph = init_graph(args.dataset)
    sim = Similarity(graph, args.decay_factor)

    s = time.time()
    output_HITS(args.iteration, graph, 'result', args.dataset.split('/')[-1].split('.')[0])
    e = time.time()
    print(f'{args.dataset} HITS: {e-s}')
    s = time.time()
    output_PageRank(args.iteration, graph, args.damping_factor, 'result', args.dataset.split('/')[-1].split('.')[0])
    e = time.time()
    print(f'{args.dataset} PageRank: {e-s}')
    s = time.time()
    output_SimRank(args.iteration, graph, args.decay_factor, 'result', args.dataset.split('/')[-1].split('.')[0])
    e = time.time()
    print(f'{args.dataset} SimRank: {e-s}')