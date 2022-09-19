from collections import deque
import sys
input = sys.stdin.readline
def chk_dist(ax, ay, bx, by):
    if abs(ax-bx)+abs(ay-by) <= 1000:
        return True
    return False

def dfs(ax, ay, bxy, cx, cy):
    if chk_dist(ax, ay, cx, cy):
        return 'happy'
    
    v = [0] * len(bxy)
    q = deque([(ax, ay)])
    
    while q:
        x, y = q.popleft()
        for idx, i in enumerate(bxy):
            a, b = i
            if abs(x-a)+abs(y-b) <= 1000 and not v[idx] :
                if chk_dist(a, b, cx, cy):
                    return 'happy'
                q.append((a, b))
                v[idx] = 1
    return 'sad'

t = int(input())
for i in range(t):
    flag = 1
    n = int(input())
    ax, ay = list(map(int, input().split()))
    bxy = [list(map(int, input().split())) for _ in range(n)]
    cx, cy = list(map(int, input().split()))
    
    print(dfs(ax, ay, bxy, cx, cy))