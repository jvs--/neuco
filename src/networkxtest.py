#!/opt/local/bin/python2.7
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pickle

def built_graph(graph):
    # create networkx graph
    G=nx.Graph()
    # add nodes
    for node1, weights in enumerate(graph):
        #print node1
        #TODO remove node's connection to itself as it's always one with corr
        G.add_node(node1)
        #print weights
        # add edges and weights
        for node2, weight in enumerate(weights):
            #print node1, node2, weight
            G.add_edge(node1, node2, weight=weight)

    # draw graph
    #pos = nx.shell_layout(G)
    #nx.draw(G, pos)
    # show graph
    #plt.show()
    
    # write graph to GML file
    nx.write_gml(G,"trial5_day5.gml")


# load neuron data from pickled matrix
trial = pickle.load(open("trial5_day5.p", "r")) 
#n_neurons = len(trial) # total number of neurons
#n_frames = len(trial[1]) # total number of frames

corr = np.corrcoef(trial) # calculate correlation

# draw example
graph = corr
built_graph(graph)
