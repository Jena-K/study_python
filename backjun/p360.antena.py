#p360.antena
n = int(input())
houses = sorted(list(map(int,input().split())))

print(houses[round(n/2)-1])