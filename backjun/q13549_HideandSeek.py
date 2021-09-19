def solution():
    n, m = map(int, input().split())
    INF = int(1e9)
    ans = [INF]*(m*2+2)
    
    if n >= m :
        return n-m
    
    for i in range(n+1):
        ans[i] = n-i

    for i in range(1, m*2):
        ans[i] = min(ans[i-1]+1, ans[i], ans[i+1]+1)
        j = i * 2
        while j < m+2:
            ans[j] = min(ans[j], ans[j//2])
            j*=2

    return ans[m]
    
print(solution()) 