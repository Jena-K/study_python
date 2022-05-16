a = list(input())
b = list(input())

s = ''
for i, j in zip(a, b):
    s += i+j
    
print(s)