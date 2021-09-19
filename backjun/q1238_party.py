import heapq
def dijkstra(x, n):
    dist = [INF]*(n+1)
    dist[x] = 0
    heap = [(0, x)]
    while heap :
        cur_dist, now = heapq.heappop(heap)
        for new_dist, new_dest in data[now]:
            if (distance := dist[now]+new_dist) < dist[new_dest]:
                dist[new_dest] = distance
                heapq.heappush(heap, (distance ,new_dest))
    return dist

n, m, x = map(int, input().split())
data = [[] for _ in range(n+1)]

for i in range(m):
    s, d, c = map(int, input().split())
    data[s].append((c, d))

INF = int(1e9)
print(max([[i[0]+i[1]] for i in zip(dijkstra(x, n)[1:], [dijkstra(i, n)[x] for i in range(1, n+1)])])[0])