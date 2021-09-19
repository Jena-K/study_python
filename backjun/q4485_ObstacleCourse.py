import heapq
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
while (n := int(input())) != 0 :
    maps = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    heap = [(maps[0][0], 0, 0)]
    while heap:
        c, x, y = heapq.heappop(heap)
        if visited[x][y] != 0 :
            continue
        maps[x][y] = c
        visited[x][y] = 1
        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]
            if nx >= 0 and nx < n and ny >= 0 and ny < n and visited[nx][ny] == 0:
                heapq.heappush(heap, (c+maps[nx][ny], nx, ny))
    cnt+=1

    print('Problem ', cnt, ': ', maps[n-1][n-1])