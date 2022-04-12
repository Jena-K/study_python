#p327.snake
import heapq
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
#U R D L

d = 1 #cur direction

#cur time
time = 0

#current coordinate
x, y = 1, 1

#size of map
n = int(input())+1

#num of apple
k = int(input())

#drow the maps
maps = [[0]*n for i in range(n)]

#apple loc
for _ in range(k):
    a, b = map(int, input().split())
    maps[a][b] = 1

#num of movement
l = int(input())

#direction of time
move = []
for _ in range(l):
    a, b = input().split()
    b = -1 if b == 'L' else 1
    heapq.heappush(move, (int(a), b))
nxt, way = heapq.heappop(move)

tail = [(0, (1, 1))]

while True:
    if nxt == time:
        d = (d+4+way)%4
        if move :
            nxt, way = heapq.heappop(move)
    time+=1
    x += dx[d]
    y += dy[d]

    if x < 1 or y < 1 or x >= n or y >= n : break
    elif maps[x][y] == 2 : break
    elif maps[x][y] == 1 :
        maps[x][y] = 2
        heapq.heappush(tail, (time, (x, y)))
    elif maps[x][y] == 0:
        maps[x][y] = 2
        heapq.heappush(tail, (time, (x, y)))
        _, (a, b) = heapq.heappop(tail)
        maps[a][b] = 0

print(time)