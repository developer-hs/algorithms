import sys

n, m = map(int, sys.stdin.readline().split())

numbers = list(map(int, sys.stdin.readline().split()))

numbers = sorted(numbers)


def dfs(answer, idx):
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return
    overlap = 0
    for i in range(idx, n):
        if overlap != numbers[i]:
            overlap = numbers[i]
            answer.append(numbers[i])
            dfs(answer, i)
            answer.pop()


dfs([], 0)
