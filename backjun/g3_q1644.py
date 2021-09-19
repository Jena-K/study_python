from collections import deque
import math

def is_prime(n):
    if 1< n < 4:

        return True

    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0 :
            return False
    return True

def find_PN(n):    
    cnt = 0
    arr = deque([2])
    SUM = 2
    
    if n < 3 :
        return n-1

    while arr[0] < n :
        print(arr, ' : ', SUM)
        if SUM == n :
            cnt+=1
            SUM-=arr.popleft()
        elif SUM > n :
            SUM-=arr.popleft()
        elif SUM < n :
            for i in range(arr[-1]+1, n*2+1):
                if is_prime(i) :
                    SUM+=i
                    arr.append(i)
                    break

        
    if is_prime(n) :
        return cnt+1
    else :
        return cnt

n = int(input())
print(find_PN(n))
