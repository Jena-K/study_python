#미해결
# 
def solution(grid):
    direction = ['S', 'L', 'R']
    maps = [[[[] for _ in range(len(grid[0]))] for _ in range(len(grid))] for _ in range(3)] 

    '''
    
    '''

            
grid, result = ["SL","LR"], [16]
solution(grid)
grid, result = ["S"], [1,1,1,1]
solution(grid)
grid, result = ["R","R"], [4,4]
solution(grid)