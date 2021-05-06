from collections import defaultdict


def solution(gems):
    set_gems = set(gems)
    dict_gems = defaultdict(int)
    dict_gems[gems[0]] = 1
    start, end = (0, 0)
    answer = [0, len(gems)]
    while start < len(gems) and end < len(gems):
        if len(dict_gems) == len(set_gems):
            if end - start < answer[1] - answer[0]:
                answer = [start+1, end+1]

            if dict_gems.get(gems[start]):
                dict_gems[gems[start]] -= 1

            if dict_gems[gems[start]] == 0:
                del dict_gems[gems[start]]
            start += 1

        else:
            end += 1
            if end >= len(gems):
                break
            dict_gems[gems[end]] += 1
    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA",
      "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
