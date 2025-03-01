import numpy as np
from samplers.dynamic_nested import NestedSampler 
from likelihood import Likelihood as lik 
from utils.plotter import plot

data = np.load('data.npy')

# Define the sampler parameters
paramranges = np.asarray( [ [0.,10.],[0.,10.] ] )
nlive = 100

# Initiate the sampler
dns = NestedSampler(data,paramranges,nlive)

tol = 0.1
feedback_freq = 100
# Run the sampler
dns.dynamic_nested()

# plot(1000)

