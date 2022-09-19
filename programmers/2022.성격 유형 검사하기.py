'''
타입 8개를 지정
2개씩 묶어서 더 큰 값이 해당 사람의 성격 판단 
    같다면 더 앞에 있는 녀석이 해당 성격
'''

def solution(survey, choices):
    n = len(survey)
        
    types = ['RT', 'CF', 'JM', 'AN']
    type_dict = dict()
    for idx, type in enumerate(types):
        type_dict[type] = (idx, 1)
        type_dict[type[::-1]] = (idx, -1)
        
    score = [0 for _ in range(4)]
    
    for i in range(n):
        score[type_dict[survey[i]][0]] += (choices[i]-4) * type_dict[survey[i]][1]
    
    answer = ''
    for i in range(4):
        if score[i] <= 0 :
            answer += types[i][0]
        else :
            answer += types[i][1]
            
    return answer

survey, choices, result = ["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5], "TCMA"
print(solution(survey, choices))
survey, choices, result = ["TR", "RT", "TR"], [7, 1, 3], "RCJA"
print(solution(survey, choices))
