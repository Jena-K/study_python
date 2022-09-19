coins = [500, 100, 50, 10, 5, 1]

n = 1000-int(input())

ans = 0

for i in coins:
    ans += n//i
    n %= i
    if n == 0 :
        break
print(ans)