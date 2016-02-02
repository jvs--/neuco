#!/opt/local/bin/python2.7
"""
Takes a pickled file of neuron activations, calculates correlations between them
and makes them into a graph in GML format to be opened with graph visualization 
softwares like Gephi.  
"""
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pickle

def built_graph(graph):
    G = nx.Graph()  # create networkx graph
    # add nodes
    for node1, weights in enumerate(graph):
        #TODO remove node's connection to itself as it's always one with corr
        G.add_node(node1)
        # add edges and weights
        for node2, weight in enumerate(weights):
            G.add_edge(node1, node2, weight=weight)
    return G


# load neuron data from pickled matrix
file_name = "trial1_day5.p"
trial = pickle.load(open(file_name, "r")) 
#n_neurons = len(trial) # total number of neurons
#n_frames = len(trial[1]) # total number of frames

corr = np.corrcoef(trial) # calculate correlation
graph = built_graph(corr) # make graph out of it
nx.write_gml(graph,"trial1_day5.gml") # write graph to GML file