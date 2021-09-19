from collections import deque
import math

def is_prime(n):
    for i in range(2, math.sqrt(n)):
        if n%i == 0 :
            return False
    return True

def find_PN(n):    
    cnt = 0
    arr = deque()
    SUM = 0
    if n == 1 :
        return 0
    while not arr :
        if SUM == n :
            cnt+=1
            SUM-=arr.popleft()
        elif SUM > n :
            SUM-=arr.popleft()
        elif SUM < n :
            for i in range(arr[-1]+1, n+1):
                if is_prime(i) :
                    arr.append(i)
                    break
    return cnt
    
    



n = int(input())
print(find_PN(n))
