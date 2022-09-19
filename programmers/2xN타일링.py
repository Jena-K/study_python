def solution(n):
    dp = [0 for _ in range(60001)]
    dp[1], dp[2] = 1, 2
    for i in range(3, n+1):
        dp[i] = dp[i-2]*2+1
    return dp[n]%100000007

'''
1   1   ㅣ
2   2   ㅣㅣ, =
3   3   ㅣㅣㅣ, =ㅣ, ㅣ=
4   5   =ㅣㅣ, ㅣㅣ=, ㅣㅣㅣㅣ, ㅣ=ㅣ, ==
5   10  ㅣㅣㅣ=, =ㅣㅣㅣ, ㅣ=ㅣㅣ
        ㅣㅣㅣㅣㅣ, =ㅣ, ㅣ=
        
'''
print(solution(4))