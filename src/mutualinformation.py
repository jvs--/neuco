#!/opt/local/bin/python2.7
import matplotlib.pyplot as plt
import numpy as np
import pickle
from sklearn.metrics.cluster import adjusted_mutual_info_score

def mutual_information(hgram):
    """ Mutual information for joint histogram
    """
    pxy = hgram / float(np.sum(hgram)) # Convert to probability
    px = np.sum(pxy, 1) # marginal for x over y
    py = np.sum(pxy, 0) # marginal for y over x
    px_py = px[:, None] * py[None, :] # Broadcast to multiply marginals
    nzs = pxy > 0 # Only non-zero pxy values contribute to the sum
    return np.sum(pxy[nzs] * np.log(pxy[nzs] / px_py[nzs]))




#l1 = [1, 2, 2, 2, 3, 4, 5, 6]
#l2 = [1, 2, 2, 2, 3, 4, 5, 6]
#print mutual_info_score(l1,l2)

# LOADING DATA #################################################################
# neuron data from pickled matrix
trial = pickle.load(open("trial1_day5.p", "r")) 

n_neurons = len(trial) # total number of neurons
n_frames = len(trial[1]) # total number of frames
#print "number of neurons recorded: ", n_neurons
#print "number of frames recorded: ", n_frames

# how to access single neurons
#n2 = trial[2, 0:n_frames]

# how to access a bunch of neurons at once
n0_50 = trial[0:15, 0:n_frames]


MI = []
for neuron1 in n0_50:
    for neuron2 in n0_50:
        score = adjusted_mutual_info_score(neuron1, neuron2)
        print neuron1
        print neuron2
        print score
        MI.append(score)

print MI
        