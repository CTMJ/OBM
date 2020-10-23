# HeatDiffusion

from DiffusionModels.Graphs.WGraph import WGraph
import DiffusionModels.Factor.Hamiltonian as Hamiltionians
import numpy as np


class HDGraph(WGraph): #traditional model  no user internal factor

    '''
    A `DiffusiveGraph` is a model that utilizes a graph state acted upon by a Hamiltonian operator.
    These are forms of weighted, directed, graphs.
    Note that the form of the Hamiltonian has drastic effects on the evolution of the network.
    The default implementation is a heat-diffusion model.
    '''

    def __init__(self, weight_matrix: np.ndarray):
        WGraph.__init__(self, weight_matrix)
        self.Hamiltonian = Hamiltionians.createHeatDiffusionDSNHam(weight_matrix)#哈密因子
        self.kernel = Hamiltionians.createEvolutionKernel(self.Hamiltonian)#热核初始值

    def evolve(self, state: np.ndarray) -> np.ndarray:
        '''
        Using the evolution kernel `self.kernel`,
        identify the evolved state of the network starting from `state`.
        '''
        return np.dot(self.kernel, state)

    def getNetworkState(self) -> np.ndarray:
        '''
        The Network state represents a network with exactly zero opinion for or against a topic.
        For an OBM, this is c_i/2. For heat-diffusion, this is an identically-zero state.
        When constructing a `diffusiveGraph`, make sure to implement the proper Network state!
        '''
        return np.zeros(self.size)

    def getNeutralState(self) -> np.ndarray:
        ''' The neutral state represents a network with exactly zero opinion for or against a topic. For an OBM, this is c_i/2. For heat-diffusion, this is an identically-zero state.
        When constructing a `DiffusiveGraph`, make sure to implement the proper neutral state!
        '''
        return np.zeros(self.size)

    def getInfluenceOfUser(self, state: np.ndarray, user_index: int) -> float:
        '''
        Return the degree of influence of a user from the state.
        This process may vary depending on the model.
        '''
        return state[user_index]
