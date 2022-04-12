#p.339 CityDistance
from collections import deque
import sys
input = sys.stdin.readline
n, m, k, x = map(int, input().split())
node = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    node[a].append(b)

INF = int(1e9)
distance = [INF] * (n+1)

def dijkstra(start):
    q = deque([start])
    distance[start] = 0
    while q:
        s = q.popleft()
        for i in node[s] :
            if distance[s]+1 < distance[i]:
                distance[i] = distance[s] + 1
                q.append(i)

dijkstra(x)
answer = []
for i in range(1, n+1):
    if distance[i] == k :
        answer.append(i)

if answer :
    for i in answer :
        print(i)
else :
    print(-1)