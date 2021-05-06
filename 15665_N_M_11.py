import sys

n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

numbers = sorted(numbers)


def dfs(answer):
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return
    overlap = 0
    for i in range(n):
        if overlap != numbers[i]:
            answer.append(numbers[i])
            overlap = numbers[i]
            dfs(answer)
            answer.pop()


dfs([])
