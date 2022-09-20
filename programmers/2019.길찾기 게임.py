'''
부모 높이 저장.



'''

from collections import defaultdict
from bisect import bisect_left

def drow_graph():
    pass

def solution(nodeinfo):
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    
    arrY = sorted(nodeinfo)
    arrX = sorted(nodeinfo, key=lambda x : x[1])
    
    print(arrX)
    print(arrY)
    
    

    arrX, arrY
    



nodeinfo, result = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]],[[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
print(solution(nodeinfo))