from collections import deque
#m, n = 3, 3
#maps = ['011', '111', '110']
m, n = 6, 6
maps = ['001111','010000','001111','110001','011010','100010']
#m, n = 4, 2
#maps = ['0001', '1000']
for i in range(n): maps[i] = list(map(int, maps[i]))

'''
from collections import deque
n, m = map(int, input().split())
maps = [list(map(int, input())) for _ in range(n)]
'''
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

INF = int(1e9)
dist = [[-1] * m for _ in range(n)]

dist[0][0] = 0

heap = deque()
heap.append((0, 0))

while heap:
    x, y = heap.pop()
    for d in range(4):
        nx = x+dx[d]
        ny = y+dy[d]
        if nx >= 0 and nx < n and ny >= 0 and ny < m :
            if dist[nx][ny] == -1:
                if maps[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y]
                    heap.append((nx, ny))
                elif maps[nx][ny] == 1:
                    dist[nx][ny] = dist[x][y]+1
                    heap.appendleft((nx, ny))
                    
print(dist[n-1][m-1])