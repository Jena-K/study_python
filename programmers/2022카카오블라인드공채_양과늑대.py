def solution(info, edges):
    global MAX
    MAX = 0
    def dfs(togo, sheep_n, wolf_n):
        global MAX
        if sheep_n <= wolf_n or not togo:
            MAX = max(MAX, sheep_n) # 최대값 저장
            return
        
        for idx, i in enumerate(togo):
            #parameter 1: 모든 노드를 방문하는 경우의 수를 찾아야 하므로 방문할 노드 값으로 하위노드 추가
            #parameter 2, 3: 양인 경우 양 +1 늑대인 경우 늑대 +1
            dfs(togo[:idx] + togo[idx+1:] + ch[i], sheep_n+(info[i]+1)%2, wolf_n+info[i]%2) 

    ch = [[] for _ in range(len(info))]
    
    for parent, child in edges:
        ch[parent].append(child)
    
    dfs(ch[0], 1, 0)
    
    return MAX

'''
자식노드, 현재까지 늑대 수, 현재까지 양의 수
자식노드들을 탐색
'''


info, edges, result = [0,0,1,1,1,0,1,0,1,0,1,1],  [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]],  5
print(solution(info, edges)) 
#info, edges, result = [0,1,0,1,1,0,1,0,0,1,0],  [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]],  5
#print(solution(info, edges))