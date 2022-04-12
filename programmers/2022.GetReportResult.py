def solution(id_list, report, k):
    #값을 지정할 딕셔너리 생성
    dic = {id:[] for id in id_list}
    mail = {id:0 for id in id_list}
    for rpt in report:
        a, b = rpt.split()
        if a not in dic[b]:
            dic[b].append(a)
            
    for id in id_list:
        if len(dic[id]) >= k :
            for i in dic[id]:
                mail[i] += 1
    return list(mail.values())


id_list, report, k = ["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2
print(solution(id_list, report, k))
#[2,1,1,0]
id_list, report, k =  ["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3
#[0,0]
print(solution(id_list, report, k))