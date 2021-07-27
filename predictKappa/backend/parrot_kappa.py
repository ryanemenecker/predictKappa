"""
Backend of the IDR machine learning predictor. Based partly
on code from Dan Griffith's IDP-Parrot from the Holehouse lab
(specifically the test_unlabeled_data function in train_network.py).
"""

# import packages for predictor
import sys
import os

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader


# import modules that predictor depends on
from predictKappa.backend import encode_sequence
from predictKappa.backend import brnn_architecture


# set path for location of predictor. Using this in case I want to update the predictor or
# eventually make multiple predictors.
PATH = os.path.dirname(os.path.realpath(__file__))

# Setting predictor equal to location of weighted values.
predictor = "{}/networks/kappa_parrot_v2_072621.pt".format(PATH)

##################################################################################################
# hyperparameters used by when metapredict was trained. Manually setting them here for clarity.
##################################################################################################
# This is defined externally so its read in and loaded one time on the initial import
#


device = 'cpu'
hidden_size = 10
num_layers = 1
dtype = 'sequence'
num_classes = 1
encoding_scheme = 'onehot'
input_size = 20
problem_type = 'regression'

# set location of saved_weights for load_state_dict
saved_weights = predictor

###############################################################################
# Initialize network architecture using previously defined hyperparameters
###############################################################################
brnn_network = brnn_architecture.BRNN_MtO(input_size, hidden_size, num_layers, num_classes, device).to(device)
brnn_network.load_state_dict(torch.load(saved_weights, map_location=torch.device(device)))
###############################################################################

def change_for_input(seq):
    # first need to mod the sequence
    # so that it is just A, K, and D
    # did this to train PARROT-KAPPA
    # to minimize sequence space and waste
    # of focus on unimportant residue
    # differences


    # make empty string
    input_seq = ""
    # iterate through each aa in seq
    for aa in seq:
        # if aa D or E add a 'D'
        if aa == 'D' or aa == 'E':
            input_seq += 'D'
        # if aa K or R add 'K'
        elif aa == 'K' or aa == 'R':
            input_seq += 'K'
        # otherwise just add 'A'
        else:
            input_seq += 'A'
    
    return input_seq
    



def kappa_predict(sequence,  network=brnn_network, device=device, encoding_scheme=encoding_scheme):
    """
    The actual executing function for predicting the disorder of a sequence using metapredict.
    Returns a list containing predicted disorder values for the input sequence. 

    Arguments
    ---------
    sequence - the amino acid sequence to be predicted

    network - the network used by the predictor. See brnn_architecture BRNN_MtO for more info.

    device - String describing where the network is physically stored on the computer. 
    Should be either 'cpu' or 'cuda' (GPU).

    encoding_scheme - encoding scheme used when metapredict was trained. The encoding scheme was onehot.
    """

    # change sequence to ADK seq
    sequence = change_for_input(sequence)

    # set seq_vector equal to converted amino acid sequence that is a PyTorch tensor of one-hot vectors
    seq_vector = encode_sequence.one_hot(sequence)
    seq_vector = seq_vector.view(1, len(seq_vector), -1)

    # get output values from the seq_vector based on the network (brnn_network)
    output = round(float(network(seq_vector.float()).detach().numpy()[0]), 6)

    if output < 0:
        output = 0

    # return the prediction
    return output
