import DiffusionModels.imp.GTS1H as gts1h
from DiffusionModels.Models.OBM import OBM
from DataExtrraction.Generate import Common_matrix
import matplotlib.pyplot as plt
import DiffusionModels.Constants.constants as ct

filePath = ct.FILE_PATH_500
w = Common_matrix(filePath).getWeight_matrix(0)
G = OBM(w)
h0 = 10
t0 = 50
time_msg_gts5 = gts1h.GTSH(G, t0, h0, 5)
time_msg_gts10 = gts1h.GTSH(G, t0, h0, 10)
time_msg_gts50 = gts1h.GTSH(G, t0, h0, 50)
time_msg_gts100 = gts1h.GTSH(G, t0, h0, 100)
print("---drawing---")
x = list(time_msg_gts5.keys())
y_gts5 = list(time_msg_gts5.values())
y_gts10 = list(time_msg_gts10.values())
y_gts50 = list(time_msg_gts50.values())
y_gts100 = list(time_msg_gts100.values())
#plt.plot(x, y_rdm, label='Random Selection', color='red')
#plt.plot(x, y_drs, label='Degree Ranking Selection', color='blue')
#plt.plot(x, y_ks, label='kstep', color='orange')
plt.plot(x, y_gts5, label='gts 5', color='green')
plt.plot(x, y_gts10, label='gts 10', color='orange')
plt.plot(x, y_gts50, label='gts 50', color='blue')
plt.plot(x, y_gts100, label='gts 100', color='red')
plt.legend()
plt.ylabel("Message_Sum")
plt.xlabel("time")
PicPath = "E:/project/Experiment/TestResult/GTS500H.png"
plt.savefig(PicPath);
plt.show()
