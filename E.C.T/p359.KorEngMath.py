#p359.KorEngMath
#Kor, Eng, Math
import sys
input = sys.stdin.readline
n = int(input())
data = [input().split() for _ in range(n)]

data.sort(key=lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in data:
    print(i[0])