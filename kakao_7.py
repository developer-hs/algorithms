from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    answer = []
    temp = defaultdict(int)
    check = defaultdict(int)
    for k in course:
        candidates = []
        for menu_li in orders:
            for li in combinations(menu_li, k):
                res = ''.join(sorted(li))
                temp[res] += 1
    temp = sorted(temp.items(), key=lambda x: x[1], reverse=True)
    for t in temp:
        if not check[len(t[0])] and t[1] >= 2:
            check[len(t[0])] = t[1]
            answer.append(t[0])
        else:
            if t[1] == check[len(t[0])] and t[1] >= 2:
                answer.append(t[0])
    return sorted(answer)


print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
