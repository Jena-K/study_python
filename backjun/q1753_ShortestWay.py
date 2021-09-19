import heapq
import sys
input = sys.stdin.readline
v, e = map(int, input().split())
k = int(input())

data = [[] for _ in range(v+1)]

for _ in range(e):
    s, d, c = map(int, input().split())
    data[s].append((c, d))

INF = int(1e9)

def dijkstra(s):
    dist = [INF]*(v+1)
    dist[s] = 0
    heap = [(0 ,s)]

    while heap:
        cost, now = heapq.heappop(heap)
        if cost > dist[now] : continue
        for dist_new, dest_new in data[now]:
            if dist[dest_new] > (distance := dist[now]+dist_new):
                dist[dest_new] = distance
                heapq.heappush(heap, (distance, dest_new))
    return dist

for i in dijkstra(k)[1:]:
    print(i if i != INF else 'INF')