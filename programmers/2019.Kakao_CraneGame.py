def solution(board, moves):
    stack = []
    answer = 0
    n = len(board[0])
    
    for move in moves:
        for i in range(n):
            if board[i][move-1] != 0 :
                temp, board[i][move-1] = board[i][move-1], 0
                stack.append(temp)
                if len(stack) < 2 :
                    break
                elif stack[-1] == stack[-2] :
                    stack.pop()
                    stack.pop()
                    answer += 2
                break
    return answer

board, moves = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]
###result = 4
print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))