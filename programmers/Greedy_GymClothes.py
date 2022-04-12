def solution(n, lost, reserve):
    answer = 0
    arr = [1] * n
    
    for i in lost:
        arr[i-1] = 0
        
    for i in reserve:
        arr[i-1] += 1
    
    for i in range(n):
        if arr[i] == 0:
            if arr[max(0, i-1)] == 2:
                arr[max(0, i-1)] -= 1
                arr[i] = 1
            elif arr[min(n-1, i+1)] == 2:
                arr[min(n-1, i+1)] -= 1
                arr[i] += 1

    return len([i for i in arr if i != 0])




n, lost, reserve = 5, [2, 4], [1, 3, 5]
print(solution(n, lost, reserve))
#return = 5

n, lost, reserve = 5, [2, 4], [3]
print(solution(n, lost, reserve))
#return = 4

n, lost, reserve = 3, [3], [1]
print(solution(n, lost, reserve))
#return = 2