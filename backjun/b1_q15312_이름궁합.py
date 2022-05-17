a, b = input(), input()
arr = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

s = []
for i in range(len(a)):
    s.append(arr[ord(a[i])-65])
    s.append(arr[ord(b[i])-65])
    
while len(s) > 2:
    ns = []
    for i in range(len(s)-1):
        ns.append((s[i] + s[i+1])%10)
        
    s = ns

print(''.join(map(str, s)).rjust(2, '0'))