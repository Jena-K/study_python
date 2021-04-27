#p349.InsertOperator
# + - * %
#'+' '-' '*' '/'
from itertools import permutations
n = int(input())
nums = list(map(int, input().split()))
add, mns, mul, div = map(int, input().split())
idx = 1
ans = nums[0]
INF = int(1e9)

MAX = -INF
MIN = INF

def calc(ans, idx, add, mns, mul, div):
    global MAX, MIN
    if idx == n:
        if ans > MAX :
            MAX = ans
        if ans < MIN :
            MIN = ans
    else : 
        if add:
            calc(ans+nums[idx], idx+1, add-1, mns, mul, div)
        if mns :
            calc(ans-nums[idx], idx+1, add, mns-1, mul, div)
        if mul:
            calc(ans*nums[idx], idx+1, add, mns, mul-1, div)
        if div:
            if ans > 0 :
                calc(ans//nums[idx], idx+1, add, mns, mul, div-1)
            else :
                calc(-(-ans//nums[idx]), idx+1, add, mns, mul, div-1)

calc(ans, idx, add, mns, mul, div)

print(MAX)
print(MIN)

'''
from itertools import permutations
n = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))
operators_string = list('+'*operators[0]+'-'*operators[1]+'*'*operators[2]+'/'*operators[3])

INF = int(1e10)
MIN = INF
MAX = -INF
perm = permutations(operators_string, n-1)



for operator in perm:
    answer = nums[0]
    for i in range(n-1):
        if operator[i] == '+' :
            answer += nums[i+1]
        elif operator[i] == '-' :
            answer -= nums[i+1]
        elif operator[i] == '*' :
            answer *= nums[i+1]
        elif operator[i] == '/' :
            if answer > 0 :
                answer //= nums[i+1]
            else :
                answer = -((-answer)//nums[i+1])
    if answer < MIN :
        MIN = answer
    if answer > MAX:
        MAX = answer
'''
