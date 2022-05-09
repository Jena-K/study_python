import heapq

def solution(jobs):
    answer = []
    
    q = []
    arr = [[] for _ in range(2002)]
    t = 0 #작업 시작 가능 시간
    ans = 0 #총 대기시간
    
    for a, b in jobs:
        arr[a].append(b)
        
    for i in range(2002):
        ans += len(q)
        
        for a, b in i:
            heapq.heappush(q, b)
            
        
    
    return None
    '''
    * n초에 하는 작업
    
    n초까지 들어온 값을 heap에 삽입
    그리고 현재 작업중이 아니라면 끝나는 시간이 가장 빠른 녀석을 pop
    현재 시간 t
    매 초마다 heapq의 길이만큼 cnt += t
    '''
    
    return answer

#jobs = [[0, 3], [1, 9], [2, 6]]
jobs = [[0, 3], [1, 9], [4, 5], [2, 6]]
print(solution(jobs))