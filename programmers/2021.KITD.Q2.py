#P Person
#O Empty
#X Partition

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def check(place):
    lp = len(place)
    for x in range(lp):
        for y in range(lp):
            if place[x][y] == 'P':
                #1회차 : 4방 탐색
                for d in range(4):
                    nx = x+dx[d]
                    ny = y+dy[d]
                    if nx >= 0 and ny >= 0 and nx < lp and ny < lp :
                        if place[nx][ny] == 'P' :
                            return 0
                #2회차 : 4방(2칸) 탐색
                for d in range(4):
                    nx = x+dx[d]*2
                    ny = y+dy[d]*2
                    if nx >= 0 and ny >= 0 and nx < lp and ny < lp :
                        if place[nx][ny] == 'P' and place[x+dx[d]][y+dy[d]] != 'X':
                            return 0
                #3회차 : 대각선 탐색
                ndx = [-1, 1, -1, 1]
                ndy = [1, 1, -1 ,-1]
                for d in range(4):
                    nx = x+ndx[d]
                    ny = y+ndy[d]
                    if nx >= 0 and ny >= 0 and nx < lp and ny < lp :
                        if place[nx][ny] == 'P':
                            for dd in range(4):
                                if place[nx][y] != 'X' or place[x][ny] != 'X':
                                    return 0
    return 1


def solution(places):
    answer = []
    for place in places:
        answer.append(check(place))
    return answer
places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))