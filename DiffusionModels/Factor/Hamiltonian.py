import numpy as np
import DiffusionModels.Constants.constants as cst
import math
import scipy.linalg as lin


def createHeatDiffusionUSNHam(adjacency_matrix: np.ndarray) -> np.ndarray:
    '''This creates a Hamiltonian where heat-diffusion is simple:
    interaction rates perfectly counter the effects of vertex outdegrees,
    and information capacity for each user is set to 1.
    These combine to assume a heat-diffusive process on a weighted, directed graph.
    '''
    rank = len(adjacency_matrix)
    Hamiltonian = np.zeros(adjacency_matrix.shape)
    for i in range(rank):
        for j in range(rank):
            if i == j:
                num = 0
                for k in range(rank):
                    if k != i:
                        num += adjacency_matrix[i][k]
                Hamiltonian[i][j] = -num
            else:
                Hamiltonian[i][j] = adjacency_matrix[i][j]
    return Hamiltonian


def createHeatDiffusionDSNHam(adjacency_matrix: np.ndarray, outdegrees: np.ndarray) -> np.ndarray:
    '''This creates a Hamiltonian where heat-diffusion is simple:
    interaction rates perfectly counter the effects of vertex outdegrees,
    and information capacity for each user is set to 1.
    These combine to assume a heat-diffusive process on a weighted, directed graph.
    '''
    rank = len(adjacency_matrix)
    Hamiltonian = np.zeros(adjacency_matrix.shape)
    for i in range(rank):
        for j in range(rank):
            if i == j:
                sum = 0
                for k in range(rank):
                    sum += adjacency_matrix[i][k]
                if sum == 0:
                    Hamiltonian[i][j] = 0
                else:
                    Hamiltonian[i][j] = -1
            else:
                if outdegrees[j] == 0:
                    Hamiltonian[i][j] = 0
                else:
                    Hamiltonian[i][j] = adjacency_matrix[i][j] / outdegrees[j]
    return Hamiltonian


def createOBMHam(weight_matrix: np.ndarray, interaction_rates: np.ndarray, vertex_outdegrees: np.ndarray, vertex_capacities: np.ndarray) -> np.ndarray:
    '''
    The current literature for the OBM is based on a pair of coupled Markov processes
    that represent the exchange of messages for and against a topic in a social network.
    These interactions are captured by several effects:
    - User-user trust is captured via weight_matrix (n,n)
    - The frequency a user interacts with peers is captured via interaction_rates (n)
    - The number of followers a user has is vertex_outdegrees (n)
    - The number of messages in the memory of a user is vertex_capacities (n)
    The literature refers to these quantities by:
    - weight_matrix: w_{ij}
    - interaction_rates: r_i
    - vertex_outdegrees: d_i
    - vertex_capacities: c_i
    '''
    rank = len(weight_matrix)
    Hamiltonian = np.zeros(weight_matrix.shape)
    for i in range(rank):
        for j in range(rank):
            if i == j:
                if vertex_outdegrees[i] == 0 or vertex_capacities[i] == 0:
                    Hamiltonian[i][j] = 0
                else:
                    Hamiltonian[i][j] = -(
                                interaction_rates[i] / (vertex_outdegrees[i] * vertex_capacities[i])) * np.sum(
                        [(vertex_capacities[k] / (vertex_capacities[i] + vertex_capacities[k])) * weight_matrix[k][i]
                         for k in range(rank)])
                ''' The fact that weight_matrix[k][i] is not weight_matrix[i][k] worries me:
                This suggests that the OBM only resembles heat-diffusion on a symmetric graph (w[i][j] = w[j][i]). Perhaps the OBM is more different from heat-diffusion than we expected. '''
            else:
                if vertex_outdegrees[i] == 0 or vertex_capacities[i] == 0:
                    Hamiltonian[i][j] = 0
                else:
                    Hamiltonian[i][j] = (interaction_rates[i] / (
                                vertex_outdegrees[i] * (vertex_capacities[i] + vertex_capacities[j]))) * \
                                        weight_matrix[j][i]
    return Hamiltonian


def createEvolutionKernel(Hamiltontian: np.ndarray, dt=cst.DELTA_T, approximation_method="scipy",
                          approximation_level=cst.APPROX_STEP) -> np.ndarray:
    '''
    Using a provided Hamiltonian `Hamiltonian`, create the kernel matrix that evolves the state `dt` in time.
    `approximation_method` is a string (`limit`,`taylor`,`scipy`) denoting
    which approximation procedure to use. `scipy` uses the built-in method: `scipy.linalg.expm`.
    `approximation_level` determines the number of terms in the approximation series to return.
    '''

    kernel = np.zeros(Hamiltontian.shape)
    dimension = Hamiltontian.shape[0]
    if approximation_method == 'scipy':
        kernel = lin.expm(Hamiltontian)
    elif approximation_method == 'limit':
        kernel = np.linalg.matrix_power(np.identity(dimension) + ((dt / approximation_level) * Hamiltontian),
                                        approximation_level)
    elif approximation_method == 'taylor':
        for i in range(approximation_level + 1):
            kernel += (1 / math.factorial(i)) * np.linalg.matrix_power(Hamiltontian.i)
    else:
        raise ValueError('Kernel approxiation method must be one of "scipy","limit",or "taylor".')
    return kernel
