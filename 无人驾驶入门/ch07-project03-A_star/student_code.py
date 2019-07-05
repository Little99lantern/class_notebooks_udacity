"""
版本3
"""

from helpers import Map, load_map, show_map
import math


# 计算直线距离（欧式距离），同时用作启发式函数
def get_distance(M, a, b):
    return math.sqrt((M.intersections[a][0]-M.intersections[b][0])**2 + (M.intersections[a][1]-M.intersections[b][1])**2)

# 得到某点的frontier
def get_frontier_from_father(M, father_node, processed):
    return [node for node in M.roads[father_node] if node not in processed]


infinity = float("inf")  # python中表示无穷大


def shortest_path(M, start, goal):
    # 初始化参数
    processed = []
    g_n = {}  # start到某点的总距离

    # 添加初始节点
    processed.append(start)
    g_n[start] = 0

    # 初始化路径点,元素为 (节点,父节点)
    path_nodes = []
    
    # 初始化路径, 添加目标节点
    shortest = [goal]
    if start == goal:
        return shortest
    
    
    while goal not in processed:
        temp_g = infinity
        temp_add = infinity
        choice = None
        father = None
        
        # 得到temp_add最小的节点choice和他的父节点father
        for father_node in processed:
            for node in get_frontier_from_father(M,father_node, processed):
                temp_h = get_distance(M, goal, node)
                if g_n[father_node] + get_distance(M, father_node, node) < temp_g and g_n[father_node] + get_distance(M, father_node, node) + temp_h < temp_add:
                    temp_g = g_n[father_node] + get_distance(M, father_node, node)
                    temp_add = temp_g + temp_h
                    choice = node
                    father = father_node
                    
        # 更新g_n
        g_n[choice] = g_n[father] + get_distance(M, father, choice)
        
        processed.append(choice)
#         print(processed)
        path_nodes.append((choice,father))
    
#     print(path_nodes)
    for i in reversed(path_nodes):
        if i[0] == shortest[0]:
            shortest.insert(0, i[1])
#     print(shortest)
    return shortest


if __name__ == "__main__":
    from test import test
    import time
    start_time = time.time()
    for i in range(100):
        test(shortest_path)

    stop_time = time.time()
    millisec_time = 1000*(stop_time - start_time)
    print("Time to test 100 iterations in milliseconds: " + str(millisec_time))