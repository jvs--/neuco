#!/opt/local/bin/python2.7
"""
Calculates the event triggered average of neural response given sound cues.
"""
import matplotlib.pyplot as plt
import numpy as np
import pickle
import collections

# LOADING & UNPACKING DATA
# load neuron activation data from pickled matrix
trial = pickle.load(open("trial1_day5.p", "r")) 

# load sound data from pickled matrix
sound_data = pickle.load(open("foo.p"))
# unpack sound onset and offset frames from sound data
spk_on = sound_data["spk_scan"]["matrix"]
spk_off = sound_data["spk_scan_down"]["matrix"]


n_neurons = len(trial) # total number of neurons
n_frames = len(trial[1]) # total number of frames
#print "number of neurons recorded: ", n_neurons
#print "number of frames recorded: ", n_frames


# for every speaker gather the sound onset and offset frame numbers
on_frames = []
off_frames = []
for i in range(12): 
    # first index is (trial nr - 1)
    # second index is speaker nr 
    # last index only unpacks doubely wrapped list
    sound_on = [frame for frame,x in enumerate(spk_on[4][i][0]) if x == 1]
    sound_off = [frame for frame,x in enumerate(spk_off[4][i][0]) if x == 1]
    on_frames.append(sound_on[0])
    off_frames.append(sound_off[0])
# gather in a list of tuples of the form (onset, offset)
frames = zip(on_frames, off_frames)
print "Sound onset and off set frames: ", frames

# how to access a bunch of neurons at once
#n0_50 = trial[0:50, 0:n_frames]

# CALCULATING EVENT TRIGGERED AVERAGES 
def eta(trial, neuron, frames):
    # Average activation of indicated neuron across all frames
    # during sound played from each speaker
    n1 = trial[neuron, 0:n_frames]
    total_average = sum(n1)/n_frames
    #print "Average activation across all frames: ", total_average 
    
    data = []
    for sound_event in frames:
        duration = sound_event[1] - sound_event[0] # offset - onset of sound
        acti_during_sound = trial[neuron, sound_event[0]:sound_event[1]] 
        data.append(acti_during_sound)
    average_during_sound = sum(acti_during_sound)/duration
    #print "Average activation during sound: ", average_during_sound
    
    # PLOTTING 
    #fig = plt.figure()
    #plt.axhline(y=total_average, ls='--', c='black')
    #plt.axhline(y=average_during_sound, ls='--', c='red')
    #plt.boxplot(data, 0, '')
    #plt.ylabel('Activation')
    #plt.xlabel('Speaker')
    #plt.title('Average activation of neuron during sound')
    #plt.ylim([0, 3])
    #plt.show()
    
    return data

def eta_allneurons(trial, frames):
    averages = np.ndarray( shape=(688, 12), dtype = float)
    for neuron in xrange(len(trial)):
        average = eta(trial, neuron, frames)
        for speaker, values in enumerate(average):
            
            speaker_average = sum(values)
            #print speaker, speaker_average
            averages[neuron][speaker] = speaker_average
    #print "All event triggered averages: ", averages
    #print averages[15]
    #columns = sorted(set(column for subdict in averages.itervalues() for column in subdict))
    #print averages   
    # PLOTTING

    fig, ax = plt.subplots()
    # heatmap for correlation with fixed color range between 1 and -1
    heatmap = ax.pcolor(averages, cmap=plt.cm.RdBu_r,) 
    # add color bar of the heatmap to the right
    plt.colorbar(heatmap)
    #plt.axis('equal')
    plt.ylim(0, n_neurons)
    ax.set_xlabel('Speakers')
    ax.set_ylabel('Neuro #')
    plt.show()


#eta(trial, 72, frames) # a highly positive correlated neuron
#eta(trial, 15, frames) # a highly negative correlated neuron
#eta(trial, 313, frames)
#eta(trial, 124, frames)
eta_allneurons(trial, frames)

