from itertools import combinations
from collections import Counter

#Edited Sorve
def solution(orders, course):
    answer = []
    for c in course:
        order_list = []
        for order in orders:
            order_list += combinations(sorted(order), c)

        order_count = Counter(order_list).most_common()
        answer+=[''.join(o) for o, c in order_count if c > 1 and c == order_count[0][1]]
    return sorted(answer)


orders, course, result = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4], ["AC", "ACDE", "BCFG", "CDE"]
print(solution(orders, course))

orders, course, result = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5], ["ACD", "AD", "ADE", "CD", "XYZ"]
print(solution(orders, course))

orders, course, result = ["XYZ", "XWY", "WXA"], [2,3,4], ["WX", "XY"]
print(solution(orders, course))