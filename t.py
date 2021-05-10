from collections import defaultdict
from itertools import combinations


def solution(info, query):

    answer = []
    applicant = defaultdict(list)
    for x in info:
        x = x.split()
        keylist = x[:-1]
        score = int(x[-1])

        for i in range(5):
            for c in combinations(keylist, i):
                key = ''.join(c)
                applicant[key].append(score)

    for key in applicant.keys():
        applicant[key].sort()

    for x in query:
        q = []
        x = x.split(' ')

        for y in x:
            if y != "and" and y != "-":
                q.append(y)
        key = ''.join(q[:-1])
        score = int(q[-1])

        count = 0

        if key in applicant.keys():
            value = applicant[key]
            start, end = 0, len(value)

            while start <= end and start < len(value):
                mid = (start+end) // 2
                if value[mid] < score:
                    start = mid + 1
                else:
                    end = mid - 1
            count = len(value) - start
        answer.append(count)
    return answer


print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], [
      "java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))
