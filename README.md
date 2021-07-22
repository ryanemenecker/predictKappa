predictKappa
==============================

# predictKappa - close to kappa, but a lot faster.

**predictKappa** provides a Python API for predicting kappa values of protein sequences. Kappa is a value that describes the charge asymmetry of a sequence and is known to have an impact on IDR behavior (see: *Conformations of intrinsically disordered proteins are influenced by linear sequence distributions of oppositely charged residues* Das, R.K. & Pappu, R.V. (2013) PNAS 110, 33, pp 13392 - 13397). However, kappa calculations are computationally expensive and fairly slow. To bypass this, we generated a bunch of sequences with a broad range of fractions of charged residues, net charge per residue, and length, and calculated their kappa values the old school way. We then input these sequences and their corresponding known kappa values into PARROT (see https://github.com/idptools/parrot), which generated a bidirectional recurrent neural network (BRNN) that predicts kappa values of protein sequences.

## How accurate is predictKappa?

The current implementation (July 22, 2021) has an error rate of about 4.5%. We plan on adding more sequences to our training set and making better networks in the future.

## Using predictKappa

The first thing you need to do is install predictKappa, which is currently only available on GitHub (maybe on PyPi some day...).

To clone the GitHub repository and gain the ability to modify a local copy of the code, run

    $ git clone https://github.com/ryanemenecker/predictKappa.git
    $ cd predictKappa
    $ pip install .


Once installed, in Python simply import predictKappa

    from predictKappa import predict

Now you can predict kappa from any protein sequence by using the predict.kappa() function.

    predict.kappa('KKKKKKKKKKKKEKKEKEKKEEKKEKEKEKEKEKKEEEEEEEEEEEEEEE')

    0.443426


The actual kappa value is 0.453 (according to CIDER, see http://pappulab.wustl.edu/CIDER/analysis/). That's pretty close!
