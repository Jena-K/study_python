#p332.ChickenDeliver
n, m = map(int, input().split())
maps = []

#0 = empty, 1 = house, 2 = chck
#max(h) < 2n  /  max(n) < 50  /   max(chck) < 13
for _ in range(n):
    maps.append(list(map(int, input().split())))

chck = []
home = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1 :
            chck.append((i, j))
        elif maps[i][j] == 2:
            home.append((i, j))

print(chck)
print(home)


