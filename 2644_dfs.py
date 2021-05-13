import sys
# 촌수계산 https://www.acmicpc.net/problem/2644
people = int(sys.stdin.readline().strip())
target_1, target_2 = list(map(int, sys.stdin.readline().split()))
num = int(sys.stdin.readline().strip())
matrix = [[0] * people for _ in range(people)]

target_1, target_2 = target_1 - 1, target_2 - 1
for _ in range(num):
    a, b = list(map(int, sys.stdin.readline().split()))
    a = a - 1
    b = b - 1
    matrix[a][b] = matrix[b][a] = 1

answer = 0
break_sw = False


def dfs(start, visited):
    global answer, break_sw
    visited += [start]
    for i in range(people):
        if matrix[start][i] == 1 and i not in visited:
            if break_sw:
                return answer
            answer += 1
            if i == target_2:
                break_sw = True
                return answer
            dfs(i, visited)
    if not break_sw:
        answer -= 1
    return answer


print(dfs(target_1, []))
