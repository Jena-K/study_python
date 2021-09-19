import heapq
n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n):
    data = list(map(int, input().split()))
    for i in range((len(data)-2)//2):
        tree[data[0]].append((data[i*2+2], data[i*2+1]))

def dijkstra(x):
    INF = int(1e9)
    distance = [INF] * (n+1)
    distance[x] = 0
    q = [(0, x)]
    while q:
        _, now = heapq.heappop(q)
        for dist, dest in tree[now] :
            if (d := dist+distance[now]) < distance[dest] :
                distance[dest] = d
                heapq.heappush(q, (d, dest))
    return distance[1:]
ans1 = dijkstra(1)
print(max(dijkstra(ans1.index(max(ans1))+1)))