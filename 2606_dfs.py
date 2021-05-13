from collections import deque
import sys

computer = int(sys.stdin.readline().strip())
virus = int(sys.stdin.readline().strip())
matrix = [[0]*computer for _ in range(computer)]
for _ in range(virus):
    a, b = list(map(int, sys.stdin.readline().split()))
    a, b = a-1, b-1
    matrix[a][b] = matrix[b][a] = 1

answer = 0


def dfs(start, infect):
    infect.append(start)
    for i in range(len(matrix)):
        if matrix[start][i] == 1 and (i not in infect):
            dfs(i, infect)
    return len(infect) - 1


print(dfs(0, []))
