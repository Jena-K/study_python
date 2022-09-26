'''
현재 배열의 최대 높이를 저장
해당 높이를 가진 값들 중 부모보다 크다면 왼쪽, 작다면 오른쪽으로 보냄.

'''

from collections import defaultdict
from bisect import bisect
import sys

sys.setrecursionlimit(10**6)

DFS = []
BFS = []

def drow_graph(arrX, arrY, graph):
    now = bisect(list(zip(*arrX))[0], arrY[0][0])

    #왼쪽
    if now > 1 :
        arrY = sorted(arrX[:now-1], key=lambda x: x[1], reverse=True)
        graph[arrX[now-1][2]][0] = arrY[0][2]
        drow_graph(arrX[:now-1], arrY, graph)
    else :
        graph[arrX[now-1][2]][0] = -1
    
    #오른쪽
    if now < len(arrX):
        arrY = sorted(arrX[now:], key=lambda x: x[1], reverse=True)
        graph[arrX[now-1][2]][1] = arrY[0][2]
        drow_graph(arrX[now:], arrY, graph)
    else :
        graph[arrX[now-1][2]][1] = -1
    

def BfsDfs(now, graph):
    if now == -1:
        return
    BFS.append(now)
    for i in graph[now]:
        BfsDfs(i, graph)
    DFS.append(now)

def solution(nodeinfo):
    
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    
    graph = [[-1 for _ in range(2)] for _ in range(len(nodeinfo)+1)]

    arrX = sorted(nodeinfo)
    arrY = sorted(nodeinfo, key=lambda x : x[1], reverse=True)

    drow_graph(arrX, arrY, graph)
    
    root = arrY[0][2]
    BfsDfs(root, graph)
    
    return [BFS, DFS]

nodeinfo, result = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]],[[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
print(solution(nodeinfo))

