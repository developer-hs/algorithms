import sys

n, m = map(int, sys.stdin.readline().split())

numbers = list(map(int, sys.stdin.readline().split()))

numbers = sorted(numbers)


def dfs(answer):
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return

    for i in range(len(numbers)):
        if numbers[i] in answer:
            continue
        answer.append(numbers[i])
        dfs(answer)
        answer.pop()


dfs([])
