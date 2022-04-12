#361.FaleRate
from collections import Counter
def solution(N, stages):
    answer = [[i] for i in range(N+1)]
    num_users = len(stages)

    stage_c = Counter(sorted(stages))

    for i in range(1,N+1):
        try:
            answer[i].append(stage_c[i]/num_users)
            num_users-=stage_c[i]
        except:
            answer[i].append(0)
    return [i[0] for i in sorted(answer[1:], key=lambda x : x[1], reverse=True)]