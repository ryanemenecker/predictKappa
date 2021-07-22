##
## pred_kappa.py
## 
## pred_kappa.py contains all the user-facing function associated with kappaPredict. If a new function is added it should be included
## here and added to the __all__ list
## 

##Handles the primary functions


__all__ =  ['kappa']
 
import os
import sys


# note - we imort packages below with a leading _ which means they are ignored in the import

#import protfasta to read .fasta files
import protfasta as _protfasta

# import stuff for IDR predictor from backend. Note the 'as _*' hides the imported
# module from the user
#from predictKappa.backend.parrot_kappa import kappa_predict as _kappa_predict
from predictKappa.backend.parrot_kappa import kappa_predict as _kappa_predict
from predictKappa.backend import kappa_tools as _kappa_tools

# stuff for uniprot from backend
from predictKappa.backend.uniprot_predictions import fetch_sequence as _fetch_sequence
from predictKappa.kappa_exceptions import KappaError



def kappa(sequence):
    """
    Function to return kappa of a single input sequence. Returns the
    predicted values as a float.

    Parameters
    ------------

    sequence : str 
        Input amino acid sequence (as string) to be predicted.

    Returns
    --------
    
    Float
        Returns a float of the kappa value (predicted)

    """
    # make all residues upper case 
    sequence = sequence.upper()

    # return predicted values of disorder for sequence
    return _kappa_predict(sequence)
