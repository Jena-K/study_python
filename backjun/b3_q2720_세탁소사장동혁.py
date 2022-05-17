n = int(input())
c = [25, 10, 5, 1]

for _ in range(n):
    x = int(input())
    for i in range(4) :
        print(x//c[i], end=' ')
        x %= c[i]

    print('')