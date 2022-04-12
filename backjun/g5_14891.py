n, m = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def up():
    pass

def watch(x, y, cctv):
    if cctv == 1 :
        for i in range(4):
            pass
    elif cctv == 2 :
        pass
    elif cctv == 3 :
        pass
    elif cctv == 4 :
        pass
    elif cctv == 5 :
        pass

c = []
for x in n:
    for y in m:
        if 0 < maps[x][y] < 6 :
            watch(x, y, maps[x][y])
    
#1: straight - 4 way
#2: opposite    2 w
#3: right angle 4 w
#4: F U     4 w
#5: all way 1 w
#6: Wall 0 w