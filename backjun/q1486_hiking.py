import heapq
import queue
import math
n, m, t, d = map(int, input().split())
maps = [input() for _ in range(n)]

#distance dictionary
dic = {chr(i+65):i for i in range(26)}
dic.update({chr(i+97):i+26 for i in range(26)})
INF = int(1e9)
visited = [[0]*m for _ in range(n)]
up = [[INF]*m for _ in range(n)]
down = [[INF]*m for _ in range(n)]
up[0][0], down[0][0] = 0, 0
#dist, ax, ay, bx, by
q = [(0, 0, 0, 0, 0)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

while q:
    dist, ax, ay, bx, by = heapq.heappop(q)
    visited[ax][ay] = 1

    up[bx][by] = 1
    for dm in range(4):
        nx = ax+dx[dm]
        ny = ay+dy[dm]
        if nx >= 0 and ny >= 0 and nx < n and ny < n and visited[nx][ny] == 0 :
            if maps[nx][ny] > maps[x][y] :
                up[nx][ny] = min(up[nx][ny], (dic[maps[nx][ny]]-dic[maps[x][y]])^2)
            else :
                up[nx][ny] = min(up[nx][ny], up[x][y]+1)
            heapq.heappush(q, (up[nx][ny], nx, ny))
for i in up:
    print(i)