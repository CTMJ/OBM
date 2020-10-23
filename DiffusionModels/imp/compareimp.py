import DiffusionModels.imp.Random as rdm
import DiffusionModels.imp.DRS as drs
import DiffusionModels.imp.Kstep1 as ks
import DiffusionModels.imp.GTS1 as gts1
#import DiffusionModels.imp.GTS2 as gts2
from DiffusionModels.Models.OBM import OBM
from DataExtrraction.Generate import Common_matrix
import DiffusionModels.Factor.Hamiltonian as ham
from DiffusionModels.Graphs.RD import RDGraph
from DiffusionModels.Graphs.WGraph import WGraph
import matplotlib.pyplot as plt
import scipy.linalg as lin
import numpy as np
import matplotlib.pyplot as plt
import DiffusionModels.Constants.constants as ct

filePath = ct.FILE_PATH_500
w = Common_matrix(filePath).getWeight_matrix(0)
G = OBM(w)
k = 100
h0 = 10
t0 = 50
seedSize_msg_rdm = rdm.Random(G, k, h0)
seedSize_msg_drs = drs.DRS(G, k, h0)
seedSize_msg_gts = gts1.GTS(G, t0, h0, k)
seedSize_msg_ks = ks.Kstep1(G, k, h0, t0)
print("---drawing---")
x = list(seedSize_msg_ks.keys())
y_rdm = list(seedSize_msg_rdm.values())
y_drs = list(seedSize_msg_drs.values())
y_gts1 = list(seedSize_msg_gts.values())
y_ks = list(seedSize_msg_ks.values())
plt.plot(x, y_rdm, marker='o', markevery=5, label='Random Selection', color='blue', linestyle='-')
plt.plot(x, y_drs, marker='s', markevery=5, label='Degree Ranking Selection', color='green', linestyle='-')
plt.plot(x, y_ks, marker='v', markevery=5, label='K-Step Greedy Selection', color='orange', linestyle='-')
plt.plot(x, y_gts1,marker='d', markevery=5, label='GTS Greedy Selection', color='red', linestyle='-')
plt.legend()
plt.ylabel("global topical support(message)")
plt.xlabel("Seed Set Size")
PicPath = "E:/project/Experiment/TestResult/ks500x50.png"
plt.savefig(PicPath);
plt.show()
