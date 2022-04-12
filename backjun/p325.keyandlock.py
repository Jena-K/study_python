#325 자물쇠와 열쇠
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

#turn graph
def turn_graph(maps):
    n = len(maps)

    new_mpas = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_mpas[n-j-1][i] = maps[i][j]
    return new_mpas

#check True False
def tf(maps, n):
    for i in range(n, n*2):
        for j in range(n, n*2):
            if maps[i][j] != 1:
                return False
    return True

def solution(key, lock):
    m = len(lock)
    n = len(key)
    # drow maps 3 multiple size
    maps = [[0]*m*3 for i in range(m*3)]

    #copy lock
    for i in range(m, m*2):
        maps[i][m:m*2] = lock[i-m]
    
    #tf check
    for _ in range(4):
        if tf(maps, m) == True : return True
        for a in range(m*2+1):
            for b in range(m*2+1):
                for c in range(n):
                    for d in range(n):
                        maps[a+c][b+d] += key[c][d]
                if tf(maps, m) == True : return True
                for c in range(n):
                    for d in range(n):
                        maps[a+c][b+d] -= key[c][d]
        key = turn_graph(key)
                

    return False

print(solution(key, lock))

    
