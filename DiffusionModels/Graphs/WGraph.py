import numpy as np


class WGraph:
    '''
    This is a primitive Graph that contains universal weighted, directed graph properties
    for OBM, HD and ABM, including:
    - `self.size`: the number of vertices in the graph. 点
    - `self.adjacency_matrix`
    - `self.weight_matrix`
    - `self.outdegrees` #传出
    - `self.indegrees`  #收到
    '''

    def __init__(self, weight_matrix: np.ndarray):
        self.size = weight_matrix.shape[0]
        self.adjacency_matrix = np.array(
            [[1 if weight_matrix[i][j] != 0 else 0 for j in range(self.size)] for i in range(self.size)])
        self.weight_matrix = weight_matrix
        self.outDegrees = [np.sum([self.adjacency_matrix[i][j] for j in range(self.size)]) for i in range(self.size)]
        self.inDegrees = [np.sum([self.adjacency_matrix[j][i] for j in range(self.size)]) for i in range(self.size)]
