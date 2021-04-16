import heapq
import sys
input_old = input
input = sys.stdin.readline
input = input_old
inf = int(1e9)

n,m,c = map(int, input().split())
#노드 개수, 간선 개수, 시작 노드
graph = [[] for i in range(n+1)]
distance = [inf]*(n+1)

for _ in range(m):
    x,y,z = map(int,input().split())
    #x번 노드에서 y번 노드로 가는 비용이 z
    graph[x].append((y,z))

def dijkstra(c):
    q = []
    heapq.heappush(q,(0,c))
    distance[c]=0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(c)

count = 0
max_distance = 0

for d in distance:
    if d != inf:
        count += 1
        max_distance = max(max_distance,d)

print(count -1,max_distance)
