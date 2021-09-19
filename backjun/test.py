import sys
input = lambda : sys.stdin.readline().strip()
for _ in range(int(input())):
    orders = input()
    n = int(input())
    nums = input()[1:-1].split(',')

    if nums[0] == '': nums = []
        
    flag = True
    way = 1
    for o in orders :
        if o == 'R':
            way *= -1
        else :
            if nums :
                if way == 1:
                    nums = nums[1:]
                else :
                    nums = nums[:-1]
            else :
                flag = False
                break
        print(nums)
    if way == -1:
        nums.reverse()

    if flag :
        print('['+','.join(nums)+']')
    else :
        print('error')