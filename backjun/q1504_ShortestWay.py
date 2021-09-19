import heapq
import sys
input = sys.stdin.readline
def dks(s, d):
    distance = [INF]*(n+1)
    distance[s] = 0
    heap = [(0, s)]
    while heap :
        now = heapq.heappop(heap)[1]
        for new_dist, new_dest in data[now]:
            if (dist := distance[now]+new_dist) < distance[new_dest]:
                distance[new_dest] = dist
                heapq.heappush(heap, (dist, new_dest))
    return distance[d]

n, m = map(int, input().split())
data = [[] for _ in range(n+1)]
for _ in range(m):
    s, d, c = map(int, input().split())
    data[s].append((c, d))
    data[d].append((c, s))
a, b = map(int, input().split())

INF = int(1e9)

res = min(dks(1, a)+dks(a, b)+dks(b, n), dks(1, b)+dks(b, a)+dks(a, n))
print(res if res < INF else -1)