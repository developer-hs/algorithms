def solution(s):
    answer = []
    s = s[1:-1].split("},")
    li = [[""] for _ in range(len(s))]
    idx = -1
    num_sw = False
    append_sw = False
    for i in "".join(s):
        if i == "{":
            num_sw = True
            append_sw = False
            idx += 1
            continue
        elif i == "}":
            num_sw = False
            continue
        elif i == ",":
            append_sw = True
            continue
        elif num_sw:
            if append_sw:
                li[idx].append(i)
                append_sw = False
            else:
                li[idx][-1] += i
    li = sorted(li, key=lambda x: len(x))
    for l in li:
        for i in l[::-1]:
            if int(i) not in answer:
                answer.append(int(i))
    return answer


print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
