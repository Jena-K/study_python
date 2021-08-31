from collections import deque

n = int(input())
q = deque()
for _ in range(n) :
    q.append(int(input()))
ans = []
stack = []
for i in range(1,n+1):
    x = q.pop()
    if i == x :
        ans.append(x)
    elif i < x :
        stack.append(x)
    elif i > x :
        while stack:
            ans.append(stack.pop())