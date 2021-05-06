import sys

n, m, v = map(int, sys.stdin.readline().split())
matrix = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    matrix[a][b] = matrix[b][a] = 1
print(matrix)


def bfs(start):
    visited = [start]
    queue = [start]
    while queue:
        n = queue.pop(0)
        for c in range(len(matrix[start])):
            if matrix[n][c] == 1 and (c not in visited):
                # 한번 돌면서 조건에 걸리는 모든 것들을 queue 에 담고
                # queue 가 없얼질때 까지(모든경우를 다 돌 때 까지) 반복
                visited.append(c)
                queue.append(c)
    return visited


def dfs(start, visited):
    visited += [start]
    for c in range(len(matrix[start])):
        if matrix[start][c] == 1 and (c not in visited):
            # 한번 돌면서 조건에 걸리면 그 값으로 재귀
            # 재귀 에서 return 된 visited 값은 그 재귀가 실행되기 전 visited 에 덮어쓴다
            dfs(c, visited)
    return visited


print(dfs(v, []))
print(bfs(v))
