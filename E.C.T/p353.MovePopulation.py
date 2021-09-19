#p353.MovePopulation
#pass
from collections import deque
n, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt_old = -1
cnt = 0

adjoined = deque()

union = [[0] * n for _ in range(n)]

def Unite(i, j):
    uni = deque()
    uni2 = []
    cnt = union[i][j]
    Sum = 0
    Num = 0
    uni.append((i, j))
    uni2.append((i, j))
    union[i][j] = 0
    while uni:
        x, y = uni.popleft()
        Sum+=graph[x][y]
        Num+=1
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx >= 0 and ny >= 0 and nx < n and ny < n :
                if union[nx][ny] == cnt:
                    Sum+=graph[nx][ny]
                    cnt+=1
                    uni.append((nx, ny))
                    uni2.append((nx, ny))
                    union[x][y] = 0
    print(uni2)
    for x, y in uni2:
        graph[x][y] = Sum//Num
        
for i in range(n):
    for j in range(n):
        cnt+=1
        adjoined.append((i,j))
        while adjoined:
            x, y = adjoined.popleft()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if nx >= 0 and nx >= 0 and nx < n and ny < n and union[nx][ny] == 0 :
                    diff = abs(graph[x][y] - graph[nx][ny])
                    if diff >= L and diff <= R :
                        union[nx][ny] = cnt
                        adjoined.append((nx, ny))


      
for i in range(n):
    for j in range(n):
        if union[i][j] != 0 :
            Unite(i, j)


for i in graph:
    print(i)
print('')

for i in union:
    print(i)
