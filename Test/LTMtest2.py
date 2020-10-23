import DiffusionModels.Models.LTM2 as LTM2
from DiffusionModels.Graphs.RD import RDGraph
import numpy as np
import networkx as nx
import time
import DataExtrraction.public as public
import matplotlib.pyplot as plt


class LTMTest2:
    def __init__(self, filePath, _time: int, beta: float = 0.5):
        self.RD = RDGraph(filePath)
        self.adjacency_matrix = self.RD.getAdjacency_matrix(0)
        self._outDegrees = self.RD.getOutDegrees(0)
        self._inDegrees = self.RD.getInDegrees(0)
        self.origin = list(public.DictToFlipKeyAndValue(public.ListToDict(self.RD.getSeedTime(_time))).values())
        self.node = list(public.DictToFlipKeyAndValue(public.ListToDict(self.RD.getNodeList())).values())
        self.beta = 0.5

    def getYLTM(self):
        return LTM2.lt_(self.adjacency_matrix, self._inDegrees, self.node, self.origin, self.beta)

    def draw(self, PicPath):
        i = self.getNextAllNode()
        a = self.adjacency_matrix
        color = []
        for j in range(0, a.shape[0]):
            color.append('b')
        for j in range(0, len(i)):
            color[int(i[j])] = 'r'
        g = nx.from_numpy_matrix(a)
        nx.draw(g, with_labels=True, node_color=color, node_size=1)
        plt.savefig(PicPath);
        plt.show()
