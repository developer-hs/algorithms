import sys

n, m = map(int, sys.stdin.readline().split())

numbers = list(map(int, sys.stdin.readline().split()))

numbers = sorted(numbers)


def dfs(answer, idx):
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(idx, len(numbers)):
        answer.append(numbers[i])
        dfs(answer, i)
        answer.pop()


dfs([], 0)
