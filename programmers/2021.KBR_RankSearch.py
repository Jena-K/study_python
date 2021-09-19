from bisect import bisect_left
from itertools import combinations
from collections import defaultdict
def solution(info, query):
    answer = []
    db = defaultdict(list)
    #각각 인포가 해당되는 쿼리에 점수 등록
    for i in info:
        temp = [j for j in i.split()]
        condition = temp[:-1]
        score = temp[-1]
        for n in range(5):
            for c in list(combinations(range(4), n)):
                new_db = condition.copy()
                for c2 in c:
                    new_db[c2] = '-'
                db['/'.join(new_db)].append(int(score))
    
    #dic.values() 를 정렬
    for i in db.keys():
        db[i].sort()

    #쿼리에 해당하는 인포의 개수를 확인
    for qry in query :
        temp = [i for i in qry.split() if i != 'and']
        condition = '/'.join(temp[:-1])
        score = temp[-1]
        if condition in list(db.keys()):
            answer.append(len(db[condition])-bisect_left(db[condition], int(score)))
        else :
            answer.append(0)

    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
#info = ["java backend junior pizza 150"]
#query = ["java and backend and junior and pizza 100"]
print(solution(info,query))

