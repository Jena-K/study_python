'''
부모 높이 저장.

'''

from collections import defaultdict
from bisect import bisect_left

def drow_graph(parent, arrX, arrY):
    if not arrX:
        return -1

    h_x = arrX[0][0]
    
    graph[0] = 1
    
    

def solution(nodeinfo):
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    
    graph = [[[] for _ in range(2)] for _ in range(len(nodeinfo))]
    arrX = sorted(nodeinfo)
    arrY = sorted(nodeinfo, key=lambda x : x[1])
    
    print(arrX)
    print(arrY)
    
    drow_graph(arrX[0], arrX, arrY)
    



nodeinfo, result = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]],[[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
print(solution(nodeinfo))