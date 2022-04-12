#p329.pillarNBeam
n = 5
#build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
build_frame = [[0,0,0,1], [2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

def impossible(build):
    for x, y, a in build:
        #piller
        if a == 0:
            #바닥 or 밑에 기둥 or 왼쪽에 보 or 오른쪽에 보
            if y == 0 or [x, y-1, 0] in build or [x-1, y, 1] in build or [x, y, 1] in build:
                continue
        #beam
        if a == 1:
            #바닥이라면 bak
            if y == 0 : True
            #보보보 or 양 밑에 기둥 
            elif [x-1, y, 1] in build and [x+1, y, 1] in build or \
                [x, y-1, 0] in build or [x+1, y-1, 0] in build :
                continue
        return True

def solution(n, build_frame):
    builded = []
    for x, y, a, b in build_frame :
        if b == 1:
            builded.append([x, y, a])
            if impossible(builded) : builded.pop()
        elif b == 0:
            builded.pop(builded.index([x, y, a]))
            if impossible(builded) : builded.append([x, y, a])
            
    return sorted(builded)

print(solution(n, build_frame))

