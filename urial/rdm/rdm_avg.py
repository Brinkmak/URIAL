def rdm_avg(rdms):
    '''function to compute an average rdm from all
        RDMs in a given dictionary'''

    global DefaultListOrderedDict
    from collections import OrderedDict


    class DefaultListOrderedDict(OrderedDict):
        def __missing__(self,k):
            self[k] = []
            return self[k]


    from os.path import join as opj
    from scipy.io.matlab import loadmat
    import pandas as pd
    from collections import OrderedDict
    import pickle
    import numpy as np

    with open(rdms, 'rb') as f:
        dict_rdms = pickle.load(f)

    rdms = dict_rdms['rdm']
    conds = rdms[0].keys()

    for index, rdm in enumerate(rdms):
        rdms[index] = rdms[index].as_matrix()

    global rdm_avg

    rdm_avg = pd.DataFrame(np.mean(rdms, axis=0), columns=conds)

    return(rdm_avg)