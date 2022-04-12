from itertools import combinations
import math
def decimal(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0 :
            return False
    return True

def solution(nums):
    cnt = 0
    combs = combinations(nums, 3)
    for comb in combs:
        if decimal(sum(comb)):
            cnt += 1
    return cnt

nums = [1,2,3,4]
print(solution(nums))
#result = 1

nums = [1,2,7,6,4]
print(solution(nums))
#result = 4