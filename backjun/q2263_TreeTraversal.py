__import__('sys').setrecursionlimit(10**6)

def pre_order(in_s, in_e, post_s, post_e):
    if in_s > in_e or post_s > post_e :
        return
    
    root = post_order[post_e]
    print(root, end=' ')

    left = idx[root] -in_s
    right = in_e - idx[root]

    pre_order(in_s, in_s+left-1, post_s, post_s+left-1)

    pre_order(in_e-right+1, in_e, post_e-right+1, post_e-1)

n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

idx = [0]*(n+1)
for i in range(n):
    idx[in_order[i]]=i
print(idx)
pre_order(0, n-1, 0, n-1)


