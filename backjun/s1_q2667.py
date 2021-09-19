#s1_q2667.py
from collections import deque

n = int(input())
maps = [list(map(int, input())) for _ in range((n))]


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = []

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1 :
            arr = deque([(i, j)])
            maps[i][j] = 0
            cnt = 1
            while arr:
                a, b = arr.popleft()
                for d in range(4):
                    na, nb = a+dx[d], b+dy[d]
                    if na < n and na >= 0 and nb < n and nb >= 0 and maps[na][nb] == 1:
                        arr.append((na, nb))
                        maps[na][nb] = 0
                        cnt+=1
            answer.append(cnt)
            

print(len(answer))
for i in sorted(answer):
    print(i)
