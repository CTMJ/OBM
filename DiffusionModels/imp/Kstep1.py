from DiffusionModels.Models.OBM import OBM
import DiffusionModels.Constants.constants as cst
from Test.OBMtest import OBMTest
import scipy.linalg as lin
import numpy as np


def Kstep1(G: OBM, k: int, h0: int, t0: int, probe_temp=1) -> dict:
    print("kstep start")
    seedSize_msg = {}
    seed_sets = set()
    U = []
    for i in range(G.size):
        f0 = [0 for n in range(G.size)]
        f0[i] = h0
        fc0 = []
        for f in range(len(f0)):
            fc0.append([f0[f]])
        fv0 = np.array(fc0)
        ft = np.dot(lin.expm(G.Hamiltontian * t0), fv0)
        I1 = set()
        for j in range(G.size):
                fj = ft[j][0]
                if fj >= probe_temp:
                    I1.add(j)
        U.append(I1)
    R = set()
    for l in range(1, k):
        U_Isize = {}
        for u in U:
            I2 = u - R & u
            U_Isize[U.index(u)] = len(I2)
        m = list(U_Isize.keys())[list(U_Isize.values()).index(max(list(U_Isize.values())))]
        seed_sets.add(m)
        R = R | U[m]
        U[m] = set()
        fm0 = [0 for i in range(G.size)]
        for n in list(seed_sets):
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
            t = t + 10
        '''
        fn = ft.sum()
        seedSize_msg[len(seed_sets)] = fn
        print(seedSize_msg)
    print("kstep end")
    return seedSize_msg
