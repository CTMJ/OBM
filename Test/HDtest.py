from DiffusionModels.Graphs.RD import RDGraph
from DiffusionModels.Graphs.WGraph import WGraph
from DataExtrraction.Generate import Common_matrix
import DiffusionModels.Factor.Hamiltonian as ham
import matplotlib.pyplot as plt
import scipy.linalg as lin
import numpy as np


class HDTest:

    def __init__(self, time: int, filePath: str):
        self.time = time
        self.filePath = filePath
        self.RD = RDGraph(self.filePath)
        self.C_matrix = Common_matrix(self.filePath)
        self.userMsgSum = self.RD.getUserAndMessageSumVector(self.time)
        #self.adjacency_matrix = self.C_matrix.getAdjacency_matrix(self.time + self.RD.getMinTimeStamp())
        self.adjacency_matrix = self.C_matrix.getAdjacency_matrix(0)
        #self.weight_matrix = self.C_matrix.getWeight_matrix(self.time + self.RD.getMinTimeStamp())
        self.weight_matrix = self.C_matrix.getWeight_matrix(0)
        self.WG = WGraph(self.weight_matrix)
        self.H_DSN = ham.createHeatDiffusionDSNHam(self.adjacency_matrix, self.WG.outDegrees)
        self.H_USN = ham.createHeatDiffusionUSNHam(self.adjacency_matrix)

    def getMsgSumOrUserNumAndTimeDict(self) -> (dict, dict):
        msgSumAndTimeDict = {}
        userNumAndTimeDict = {}
        timeList = list(self.RD.getMessageSumAndTime().keys())
        for t in timeList[timeList.index(int(self.time)):]:
            TuserAList = self.RD.getUserAList(t)
            ft = np.dot(lin.expm(self.H_DSN * (t - self.time)), self.userMsgSum)
            msgSumAndTimeDict[t] = ft.sum()
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
        plt.savefig(PicPath);plt.show()
