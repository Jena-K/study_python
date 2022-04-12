def solution(numbers):
    answer = 0
    for n in range(0, 10):
        if n not in numbers:
            answer += n
            
    return answer

numbers	 = [1,2,3,4,6,7,8,0]
print(solution(numbers))
#14
numbers = [5,8,4,0,6,7,9]
print(solution(numbers))
#6