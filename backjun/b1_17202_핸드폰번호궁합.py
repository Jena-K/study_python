a = input()
b = input()


def uni(a, b):
    s = ''
    for i in range(len(b)):
        s += a[i] + b[i]

    return s+a[::-1][:len(a)-len(b)]

def sm(a, b):
    # print(sum([int(a), int(b)]))
    return str(sum([int(a), int(b)])%10)
    
s = '1' * len(a)*2
while len(s) > 2:
    s = uni(a, b)
    a, b = '', ''
    for i in range(0, len(s)-1, 2):
        a += sm(s[i], s[i+1])
    
    for i in range(1, len(s)-1, 2):
        b += sm(s[i], s[i+1])

print(s.rjust(2, '0'))