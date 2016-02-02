#!/opt/local/bin/python2.7
import matplotlib.pyplot as plt
import numpy as np
import pickle
import csv
from scipy.stats import pearsonr
# UTILITY FUNCTIONS ############################################################


# LOADING DATA #################################################################
# neuron data from pickled matrix
trial = pickle.load(open("trial1_day5.p", "r")) 

# trial can be accessed with trial[neuron_counter, frame_counter]
# counters start at 0
# eg: trial[1,2] gives the 2nd neuron's value during the 3rd time frame
#print trial[0, 0:len(trial[1])] # print data of neuron 1 for all time frames

n_neurons = len(trial) # total number of neurons
n_frames = len(trial[1]) # total number of frames
print "number of neurons recorded: ", n_neurons
print "number of frames recorded: ", n_frames

# how to access single neurons
#n1 = trial[1, 0:n_frames] # neuron 1 from frame 0 to max frame number
#n2 = trial[2, 0:n_frames]
#n3 = trial[3, 0:n_frames]
#corr = np.corrcoef([n1,n2,n3,n4]) # corr for neurons 1 - 4

# how to access a bunch of neurons at once
n0_50 = trial[0:50, 0:n_frames]
n25_30 = trial[25:30, 0:n_frames]
# TODO: make sure you actaully have the same number of frames for each neuron


# CALCULATING CORRELATION ######################################################
corr = np.corrcoef(n25_30) # for neuron 25 - 30
#corr = np.corrcoef(trial) # for all neurons
#print "corr: ", corr
for neuron in trial:
    print neuron

#x = 
#y =

# PLOTTING #####################################################################
# show correlation in a heatmap
fig, ax = plt.subplots()
# heatmap for correlation with fixed color range between 1 and -1
heatmap = ax.pcolor(corr, cmap=plt.cm.RdBu_r, vmin=-1, vmax=1) 
# add color bar of the heatmap to the right
plt.colorbar(heatmap) 

# set lables for all data points
column_labels = list(xrange(n_neurons)) # from 0 to total nr of neurons
row_labels = list(xrange(n_neurons))

# remove excess white space by setting border to data limit
plt.ylim(0, n_neurons)
plt.xlim(0, n_neurons)

# invert y-axis for a table-like look
ax.invert_yaxis()
ax.xaxis.tick_top()

# add labels
ax.set_xlabel('xlabel')
ax.set_ylabel('ylabel')

# Show plot
plt.show()
