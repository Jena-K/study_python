from collections import deque

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
MAX = 0

#침수되지 않은 칸 확인
for h in range(1, 101):
    q = deque()
    v = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if maps[i][j] >= h and v[i][j] == 0 :
                q.append((i, j))
                while q:
                    x, y = q.pop()
                    v[x][y] = 1
                    for d in range(4):
                        nx = x+dx[d]
                        ny = y+dy[d]
                        
                        if nx >= 0 and nx < n and ny >= 0 and ny < n and v[nx][ny] == 0 and maps[nx][ny] >= h:
                            q.append((nx, ny))
                cnt += 1
    MAX = max(cnt, MAX)
print(MAX)