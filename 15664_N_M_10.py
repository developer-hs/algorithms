import sys
n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

numbers = sorted(numbers)

visited = [False]*n


def dfs(answer, idx):
    if len(answer) == m:
        print(' '.join(map(str, answer)))
    overlap = 0
    for i in range(idx, n):
        if not visited[i] and overlap != numbers[i]:
            visited[i] = True
            answer.append(numbers[i])
            overlap = numbers[i]
            dfs(answer, i)
            answer.pop()
            visited[i] = False


dfs([], 0)
