#p355.exwall_check
#not Completed
from itertools import permutations
n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]

def solution(n, weak, dist):
    #n=외벽의 길이. 취약지점의 위치 weak
    # 1시간동안 이동거리 배열 dist
    #최소값
    weak_dist = []
    lw = len(weak)
    
    weak_dist = [weak[i+1]-weak[i] for i in range(lw-1)] + [n+weak[0]-weak[lw-1]]
    print(weak_dist)

    perm = permutations(dist, lw)
    print(list(perm))
    #dist combinations
    for p in perm:
        #each dist
        for i in p:
            wd = 0
            #compare distance
            while wd < len(weak_dist):
                if weak_dist[wd] > i :
                    wd+=1
                else : 
                    i -= wd
            if 1: pass

    answer = 0
    return answer

print(solution(n, weak, dist))