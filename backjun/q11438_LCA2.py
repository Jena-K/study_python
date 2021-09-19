import sys
#input = sys.stdin.readline
sys.setrecursionlimit(1e6)
n = int(input())
nodes = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())

parent = [[i] for i in range(n+1)]
depth = [0]*(n+1)
