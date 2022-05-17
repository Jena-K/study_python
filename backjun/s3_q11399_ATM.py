n = int(input())
arr = sorted(list(map(int, input().split())))

MIN = 0
for i in range(len(arr)):
    MIN += arr[i] * (len(arr)-i)
print(MIN)
#12
#1 = 1*4 = 4
#2 = 2*3 = 6
#3 = 3*2 = 6
#4 = 4*1 = 4
# 12 + 20 = 32