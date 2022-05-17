a, b = input().split()

MIN = int(a.replace('6', '5'))+int(b.replace('6', '5'))
MAX = int(a.replace('5', '6'))+int(b.replace('5', '6'))
print(MIN, MAX)