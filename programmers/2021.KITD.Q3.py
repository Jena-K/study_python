#n : 사람 수
#k : 시작점
#cmd : 명령
def solution(n, k, cmd):
    answer = ['O' for _ in range(n)]
    deleted = []
    for i in cmd:
        #위로
        if i[0]  == 'U':
            x = int(i[2:]) #  x = 남은 움직일 칸 개수 
            while x > 0 : #남은 움직일 칸 개수가 0일때까지 
                k-=1 #1칸 움직임
                if answer[k] =='O': #살아있다면 1칸 움직인걸로 셈 - C 당했다면 세지 않음 
                    x-=1 
        #아래로
        elif i[0] == 'D':
            x = int(i[2:])
            while x > 0 :
                k+=1
                if answer[k] =='O':
                    x-=1

        #삭제
        elif i[0] == 'C':
            deleted.append(k)
            answer[k] = 'X'
            #k = 4 -> 5 그런데 만약에 뒤에 살아있는애가 없다면 어쩌지??

            find = False # check 하려고 만든 변수 - 실행 됐다면 True 바꾸고 실행 안됐으면 그대로
            for i in range(k, n):
                if answer[i] == 'O' : #살아 있는 애를 발견했다면
                    k = i
                    find = True 
                    break
            if find == False:
                for i in range(k, -1, -1): #뒤에 살아있는 애가 없었다면, k 칸부터 0방향으로 검색 
                    if answer[i] == 'O':
                        k = i
                        break
                                  
        #삭제 취소    
        elif i[0] == 'Z':
            answer[deleted.pop()] = 'O' 

    return ''.join(answer)

n, k, cmd = 8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
print(solution(n,k,cmd))
#'OOOOXOOO'
n, k, cmd = 8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
print(solution(n,k,cmd))
#'OOXOXOOO'
'''
0무지
1콘
2어피치#
3제이지
4프로도
5네오
6튜브
7라이언
'''