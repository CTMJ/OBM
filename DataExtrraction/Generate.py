import numpy as np
from DataExtrraction.FileController import fileController


class Common_matrix:
    def __init__(self, filePath: str):
        self.filePath = filePath
        self.fileController = fileController(self.filePath)

    def getWeight_matrix(self, t0=0) -> np.ndarray:
        users = self.fileController.getUserListSort()
        influence_matrix = np.zeros((len(users), len(users)))
        data = self.fileController.getUserAndTimeList()
        for d in data:
            userA = d[0]
            userB = d[1]
            timestamp = d[2]
            if t0 == 0 or (t0 != 0 and timestamp < t0):
                influence_matrix[users.index(userB)][users.index(userA)] += 1
                print(users.index(userB), userB, users.index(userA), userA, timestamp, t0)
        total_influences = influence_matrix.sum(axis=1)
        weight_matrix = np.array(
            [[influence_matrix[i][j] / total_influences[j] if total_influences[j] != 0 else 0 for j in
              range(len(total_influences))] for i in range(len(total_influences))])
        return weight_matrix

    def getAdjacency_matrix(self, t0=0) -> np.ndarray:
        users = self.fileController.getUserListSort()
        adjacency_matrix = np.zeros((len(users), len(users)))
        data = self.fileController.getUserAndTimeList()
        for d in data:
            userA = d[0]
            userB = d[1]
            timestamp = int(d[2])
            if t0 == 0 or (t0 != 0 and timestamp < t0):
                adjacency_matrix[users.index(userA)][users.index(userB)] = 1
        return adjacency_matrix
