"""
版本3 可运行
Time to test 100 iterations in milliseconds: 370.6376552581787

版本4:
数据结构优化: frontier和processed需要遍历多次或查找, 尝试采用字典将两个列表整合, 形如{father_node1:{frontier1, frontier2...}, ...}
注意: 字典更新问题, 有多个father节点拥有相同frontier点时, 如果该frontier被选中, 如何从多个father:{}节点中删除该frontier
    - 解决方案1: [注1]
Time to test 100 iterations in milliseconds: 245.77021598815918
代码优化:
1. 循环体中更新g_n时, get_distance重复计算
2. get_distance中直接传入参数M, 并多次使用M.intersections
    - nodes_dic = M.intersections, 传入参数nodes_dic
3. get_frontier_from_father中直接传入参数M
    - roads_dic = M.roads, 
Time to test 100 iterations in milliseconds: 202.85296440124512

版本5
processed改用集合,(需要做查找操作)
frontier直接用roads_dic = M.roads, roads_dic[father]获取, 不用函数get_frontier_from_father获取
    roads_dic为字典, roads_dic[0]为列表, 由于现在只对roads_dic[0]做遍历操作,不做查找操作,所以对性能没有影响.
Time to test 100 iterations in milliseconds: 135.12444496154785
"""

from helpers import Map, load_map, show_map
import math


# 计算直线距离（欧式距离），同时用作启发式函数
def get_distance(nodes_dic, a, b):
    return math.sqrt((nodes_dic[a][0]-nodes_dic[b][0])**2 + (nodes_dic[a][1]-nodes_dic[b][1])**2)

def shortest_path(M, start, goal):
    nodes_dic = M.intersections
    roads_dic = M.roads
    # 初始化参数
    processed = {start}  # 已走过的点

    g_n = {}  # start到某点的总距离
    g_n[start] = 0

    # 初始化路径点,元素为 (节点,父节点)
    path_nodes = []
    
    # 初始化路径, 添加目标节点
    shortest = [goal]
    if start == goal:
        return shortest
    
    
    while goal not in processed:
        temp_g = float("inf")  # start到节点的(最小)总距离, 初始化为无穷大
        temp_add = float("inf")  # 该节点的g_n + h_n, 初始化为无穷大
        choice = None
        father = None
    
        
        # 得到temp_add最小的节点choice和他的父节点father
        for father_node in processed:
            for node in roads_dic[father_node]:
                if node not in processed:  # [注1]
                    temp_h = get_distance(nodes_dic, goal, node)
                    if g_n[father_node] + get_distance(nodes_dic, father_node, node) < temp_g and g_n[father_node] + get_distance(nodes_dic, father_node, node) + temp_h < temp_add:
                        temp_g = g_n[father_node] + get_distance(nodes_dic, father_node, node)
                        temp_add = temp_g + temp_h
                        choice = node
                        father = father_node
                    
        # 更新g_n
        g_n[choice] = temp_g

        # 更新processed
        processed.add(choice)
        # print(processed)
        
        # 更新path_nodes: 添加元素(choice,father)
        path_nodes.append((choice,father))
        # print(path_nodes)

    for i in reversed(path_nodes):
        if i[0] == shortest[0]:
            shortest.insert(0, i[1])
    return shortest


if __name__ == "__main__":
    from test import test
    # test(shortest_path)

    import time
    start_time = time.time()
    for i in range(100):
        test(shortest_path)

    stop_time = time.time()
    millisec_time = 1000*(stop_time - start_time)
    print("Time to test 100 iterations in milliseconds: " + str(millisec_time))

    