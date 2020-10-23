from DataExtrraction.Generate import Common_matrix
import DiffusionModels.Factor.Hamiltonian as ham
from DiffusionModels.Graphs.RD import RDGraph
from DiffusionModels.Graphs.WGraph import WGraph
import matplotlib.pyplot as plt
import scipy.linalg as lin
import numpy as np
import random as rdm


class OBMTest:

    def __init__(self, time: int, filePath: str):
        self.time = time
        self.filePath = filePath
        self.RD = RDGraph(self.filePath)
        self.minTimeStamp = self.RD.getMinTimeStamp()
        self.C_matrix = Common_matrix(self.filePath)
        self.userMsgSum = self.RD.getUserAndMessageSumVector(self.time)
        #self.weight_matrix = self.C_matrix.getWeight_matrix(self.time + self.minTimeStamp)
        self.weight_matrix = self.C_matrix.getWeight_matrix(0)
        self.WG = WGraph(self.weight_matrix)
        #self.user_capacities = self.WG.inDegrees
        self.user_capacities = [rdm.randint(10, 50) for i in range(self.WG.size)]
        self.interaction_rates = [2 * self.WG.outDegrees[i] * self.user_capacities[i] for i in range(self.WG.size)]
        self.outDegrees = [self.WG.outDegrees[i] for i in range(self.WG.size)]
        self.H_OBM = ham.createOBMHam(self.weight_matrix, self.interaction_rates, self.outDegrees, self.user_capacities)

    def getMsgSumOrUserNumAndTimeDict(self) -> (dict, dict):
        msgSumAndTimeDict = {}
        userNumAndTimeDict = {}
        timeList = list(self.RD.getMessageSumAndTime().keys())
        for t in timeList[timeList.index(int(self.time)):]:
            TuserAList = self.RD.getUserAList(t)
            ft = np.dot(lin.expm(self.H_OBM * (t - self.time)), self.userMsgSum)
            msgSumAndTimeDict[t] = ft.sum()
            #np.where([ft == 0], 0, 1)
            #un1 = ft.sum()
            ftl = ft.tolist()
            un = []
            for j in range(len(ftl)):
                fu = ftl[j][0]
                if fu != 0:
                    un.append(self.RD.getNodeList()[j])
            un.extend(TuserAList)
            un = list(set(un))
            ut = len(un)
            userNumAndTimeDict[t] = ut
        return msgSumAndTimeDict, userNumAndTimeDict

    def getMsgSumAndTimeDict(self) -> dict:
        return self.getMsgSumOrUserNumAndTimeDict()[0]

    def getUserNumAndTimeDict(self) -> dict:
        return self.getMsgSumOrUserNumAndTimeDict()[1]

    def drawMsgSumAndTime(self, PicPath):
        print("---drawing---")
        x = list(self.getMsgSumAndTimeDict().keys())
        y = list(self.getMsgSumAndTimeDict().values())
        plt.plot(x, y)
        print("finish")
        plt.savefig(PicPath);
        plt.show()

    def getH_OBM(self):
        return self.H_OBM
