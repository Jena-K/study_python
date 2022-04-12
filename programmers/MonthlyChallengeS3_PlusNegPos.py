def solution(absolutes, signs):
    answer = 0
    for i, j in zip(absolutes, signs):
        if j == True:
            answer += i
        else :
            answer += i*(-1)

    return answer


absolutes, signs = [4,7,12], [True,False,True]
print(solution(absolutes, signs))
#result = 9
absolutes, signs = [1,2,3], [False,False,True]
print(solution(absolutes, signs))
#result = 0