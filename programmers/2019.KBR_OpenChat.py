def solution(record):
    action = {'Enter':'님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}
    answer = []
    users = {}
    for i in record:
        data = i.split()
        if data[0] in ['Enter', 'Change']:
            users[data[1]] = data[2]

    for i in record :
        data = i.split()
        if data[0] != 'Change':
            answer.append(users[data[1]]+action[data[0]])

    return answer








record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))