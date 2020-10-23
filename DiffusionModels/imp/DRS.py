import networkx as nx
import numpy as np
from DiffusionModels.Models.OBM import OBM
from Test.OBMtest import OBMTest
import scipy.linalg as lin
import numpy as np


def DRS(G: OBM, k: int, h0: int) -> dict:
    print("DRS start")
    seedSize_msg = dict()
    seed_set = set()
    outDgreesList = G.outDegrees
    outDgreesDict = {}
    for o in range(len(outDgreesList)):
        outDgreesDict[o] = outDgreesList[o]
    for l in range(1, k):
        m = list(outDgreesDict.keys())[list(outDgreesDict.values()).index(max(list(outDgreesDict.values())))]
        seed_set.add(m)
        fm0 = [0 for i in range(G.size)]
        for n in list(seed_set):
            fm0[n] = h0
        fmc0 = []
        for f in range(len(fm0)):
            fmc0.append([fm0[f]])
        fmv0 = np.array(fmc0)
        fn = 0.0
        t = 120
        ft = np.dot(lin.expm(G.Hamiltontian * t), fmv0)
        '''if fn == ft.sum():
            break
            #t = t + 10
        '''
        fn = ft.sum()
        seedSize_msg[len(seed_set)] = fn
        print(seedSize_msg)
        outDgreesDict.pop(m)
    print("DRS end")
    return seedSize_msg
