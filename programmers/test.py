from itertools import combinations
def solution(n, rooks):
    def search(comb):
        #좌, 우, 좌상, 우상, 좌하, 우하 6방향 순서로 탐색
        while comb :
            x, y = comb.pop()
            #가로 탐색
            for ny in range(x*2+1):
                if (x, ny) in comb:
                    return False
            #좌상
            nx, ny = x, y
            while True :
                nx, ny = (nx-1, ny-1) if ny % 2 == 1 else (nx, ny-1)

                if nx >= 0 and nx < n and ny >= 0 and ny < 2*nx+1:
                    if (nx, ny) in comb :
                        return False
                else :
                    break
            #우상
            nx, ny = x, y
            while True :
                nx, ny = (nx-1, ny-1) if ny % 2 == 1 else (nx, ny+1)

                if nx >= 0 and nx < n and ny >= 0 and ny < 2*nx+1:
                    if (nx, ny) in comb :
                        return False
                else :
                    break
            
            #좌하
            nx, ny = x, y
            while True:
                nx, ny = (nx, ny-1) if ny % 2 == 1 else (nx+1, ny+1)

                if nx >= 0 and nx < n and ny >= 0 and ny < 2*nx+1:
                    if (nx, ny) in comb :
                        return False
                else :
                    break
                
            #우하
            nx, ny = x, y
            while True:
                nx, ny = (nx, ny+1) if ny % 2 == 1 else (nx+1, ny+1)

                if nx >= 0 and nx < n and ny >= 0 and ny < 2*nx+1:
                    if (nx, ny) in comb :
                        return False
                else :
                    break
        return True
    
    #경우의 수 생성
    d = []
    for i in range(n):
        d+=[(i, j) for j in range(2*i+1)]
    
    cnt = 0
    for comb in combinations(d, rooks):
        if search(list(comb)):
            cnt += 1

    return cnt
print(solution(3, 2))
#print(solution(5, 3))