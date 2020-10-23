from DiffusionModels.Models.OBM import OBM
from Test.OBMtest import OBMTest
import scipy.linalg as lin
import numpy as np


def GTSH(G: OBM, t: int, h0: int, k: int):
    print("GTS start")
    Time_msg = {}
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
    for t1 in range(0, 160):
        ft = np.dot(lin.expm(G.Hamiltontian * t1), fmv0)
        Time_msg[t1] = ft.sum()
        print(Time_msg)
    print("GTS end")
    return Time_msg
