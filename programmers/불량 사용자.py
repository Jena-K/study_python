import re

def solution(user_id, banned_id):
    answer = []
    anset = set()
    for ban in banned_id:
        arr = set()
        r = re.compile(ban.replace('*', '.'))
        for user in user_id :
            result = r.match(user)
            if result and len(user) == len(result.group()):
                arr.add(user)
        answer.append(arr)
        anset|=(arr)
        
    
    print(anset)
    print(answer)
    # return anset



user_id, banned_id, result = ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"], 2
print(solution(user_id, banned_id))
user_id, banned_id, result = ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"], 2
print(solution(user_id, banned_id))
user_id, banned_id, result = ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"], 3
print(solution(user_id, banned_id))