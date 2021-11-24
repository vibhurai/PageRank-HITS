from src.utils.utils import init_graph
from src.HITS import HITS
from src.PageRank import PageRank
from src.SimRank import SimRank
from src.Similarity import Similarity
from optparse import OptionParser
import numpy as np
import os


def output_HITS(iteration, graph, result_dir, fname):
    authority_fname = '_HITS_authority.txt'
    hub_fname = '_HITS_hub.txt'

    HITS(graph, iteration)
    auth_list, hub_list = graph.get_auth_hub_list()
    print('Authority:')
    print(auth_list[1:15])

    auth_list.sort(reverse=True)
    hub_list.sort(reverse=True)

    path = os.path.join(result_dir, fname)
    os.makedirs(path, exist_ok=True)

    with open(os.path.join(path, fname + authority_fname), 'w') as f:
        for idx, i in enumerate(auth_list):
            f.write("{0} {1}\n".format(idx+1, i))

    print('\n\nHub:')
    print(hub_list[1:15])
    with open(os.path.join(path, fname + hub_fname), 'w') as f:
        for idx, i in enumerate(hub_list):
            f.write("{0} {1}\n".format(idx+1, i))

# def output_HITS(iteration, graph, result_dir, fname):
#     authority_fname = '_HITS_authority.txt'
#     hub_fname = '_HITS_hub.txt'

#     HITS(graph, iteration)
#     auth_list, hub_list = graph.get_auth_hub_list()
#     print('Authority:')
#     print(auth_list[1:15])

#     auth_list.sort(reverse=True)
#     hub_list.sort(reverse=True)

#     path = os.path.join(result_dir, fname)
#     os.makedirs(path, exist_ok=True)

#     with open(os.path.join(path, fname + authority_fname), 'w') as f:
#         f.write("%s\n" % auth_list)

#     print('\n\nHub:')
#     print(hub_list[1:15])

#     with open(os.path.join(path, fname + hub_fname), 'w') as f:
#         f.write("%s\n" % hub_list)


# def output_PageRank(iteration, graph, damping_factor, result_dir, fname):
    # pagerank_fname = '_PageRank.txt'

    # PageRank(graph, damping_factor, iteration)
    # pagerank_list = graph.get_pagerank_list()

    # pagerank_list.sort(reverse=True)

    # print('\n\nPageRank:')
    # print(pagerank_list[1:15])
    # print()
    # path = os.path.join(result_dir, fname)
    # os.makedirs(path, exist_ok=True)
    # with open(os.path.join(path, fname + pagerank_fname), 'w') as f:
    #     f.write("%s\n" % pagerank_list)


def output_PageRank(iteration, graph, damping_factor, result_dir, fname):
    pagerank_fname = '_PageRank.txt'

    PageRank(graph, damping_factor, iteration)
    pagerank_list = graph.get_pagerank_list()

    pagerank_list.sort(reverse=True)

    print('\n\nPageRank:')
    print(pagerank_list[1:15])
    print()
    path = os.path.join(result_dir, fname)
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, fname + pagerank_fname), 'w') as f:
        for idx, i in enumerate(pagerank_list):
            f.write("{0} {1}\n".format(idx+1, i))


if __name__ == '__main__':

    optparser = OptionParser()
    optparser.add_option('-f', '--input_file',
                         dest='input_file',
                         help='CSV filename',
                         default='dataset/links.txt')
    optparser.add_option('--damping_factor',
                         dest='damping_factor',
                         help='Damping factor (float)',
                         default=0.15,
                         type='float')
    optparser.add_option('--decay_factor',
                         dest='decay_factor',
                         help='Decay factor (float)',
                         default=0.9,
                         type='float')
    optparser.add_option('--iteration',
                         dest='iteration',
                         help='Iteration (int)',
                         default=500,
                         type='int')

    (options, args) = optparser.parse_args()

    file_path = options.input_file
    iteration = options.iteration
    damping_factor = options.damping_factor
    decay_factor = options.decay_factor

    result_dir = 'result'
    fname = file_path.split('/')[-1].split('.')[0]

    fileobj = open(
        ".\\relevant_docs.txt")

    lines_original = []
    for line in fileobj:
        lines_original.append(line.strip())

    with open(file_path) as f:
        lines = f.readlines()

        with open(os.path.join(".", "hub_links.txt"), 'w') as f0:
            for line in lines_original:
                for _ in lines:
                    if(_.find(line) != -1):
                        f0.write("%s" % _)

    file = os.path.join(
        ".", "hub_links.txt")
    graph = init_graph(file)

    output_HITS(iteration, graph, result_dir, "hub_links")
    output_PageRank(iteration, graph, damping_factor, result_dir, fname)
