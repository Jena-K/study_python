#p375.Mine
T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    dp = [[0]*n for i in range(m)]

    x = 0
    for i in arr :
        dp[x%m][x//m] = i
        x+=1
    
    for i in range(1, m):
        dp[i][0] += max(dp[i-1][:2])
        dp[i][1] += max(dp[i-1])
        dp[i][2] += max(dp[i-1][1:])

    print(max(dp[-1]))
    
