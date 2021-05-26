#n진법, t개 구하기, m명, 내 자리 p
def Base_n(n, x):
    ABCD = '0123456789ABCDEF'
    base = ''
    while x:
        base = ABCD[x%n] + base
        x//=n
    return base

def solution(n, t, m, p):
    answer = '0'

    for i in range(m*t):
        answer+=Base_n(n, i)

    ans = ''

    for i in range(p-1, m*t+p-1, m):
        ans+=answer[i]

    return ans.upper()








n, t, m, p = 2, 4, 2, 1
print(solution(n,t,m,p))
n, t, m, p = 16,16,2,1
print(solution(n,t,m,p))
n, t, m, p = 16,16,2,2
print(solution(n,t,m,p))
n, t, m, p = 14,13,3,1
print(solution(n,t,m,p))