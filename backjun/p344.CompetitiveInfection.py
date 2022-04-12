import sys
input = sys.stdin.readline
#시작 지점부터 매 초마다 1칸씩 바이러스가 있는지 탐색
#가장 가까운 바이러스의 번호 리턴
#혹 동일한 거리에 여러 바이러스가 있다면 가장 낮은 바이러스 리턴

def solution():
    #get Data
    n, k = map(int, input().split())
    maps = [(list(map(int, input().split()))) for _ in range(n)]
    s, x, y = map(int, input().split())
    
    #Move Coordinate
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    x -= 1
    y -= 1
    #시작점이 바이러스라면 종료
    if maps[x][y] != 0 :
        print(maps[x][y])
        return
    
    q = []
    visited = [(x, y)]
    maps[x][y] = 1001
    for i in range(s):
        temp = []
        while visited:
            x, y = visited.pop()
            for d in range(4):
                nx = x+dx[d]
                ny = y+dy[d]
                if nx > -1 and ny > -1 and nx < n and ny < n:
                    if maps[nx][ny] != 0 and maps[nx][ny] != 1001:
                        q.append(maps[nx][ny])
                    elif maps[nx][ny] == 0:
                        temp.append((nx, ny))
                    maps[nx][ny] = 1001
        visited = temp[:]
        if q :
            print(min(q))
            return
    if not q :
        print(0)

solution()




'''#이전코드 01-start
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
maps = [(list(map(int, input().split()))) for _ in range(n)]
s, x, y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def virus_spread():
    global n
    for i in range(n):
        for j in range(n):
            if maps[i][j] != 0:
                v = maps[i][j]
                if v > 10000: continue
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if nx > -1 and ny > -1 and nx < n and ny < n:
                        if maps[nx][ny] == 0:
                            maps[nx][ny] = v+10000
                        elif maps[nx][ny] > v+10000:
                            maps[nx][ny] = v+10000

#10의 자리 수 제거
def clear_decimal():
    for i in range(n):
        for j in range(n):
            maps[i][j] %= 10000

for t in range(s):
    virus_spread()
    clear_decimal()

print(maps[x-1][y-1])
'''#이전코드 01-end