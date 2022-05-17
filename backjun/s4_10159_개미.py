w, h = map(int, input().split())
x, y = map(int, input().split())
t = int(input())

dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]

d = 0
for _ in range(t):
    print(x, y)
    while True: 
        nx = x + dx[d]
        ny = y + dy[d]
        if nx >= 0 and nx <= w and ny >= 0 and ny <= h :
            x = nx
            y = ny
            break
        else :
            d = (d+1)%4
            continue
        
print(x, y)