#응답완료시간 S
#처리시간 T
#MAX(t) = 3
from collections import Counter
def solution(lines):
    lines = [i.split()[1:] for i in lines]
    ans = []
    for i in range(len(lines)):
        temp = list(map(float, lines[i][0].split(':')))
        ans.append(temp[0]*3600+temp[1]*60+temp[2])
        for i in range(int(ans[-1]+float(lines[i][1][:-1]))%10):
            ans.append(ans[-1]+1)
        #ans.append(ans[-1]+float(lines[i][1][:-1]))
    ans = list(map(int, ans))
    print(ans)
    cnt = Counter(ans)

        
    return max(cnt.values())


lines = [
    "2016-09-15 01:00:04.001 2.0s",
    "2016-09-15 01:00:07.000 2s"]
print(solution(lines))
lines = [
    "2016-09-15 01:00:04.002 2.0s",
    "2016-09-15 01:00:07.000 2s"]
print(solution(lines))
lines = [
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"]
print(solution(lines))