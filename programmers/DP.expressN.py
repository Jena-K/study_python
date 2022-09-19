MIN = 9
def dfs(rs, cnt, n, number):
    global MIN

    if cnt >= MIN :
        return
    
    if rs == number :
        MIN = min(MIN, cnt)
        return
    
    for i in range(1, 9):
        dfs(rs + int(str(n)*i), cnt+i, n, number)
        dfs(rs - int(str(n)*i), cnt+i, n, number)
        dfs(rs * int(str(n)*i), cnt+i, n, number)
        dfs(rs // int(str(n)*i), cnt+i, n, number)

def solution(N, number):
    
    dfs(0, 0, N, number)
    return MIN if MIN != 9 else -1
    
print(solution(5, 12))
print(solution(2, 11))

#solution(2, 11)