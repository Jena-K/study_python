def solution(a, b):
    return sum([i*j for i, j in zip(a, b)])

a, b = [1,2,3,4], [-3,-1,0,2]
print(solution(a, b))
#result = 3
a, b = [-1,0,1], [1,0,-1]
print(solution(a, b))
#result = -2