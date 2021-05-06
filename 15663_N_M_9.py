import sys

n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

numbers = sorted(numbers)
visited = [False] * n


def dfs(answer):
    if len(answer) == m:

        return
    overlap = 0
    for i in range(n):
        if not visited[i] and overlap != numbers[i]:
            visited[i] = True
            answer.append(numbers[i])
            overlap = numbers[i]
            dfs(answer)
            visited[i] = False
            answer.pop()


dfs([])
