def validated(places, search, idx):
    o_count = 0
    safe = False
    check = True
    for place in places[search:]:
        if place[idx] == "P" and 1 <= o_count > 3 and not safe:
            return False

        elif place[idx] == "P" and safe:
            safe = False

        elif place[idx] == "O":
            o_count += 1

            if check:
                if 1 <= idx < 4:
                    if place[idx + 1] == "P" or place[idx - 1] == "P":
                        return False
                    if 1 <= search:
                        if places[search-1][idx + 1] == "P" or places[search-1][idx - 1] == "P":
                            return False
                elif idx == 0:
                    if place[idx + 1] == "P":
                        return False
                    if 1 <= search:
                        if places[search-1][idx + 1] == "P":
                            return False
                elif idx == 4:
                    if place[idx - 1] == "P":
                        return False
                    if 1 <= search:
                        if places[search-1][idx - 1] == "P":
                            return False

        elif place[idx] == "X":
            safe = True

        check = False

    return True


def solution(places):
    answer = []
    break_sw = False
    for i in range(len(places)):
        for x in range(len(places[i])):
            if break_sw:
                break_sw = False
                break
            if "P" not in places[i][x]:
                continue
            if "PP" in places[i][x]:
                answer.append(0)
                break
            for j in range(len(places[i][x])):
                if "P" == places[i][x][j]:
                    valid = validated(places[i], x+1, j)
                    if not valid:
                        answer.append(0)
                        break_sw = True
                        break
                    else:
                        continue
        else:
            answer.append(1)

    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP",
      "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
