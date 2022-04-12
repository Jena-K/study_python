def solution(numbers, hand):
    maps = [[i//3, i%3] for i in range(15)]
    L, R = 10, 12
    answer = ''
    for number in numbers:
        #0번이라면 11로 변환
        if number == 0 : number = 11
        print(answer[-1:])
        distance_left = abs((number-1)%3 - (L-1)%3) + abs((number-1)//3 - (L-1)//3)
        distance_right = abs((number-1)%3 - (R-1)%3) + abs((number-1)//3 - (R-1)//3)
        print(L, R, ' - ', distance_left, distance_right, number)
        #왼쪽이라면 왼손
        if number%3 == 1 :
            answer += 'L' 
            L = number
            
        #오른쪽이라면 오른손
        elif number%3 == 0 :
            answer += 'R'
            R = number
            
        #중간이라면
        else :            
            if distance_left == distance_right :
                if hand == 'right' :
                    answer += 'R' 
                    R = number
                else :
                    answer += 'L' 
                    L = number
                
            else :
                if distance_left > distance_right :
                    answer += 'R'
                    R = number
                else :
                    answer += 'L'
                    L = number
    return answer



numbers, hand = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"
print(solution(numbers, hand))
print("LRLLLRLLRRL")

numbers, hand = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"
print(solution(numbers, hand))
print("LRLLRRLLLRR")
numbers, hand = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"
print(solution(numbers, hand))
print("LLRLLRLLRL")
