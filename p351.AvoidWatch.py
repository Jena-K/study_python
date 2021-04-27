#p351.AvoidWatch
#skip
n = int(input())
# T = teacher, S=Student, O=Wal, X=Empty
graph = [input().split() for _ in range(n)]
student, teacher = [], []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'S':
            student.append((i, j))
        if graph[i][j] == 'T':
            teacher.append((i, j))

def detected():
    for x, y in student:
        nx = x
        while nx >= 0 and graph[nx][y] != 'O':
            if graph[nx][y] == 'T':
                return False
            nx-=1
        nx = x
        while nx < n and graph[nx][y] != 'O' :
            if graph[nx][y] == 'T':
                return False
            nx+=1
        ny = y
        while ny >= 0 and graph[x][ny] != 'O' :
            if graph[x][ny] == 'T':
                return False
            ny-=1
        ny = y
        while ny < n and graph[x][ny] != 'O' :
            if graph[x][ny] == 'T':
                return False
            ny+=1
    return True

answer = False
def solution(cnt):
    global answer
    if cnt == 3:
        if detected() :
            answer = True
        return

    for x in range(n):
        for y in range(n):
            if graph[x][y] == 'X':
                graph[x][y] = 'O'
                cnt+=1
                solution(cnt)
                graph[x][y] = 'X'
                cnt-=1

solution(0)

if answer :
    print('Yes')
else :
    print('No')

