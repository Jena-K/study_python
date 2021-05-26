#n, s, a, b, fares
#n : 지점의 수
#s : 출발지
#a, b : A,B의 도착지점
#fares : 노드별 cost
def solution(n, s, a, b, fares):
    INF = int(1e9)

    graph = [[INF] * (n+1) for _ in range(n+1)]
    for i in range(n+1):
        graph[i][i] = 0

    node = [[] for i in range(n+1)]
    for i, j, k in fares :
        node[i].append((j, k))
        graph[i][j] = k
        graph[j][i] = k
        
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k])
                                    #3              4        5
    Min = INF
    for i in range(n+1):
        Min = min(graph[s][i] + graph[i][a] + graph[i][b], Min)

    return Min

n, s, a, b, fares = 6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n, s, a, b, fares))
n, s, a, b, fares = 7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
n, s, a, b, fares = 6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]