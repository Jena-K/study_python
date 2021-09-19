#p369.InstallModem
import sys
input = sys.stdin.readline
n, c = map(int, input().split())
arr = sorted([int(input()) for _ in range(n)])

MIN = arr[0]
MAX = arr[-1]

while MAX >= MIN :
    cnt = 1
    MID = (MAX+MIN)//2
    value = arr[0]
    for i in range(1,n): 
        if arr[i] >= MID + value:
            cnt+=1
            value = arr[i]
            result = MID
    if cnt >= c :
        MIN = MID + 1
    else :
        MAX = MID - 1

print(result)

