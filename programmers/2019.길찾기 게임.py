'''
부모 높이 저장.



'''

from collections import defaultdict
from bisect import bisect_left

def drow_graph():
    pass

def solution(nodeinfo):
    # graph = [[] for _ in range(len(nodeinfo))]
    node = defaultdict(list)
    
    for idx, i in enumerate(nodeinfo):
        node[i[0]].append((idx, i[1]))
    
    for key in node.keys():
        node[key].sort()
    node_dic = {idx:i for idx, i in enumerate(nodeinfo)}
    node = [i for i in sorted(node_dic.items(), reverse=True, key=lambda x: x[1][1])]
    
    root = node[0][0]
    
    print(root)

    return 



nodeinfo, result = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]],[[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
print(solution(nodeinfo))