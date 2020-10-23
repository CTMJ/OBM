import numpy as np
from DiffusionModels.Graphs.WGraph import WGraph
from DiffusionModels.Models.HD import HDGraph
import DiffusionModels.Factor.Hamiltonian as Hamiltionians


class OBM(HDGraph, WGraph):  # 个人环境因素的影响模型

    def __init__(self, weight_matrix: np.ndarray):
        self.weight_matrix = weight_matrix
        self.wg = WGraph(self.weight_matrix)
        self.size = self.wg.size
        self.outDegrees = self.wg.outDegrees
        self.user_capacities = [10 for i in range(self.size)]
        self.interaction_rates = [2 * self.outDegrees[i] * self.user_capacities[i] for i in range(self.size)]
        self.Hamiltontian = Hamiltionians.createOBMHam(self.weight_matrix, self.interaction_rates, self.outDegrees,
                                                       self.user_capacities)
        self.kernel = Hamiltionians.createEvolutionKernel(self.Hamiltontian)

    def getNetworkState(self) -> np.ndarray:
        '''
        The OBM tracks the number of positive messages in the network.
        Thus a network state is not $\psi_i = 0$. Rather, it is $\psi_i = c_i/2$.
        '''
        return np.divide(self.user_capacities, 2)

    def getInfluenceOfUser(self, state: np.ndarray, user_index: int) -> float:
        return state[user_index] / self.user_capacities[user_index]
