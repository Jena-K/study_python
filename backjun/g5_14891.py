#N극:0 S극:1
wheel = [list(map(int, input())) for _ in range(4)]
c = [(0, 0)] * 4
k = int(input())
order = [list(map(int, input().split())) for _ in range(k)]

'''
   0
 7   1
6     2
 5   3
   4
'''
#i: 톱니바퀴 번호, o:명령(1:시계방향, -1: 반시계)
for i, o in order :
    c[i] = (1, o)
    #기준 톱니바퀴의 좌측으로 진행
    for x in range(i, 0, -1):
        #접점의 극이 다르면
        if wheel[i][6] != wheel[i-1][2] :
            c[i+1] = (1, c[i][1]*(-1))
            pass
        else :
            break


    #기준 톱니바퀴의 우측으로 진행
    for x in range(i, 3):
          #접점의 극이 다르면
        if wheel[i][2] != wheel[i+1][6] :
            #뒤에 휠을 앞 휠의 반대 방향으로 회전
            pass
        else :
            break

#정답 출력
ans = 0
for i in range(4):
    if wheel[0] == 1 :
        ans+=2**i

print(i)