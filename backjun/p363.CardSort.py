#p363CardSort
import sys
import heapq
input = sys.stdin.readline
n = int(input())
heap = []
[heapq.heappush(heap, int(input())) for _ in range(n)]
answer = 0
while len(heap) > 1 :
    small_first = heapq.heappop(heap)
    small_second = heapq.heappop(heap)
    temp = small_first + small_second
    heapq.heappush(heap, temp)
    answer+=temp

print(answer)