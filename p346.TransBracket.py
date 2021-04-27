#p346.TransBracket
#포기
def solution(p):
    if not p : return ''
    return division(p)

def reverse(u):
    temp = []
    for i in u:
        if i == '(' : temp.append(')')
        else : temp.append('(')
    return '(' + ''.join(temp) +')'

#균형잡힌 문자열로 분리
def division(p):
    if not p :
        return ''
    valance = 0
    for i in range(len(p)):
        if p[i] == '(':
            valance+=1
        elif p[i] == ')':
            valance -=1
        if valance == 0:
            u, v = p[:i+1], p[i+1:]
            break

    if p[-1] == '(':
        #균형잡힌 상태라면 뒤집기
        u = reverse(u[1:-1])

    return u+division(v)

a = '(()())()'
b = ')('
c = '()))((()'
print(solution(c))

'''
def solution(p):
    p = list(p)
    if not p:
        return ''

    #여는 괄호, 닫는 괄호, 시작점 초기화
    front, back, start = 0, 0, 0

    #균형잡힌 문자열을 탐색
    for i in range(len(p)):
        if p[i] == '(':
            front+=1
        elif p[i] == ')':
            back +=1

        #균형잡힌 문자열이라면
        if front==back:
            valance = 0
            for j in range(start, i+1):
                if p[j] == '(':
                    valance += 1
                elif p[j] == ')':
                    valance -= 1
                if valance < 0 :
                    #균형잡힌 상태라면 뒤집기
                    for k in range(start+1, i):
                        if p[k] == '(' : p[k] = ')'
                        else : p[k] = '('
                    p[start], p[i] = '(', ')'
                    start = i+1
                    break
            start = i+1
    return ''.join(p)

a = '(()())()'
b = ')('
c = '()))((()'
print(solution(')))))))(((((((())(((()))'))
'''