import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n = int(input())
data = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, d = map(int, input().split())
    data[a].append((d, b))
    data[b].append((d, a))

INF = int(1e9)

def dijkstra(x):
    distance = [INF]*(n+1)
    distance[x] = 0
    q = [(0, x)]

    while q:
        _, now = q.pop()
        for cost, dest in data[now]:
            if (dist := distance[now]+cost) < distance[dest] :
                distance[dest] = dist 
                q.append((dist, dest))
    return distance

d1 = dijkstra(1)[1:]
s = d1.index(max(d1))
print(d1)
print(s)
print(max(dijkstra(s+1)[1:]))
