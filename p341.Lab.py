#p341.Lab
from itertools import combinations
from itertools import product

n, m = map(int, input().split())
maps = []

#0:Empty, 1:Wall, 2:Virus
for i in range(n):
    maps.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

max_safty = 0
walls = []
for x in range(n):
    for y in range(m):
        if maps[x][y] == 0:
            walls.append((x, y))
walls_3 = combinations(walls, 3)

def spread_virus(x, y):
    global n, m
    for d in range(4):
        nx = x+dx[d]
        ny = y+dy[d]
        #print(nx, ny)
        if nx > -1 and ny > -1 and nx < n and ny < m and maps[nx][ny] == 0:
            maps[nx][ny] = 12
            spread_virus(nx, ny)

#build wall x 3
for ws in walls_3:
    for wx, wy in ws:
        maps[wx][wy] = 11
    #find_virus
    for x in range(n):
        for y in range(m):
            if maps[x][y] == 2:
                #spread_virus
                spread_virus(x,y)    
    
    cnt_safty = 0

    #get Number of Safty
    for x in range(n):
        for y in range(m):
            if maps[x][y] == 0:
                cnt_safty += 1
    if cnt_safty > max_safty: max_safty = cnt_safty

    #Roll Back
    for x in range(n):
        for y in range(m):
            if maps[x][y] == 11 or maps[x][y] == 12:
                maps[x][y] = 0

print(max_safty)


