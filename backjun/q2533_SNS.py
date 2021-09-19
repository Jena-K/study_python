n = int(input())
node = [[] for _ in range(n+1)]
def dfs(now, depth):
	global cnt1, cnt2
	if visited[now] :
		return
	visited[now] = True
	if depth%2 == 0:
		cnt1 += 1
	else : 
		cnt2 += 1

	for i in node[now]:
		dfs(i, depth+1)

	for _ in range(n):
		a, b = map(int, input().split())
		node[a].append(b)
		node[b].append(a)

for i in range(1, n):
	visited = False * (n+1)
	cnt1, cnt2 = 0, 0
	dfs(i, 1)
	if result > min(cnt1, cnt2):
		result = min(cnt1, cnt2)
print(result)