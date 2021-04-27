#p332.ChickenDeliver
def chck_dist(dist, comb):
    arr = []
    result = 0
    for i in comb:
        arr.append(dist[i])
    for i in range(len(dist[0])):
        result+=min([j[i] for j in arr])
    return result
    

from itertools import combinations
n, m = map(int, input().split())
maps = [(list(map(int, input().split()))) for _ in range(n)]
chck, home = [], []

#치킨, 집의 위치를 저장
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1 :
            home.append((i, j))
        elif maps[i][j] == 2:
            chck.append((i, j))

lc = len(chck)
dist = [[] for _ in range(lc)]

#가게와의 거리를 확인
for i in range(lc):
    for x2, y2 in home:
        x, y = chck[i]
        dist[i].append((abs(x-x2)+abs(y-y2)))

comb = combinations(range(lc), m)
mn = 2501

#하나씩 최소값 확인
for i in comb:
    temp = chck_dist(dist, i)
    if mn > temp : mn = temp

print(mn)
