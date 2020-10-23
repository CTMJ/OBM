import random as rdm
import networkx as nx
from DiffusionModels.Models.OBM import OBM
from Test.OBMtest import OBMTest
import scipy.linalg as lin
import numpy as np


def Random(G: OBM, k: int, h0: int):
    print("Random start")
    seedSize_msg = dict()
    seed_set = set()
    fm0 = [0 for i in range(G.size)]
    G_size_list = list(range(G.size))
    for l in range(1, k):
        r = rdm.sample(G_size_list, 1)[0]
        seed_set.add(r)
        for n in list(seed_set):
            fm0[n] = h0
        fmc0 = []
        for f in range(len(fm0)):
            fmc0.append([fm0[f]])
        fmv0 = np.array(fmc0)
        t = 120
        ft = np.dot(lin.expm(G.Hamiltontian * t), fmv0)
        '''if fn == ft.sum():
            break
        t = t + 10
        '''
        fn = ft.sum()
        seedSize_msg[len(seed_set)] = fn
        print(seedSize_msg)
        G_size_list.remove(r)
    print("Random end")
    return seedSize_msg
