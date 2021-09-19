'''
from itertools import combinations
n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

for i in range(1, n+1):
    for combi in combinations(arr, i):
        if sum(combi) == s :
            cnt+=1
print(cnt)

'''
def dfs(idx, SUM):
    global cnt
    if idx >= n :
        return
    
    SUM+=arr[idx]
    if SUM == s:
        cnt+=1

    dfs(idx+1, SUM)
    dfs(idx+1, SUM-arr[idx])

n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

dfs(0, 0)
print(cnt)