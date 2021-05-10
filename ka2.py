def solution(n, k, cmd):
    idx = 0
    maps = [i + 1 for i in range(-1, n-1)]
    remove_num = []
    answer = ""
    for c in cmd:
        if c[0] == "D":
            k = k + int(c[2])
        elif c[0] == "U":
            k = k - int(c[2])
        elif c[0] == "C":
            copy_maps = maps
            remove_num.append(maps.pop(k))
            if k == len(maps) - 1:
                k = -1
        elif c[0] == "Z":
            maps.insert(remove_num[-1], remove_num.pop(-1))
    while len(maps) != n:
        if maps[idx] != idx:
            maps.insert(idx, -1)
            idx += 1
        else:
            idx += 1
    for m in maps:
        if m != -1:
            answer += "O"
        else:
            answer += "X"
    return answer


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
