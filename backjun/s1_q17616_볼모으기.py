n = input()
arr = input()

'''
이동
    1. 좌로 다 옮기기
        2. 왼쪽부터 오른쪽으로 탐지하다가 선택되지 않은 색이 나올 경우 Flag = 1
        3. 이어서 flag가 1인 상태에서 선택된 색이 나오면
            ans += 1
            끝까지 간다.
            
    우로 다 옮기기

이동 작업을 두 번(R, B) 반복하여 최소치 구하기
'''
MIN = 10**6
for c in ['R', 'B']:
    for j in [arr, arr[::-1]]:
        flag = 0
        cnt = 0
        for i in j :
            if flag == 0 and i != c :
                flag = 1
                continue
            elif flag == 1 and i == c :
                cnt += 1
        MIN = min(MIN, cnt)
print(MIN)