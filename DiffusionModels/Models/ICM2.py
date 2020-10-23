import random
from DiffusionModels.Graphs.RD import RDGraph
import DiffusionModels.Constants.constants as cts
from DataExtrraction.Generate import Common_matrix
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import time

def ICM2():
    A = Common_matrix(cts.FILE_PATH_2000).getAdjacency_matrix()
    G = nx.DiGraph(A)
    G.add_edges_from(RDGraph(cts.FILE_PATH_2000).getEdgeList())
    G.add_nodes_from(RDGraph(cts.FILE_PATH_2000).getNodeList())
    for edge in G.edges:
        G.add_edge(edge[0], edge[1], weight=random.uniform(0, 1))  # 可不可以作为权值
    for node in G:
        G.add_node(node, state=0)  # 用state标识状态 state=0 未激活，state=1 激活

    seeds = RDGraph(cts.FILE_PATH_2000).getSeedTime(71)
    print(len(seeds))
    tmp = seeds
    deep = 90
    u = []
    for i in range(deep):
        print(len(tmp))
        u.append(len(tmp))
        for seed in tmp:
            G._node[seed]['state'] = 1  # 表示33被激活

            all_active_nodes = []  # 所有被激活的节点放在这里
            all_active_nodes.append(seed)

            start_influence_nodes = []  # 刚被激活的节点 即有影响力去影响别人的节点
            start_influence_nodes.append(seed)

            res = [[seed]]
            num = 0
            new_active = list()
            #t1 = '%s time' % i + ' %s nodes' % len(all_active_nodes)
            #print(t1)  # 当前有多少个节点激活

            for v in start_influence_nodes:
                for nbr in G.neighbors(v):
                    if G._node[nbr]['state'] == 0:  # 如果这个邻居没被激活
                        edge_data = G.get_edge_data(v, nbr)
                        if 0.01 < edge_data['weight']:
                            G._node[nbr]['state'] = 1
                            new_active.append(nbr)
                            # activated_graph.add_edge(v, nbr) # 画图 添加边

            #print('激活', new_active)
            start_influence_nodes.clear()  # 将原先的有个影响力的清空
            start_influence_nodes.extend(new_active)  # 将新被激活的节点添加到有影响力
            all_active_nodes.extend(new_active)  # 将新被激活的节点添加到激活的列表中
            res.append(new_active)

            #print('all_active_nodes', all_active_nodes)  # 打印
            tmp = np.union1d(tmp, all_active_nodes)
    return u

# print(res)
'''
res = [c for c in res if c]
pos = nx.spring_layout(G)  # 节点的布局为spring型
nx.draw(G, pos, with_labels=True, node_color='w', node_shape='.')
color_list = ['brown', 'orange', 'r', 'g', 'b', 'y', 'm', 'gray', 'black', 'c', 'pink', 'brown', 'orange', 'r', 'g',
              'b', 'y', 'm', 'gray', 'black', 'c', 'pink']
for i in range(len(res)):
    nx.draw_networkx_nodes(G, pos, with_labels=True, node_color=color_list[i], nodelist=res[i])
plt.show()
'''
