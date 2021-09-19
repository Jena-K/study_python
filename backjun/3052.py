n, m = map(int, input().split())

arr = [i for i in range(1, n+1)]
ans = []
cnt = 0

while arr :
    cnt-=1
    for _ in range(m):
        cnt = (cnt+1)%len(arr)
    ans.append(str(arr.pop(cnt)))

print('<%s>' % ', '.join(ans))