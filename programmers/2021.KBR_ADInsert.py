#play_time  재생시간 길이
#adv_time   공익광고의 재생시간 길이
#logs       시청자들이 해당 동영상을 재생했던 구간 정보
def ToSec(t):
    temp = list(map(int, t.split(':')))
    t = temp[0]*3600+temp[1]*60+temp[2]
    return t

def ToTime(t):
    h = t//3600
    m = t%3600//60
    s = t%60
    return str(h).rjust(2, '0')+':'+str(m).rjust(2, '0')+':'+str(s).rjust(2, '0')

def solution(play_time, adv_time, logs):
    cnt = 0
    play_time = ToSec(play_time)
    adv_time = ToSec(adv_time)
    all_time = [0] * (play_time+1)
    
    for i in range(len(logs)):
        temp = list(map(ToSec, logs[i].split('-')))
        all_time[temp[0]] += 1
        all_time[temp[1]] -= 1

    for i in range(1, play_time):
        all_time[i] += all_time[i-1]  
    for i in range(1, play_time):
        all_time[i] += all_time[i-1]

    Max = 0
    answer = 0

    for i in range(adv_time-1, play_time):
        if Max < all_time[i] - all_time[i-adv_time] :
            Max = all_time[i] - all_time[i-adv_time]
            answer = i-adv_time+1
    
    return ToTime(answer)



play_time, adv_time, logs = "02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
#print(solution(play_time, adv_time, logs))
print('01:30:59\n')
play_time, adv_time, logs = "99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
#print(solution(play_time, adv_time, logs))
print('01:00:00\n')
play_time, adv_time, logs = "50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]
print(solution(play_time, adv_time, logs))
print('00:00:00')


