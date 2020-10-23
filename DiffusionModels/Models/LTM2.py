import networkx as nx
import numpy as np


def lt_(a, b, s: list, origin: list, beta: float):
    '''
    邻接矩阵
    a = sw.a
    节点度数, 1/b是其他节点对该节点的影响力
    b = sw.b
    节点阀值
    beta = sw.beta
    原激活节点
    origin = sw.origin
    超过beta（如50%）的邻接节点处于激活状态，该节点才会进入激活状态
    '''
    deep = 90
    # 节点数
    n = a.shape[0]
    # 控制符
    judge = 1
    # 未激活节点
    s1 = np.delete(s, origin)
    # 激活节点
    i = origin
    U = []
    for m in range(deep):
        U.append(len(i))
        # 该轮激活节点
        temp_i = []
        # 激活节点个数
        m = len(i)
        asd_final = []
        for j in range(0, m):
            node = int(i[j])
            asd = []
            for k in range(0, n):
                if a[node][k] == 1:
                    asd.append(k)
            # 找到相邻的未激活节点
            asd2 = np.intersect1d(asd, s1)

            for k in range(0, len(asd2)):
                num = 0
                # 该未激活节点相邻的激活节点个数
                for t in range(0, m):
                    if a[int(i[t])][asd2[k]] == 1:
                        num = num + 1
                if 1 / b[asd2[k]] * num >= beta:
                    asd_final.append(asd2[k])
            temp_i = np.union1d(temp_i, asd_final)
            s1 = np.setdiff1d(s1, asd_final)
        # 将新激活节点合并到原激活节点中
        fig = asd_final
        lenl = len(temp_i)
        i = np.union1d(i, temp_i)

        # 如果该轮没有新激活节点，那之后都不会再有，跳出循环
        if len(temp_i) == 0:
            judge = 0
    return U
    '''
    #输出新的网络状况
    color = []
    for j in range(0, n):
        color.append('b')
    for j in range(0, len(i)):
        color[int(i[j])] = 'r'
    g = nx.from_numpy_matrix(a)
    nx.draw(g, with_labels=True, node_color=color)
    plt.show()
    '''
