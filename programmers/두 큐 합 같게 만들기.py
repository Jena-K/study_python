from collections import deque
def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    sq1, sq2 = sum(q1), sum(q2)
    
    cnt = 0
    for _ in range(len(q1)*2 + len(q2)*2):
        if sq1 > sq2:
            x = q1.popleft()
            sq1 -= x
            sq2 += x
            q2.append(x)
        elif sq1 < sq2 :
            x = q2.popleft()
            sq1 += x
            sq2 -= x
            q1.append(x)
        else :
            return cnt
        
        cnt += 1
        
    return -1


queue1,queue2,result = [3, 2, 7, 2],[4, 6, 5, 1],2
print(solution(queue1,queue2))
queue1,queue2,result = [1, 2, 1, 2],[1, 10, 1, 2],7
print(solution(queue1,queue2))
queue1,queue2,result = [1, 1],[1, 5],-1
print(solution(queue1,queue2))