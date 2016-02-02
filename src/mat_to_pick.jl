"""
Converts Matlab files to pickled python objects as there is some encoding issue 
with the Matlab files I am working on so it seems more reasonable to convert 
them. 
"""
using MAT
using PyCall
using DataFrames

@pyimport pylab
@pyimport numpy 
@pyimport pickle

vars = matread("All_TCMat_Scan_Analog_day5.mat") # read optical data

println(vars)

# println(vars["Trace_r"]) 
# Not smart :) Takes several minutes as we have 10 * 488 * 2000 something entries

# The data has a confusing form:
#
# trace_r dimension is 1 x 10, where 1 to 10 are the respective trials   
# We need to unpack this to get to a 488 x 2XXX which is #neurons x #frames
# Caution: not all recordings seem to have been done with the same nr of frames



# Julia seems to have a peculiar way to access arrays 
# it seems in a 2d array you can either use [i,j] to access an item or
# [k], where k runs from 1 to i*j
#nr_neuron = 1
#nr_frame = 1
#intensity = trial[nr_neuron, nr_frame] #the change of intensity in mean value 

# pickel data matricies from all 10 trials
trace_r = vars["Trace_r"]
for trial_nr = 1:10
    trial = trace_r["matrix"][trial_nr]
    filename = "trial$(trial_nr)_day5.p"
    pickle.dump(trial, open(filename, "w"))
end


