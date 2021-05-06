import sys

n, m = map(int, sys.stdin.readline().split())


def dfs(value):
    if len(value) == m:
        print(' '.join(map(str, value)))
        return
    for i in range(1, n+1):
        value.append(i)
        dfs(value)
        value.pop()


dfs([])
