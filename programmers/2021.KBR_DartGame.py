def solution(dartResult):
    answer = [0]*3
    award = [0]*3
    cnt = -1
    Num = ''
    for i in dartResult:
        if i.isdigit():
            Num += i

        elif i.isalpha():
            cnt+=1
            answer[cnt] = int(Num)
            Num = ''
            Pow = i.translate(str.maketrans('SDT', '123'))# S->1, D->2, T->3 으로 바꾸는 함수
            answer[cnt] **= int(Pow)

        elif i == '*':
            answer[cnt] *= 2
            if cnt != 0 :
                answer[cnt-1] *= 2
            award[cnt] = i
        elif i == '#':
            answer[cnt] *= -1
            award[cnt] = i
            
    return sum(answer)

data = [['1S2D*3T'],
['1D2S#10S'],
['1D2S0T'],
['1S*2T*3S'],
['1D#2S*3S'],
['1T2D3D#'],
['1D2S3T*']]

print(solution(data[3][0]))