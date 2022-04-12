#p368.FixedPoint
from bisect import bisect_left, bisect_right
N = int(input())
Data  = list(map(int, input().split()))

def Binary_Search(Data, Start, End):
    if Start > End :
        return None
    
    Mid = (Start+End)//2

    if Data[Mid] == Mid : return Mid
    elif Data[Mid] > Mid : return Binary_Search(Data, Start, Mid-1)
    elif Data[Mid] < Mid : return Binary_Search(Data, Mid+1, End)
'''
def Binary():
    Start = 0
    End = N-1
    while Start <= End:
        Mid = (Start+End)//2
        #print(Start, Mid, End)
        if Data[Mid] > Mid :
            End = Mid-1
        else :
            Start = Mid+1
    if Start == Data[Start]:
        return Start
    elif Mid == Data[Mid] :
        return Mid
    elif End == Data[End] :
        return End
    else :
        return -1

#print(Binary())
'''
Result = Binary_Search(Data, 0, N-1)
if Result == None :
    print(-1)
else :
    print(Result)