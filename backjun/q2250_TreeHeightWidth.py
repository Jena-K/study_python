def in_order(node ,depth):
    global idx
    if node == -1 :
        return

    in_order(child[node][0], depth+1)
    
    idx+=1
    dpt_arr[depth].append(idx)
    
    in_order(child[node][1], depth+1)

n = int(input())
idx = 0
parent = False * n+1
child = False * n+1
dpt_arr = [[] for _ in range(n+1)]

for _ in range(n):
    a, b, c = map(int, input().split())
    child[a] = (b, c)
    if b != -1 :
        parent[b] = a
    if c != -1 :
        parent[c] = a

root = parent[1:].index(False)+1

in_order(root, 1)

answer = [0, 0]
for i in range(1, n+1):
    if width :
        width = max(dpt_arr[i])-min(dpt_arr[i])+1

    if width > answer[1] :
        answer = [i, width]

print(answer[0], answer[1])