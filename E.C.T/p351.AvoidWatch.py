#p351.AvoidWatch
n = int(input())
#T = teacher, S=Student, O=Wal, X=Empty
graph = [input().split() for _ in range(n)] 
students, teachers = [], []

for x in range(n):
    for y in range(n):
        if graph[x][y] == 'S':
            students.append((x, y))
        elif graph[x][y] == 'T':
            teachers.append((x, y))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#Check Avoid
def Search(xy):
    for d in range(4):
        x, y = xy
        x += dx[d]
        y += dy[d]
        while x >= 0 and y >= 0 and x < n and y < n and graph[x][y] != 'O':
            if graph[x][y] == 'S' :
                return False
            x += dx[d]
            y += dy[d]
    return True

def Build_wall(cnt):
    #벽을 3개 지었다면 감시를 피했는지 확인
    if cnt == 3 :
        for teacher in teachers:
            if Search(teacher) == False:
                return False
        return True
    for x in range(n):
        for y in range(n):
            if graph[x][y] == 'X':
                graph[x][y] = 'O'
                if Build_wall(cnt+1) == True :
                    return True
                graph[x][y] = 'X'

if Build_wall(0) :
    print('Yes')
else :
    print('No')
