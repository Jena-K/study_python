#p367.Bisec_Count
'''
from collections import Counter

n, x = map(int,input().split())
arr = list(map(int, input().split()))

c_arr = Counter(arr)

print(c_arr[x] if c_arr[x] != 0 else -1)
'''

from bisect import bisect_left, bisect_right

n, x = map(int,input().split())
arr = list(map(int, input().split()))

print(bisect_right(arr, x)-bisect_left(arr, x))