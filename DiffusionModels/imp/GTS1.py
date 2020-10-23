from DiffusionModels.Models.OBM import OBM
from Test.OBMtest import OBMTest
import scipy.linalg as lin
import numpy as np


def GTS(G: OBM, t: int, h0: int, k: int):
    print("GTS start")
    seedSize_msg = {}
    seed_dict = {}
    seed_set = set()

    for i in range(G.size):
        f0 = [0 for i in range(G.size)]
        f0[i] = h0
        fc0 = []
        for f in range(len(f0)):
            fc0.append([f0[f]])
        fv0 = np.array(fc0)
        ft = np.dot(lin.expm(G.Hamiltontian * t), fv0)
        seed_dict[i] = ft.sum()
    for l in range(1, k):
        m = list(seed_dict.keys())[list(seed_dict.values()).index(max(list(seed_dict.values())))]
        seed_set.add(m)
        seed_dict.pop(m)
        fm0 = [0 for i in range(G.size)]
        for n in list(seed_set):
            fm0[n] = h0
        fmc0 = []
        for f in range(len(fm0)):
            fmc0.append([fm0[f]])
        fmv0 = np.array(fmc0)
        t1 = 120
        ft = np.dot(lin.expm(G.Hamiltontian * t1), fmv0)
        '''if fn == ft.sum():
                break
            t = t + 10
        '''
        seedSize_msg[len(seed_set)] = ft.sum()
        print(seedSize_msg)
    print("GTS end")
    return seedSize_msg
