n = int(input())

def mic(n):
    if n % 10 != 0 :
        return -1
    btn = [300, 60, 10]

    ans = [''] * 3
    for i in range(3):
        ans[i] = str(n//btn[i])
        n %= btn[i]

    return -1 if n != 0 else ' '.join(ans)
print(mic(n))