import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

q = deque()
q.append(1)
check = [False] * (n+1)
ans = {}
while q:
    x = q.popleft()
    check[x] = True
    for v in tree[x] :
        if check[v] == False:
            ans[v] = x
            q.append(v)

for i in range(2, n+1):
    print(ans[i])
