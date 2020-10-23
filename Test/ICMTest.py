import DiffusionModels.Models.ICM2 as ICM
from DiffusionModels.Graphs.RD import RDGraph
from DataExtrraction.Generate import Common_matrix
import networkx as nx
import time


class ICMTest:
    def __init__(self, filePath, dt: int, steps=0):
        self.filePath = filePath
        self.RD = RDGraph(self.filePath)
        self.Common_matrix = Common_matrix(self.filePath)
        self.nodeList = self.RD.getNodeList()
        self.edgeList = self.RD.getEdgeList()
        self.seeds = self.RD.getSeedTime(dt)
        self.adjacency_matrix = self.Common_matrix.getAdjacency_matrix(0)
        self.G = nx.DiGraph(self.adjacency_matrix)
        _ = self.G.add_edges_from(self.edgeList)
        _ = self.G.add_nodes_from(self.nodeList)
        self.layers = ICM.independent_cascade(self.G, self.seeds, steps)

    def getSeedNum(self):
        return len(self.seeds)

    def getLayers(self):
        del self.layers[-1]
        return self.layers

    def getLengths(self):
        length = 0
        for i in range(len(self.layers)):
            length = length + len(self.layers[i])
        lengths = length - len(self.layers[0])  # 获得子节点的激活节点的个数（长度）
        return lengths

    def draw(self):
        start = time.time()
        layers = self.getLayers()
        lengths = self.getLengths()
        end = time.time()
        print(layers)
        print(lengths)
        print('Running time: %s Seconds' % (end - start))  # 输出代码运行时间
