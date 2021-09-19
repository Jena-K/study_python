from collections import deque
n = int(input())
arr = list(map(int, input().split()))
rmv = deque([int(input())])


child = [[] for _ in range(n)]

for i in range(n):
    if arr[i] == -1 : continue
    child[arr[i]].append(i)

if arr[rmv[0]] != -1:
    child[arr[rmv[0]]].remove(rmv[0])
else :
    rmv = []
    child = [False]*n

while rmv:
    x = rmv.popleft()
    for i in child[x]:
        rmv.append(i)
    child[x] = False

cnt = 0
for i in range(n):
    if child[i] == [] :
        cnt+=1

print(cnt)




















def dfs(num, arr):
    arr[num] = -2
    for i in range(len(arr)):
        if num == arr[i]:
            dfs(i, arr)

n = int(input())
arr = list(map(int, input().split()))
k = int(input())

dfs(k, arr)
cnt = 0
for i in range(len(arr)):
    if arr[i] != -2 and i not in arr:
        cnt += 1

print(cnt)

