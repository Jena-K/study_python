'''
#s2_q6603.py
from itertools import combinations
while True:
    arr = input().split()
    n = int(arr[0])
    if n == 0 :
        break
    arr = arr[1:]
    go = 1
    for i in combinations(arr, 6):
        print(' '.join(i))
    print()
'''

def dfs(s, depth):
    global n
    if depth == 6 :
        for i in range(6):
            print(check[i], end=' ')
        print()
        return
    for i in range(s, n):
        check[depth] = arr[i]
        dfs(i+1, depth+1)


check = [0 for _ in range(6)]

while True:
    arr = input().split()
    n = int(arr[0])
    if n == 0 :
        break
    del arr[0]
    dfs(0, 0)
    print()



8