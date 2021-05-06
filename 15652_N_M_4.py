import sys

n, m = map(int, sys.stdin.readline().split())


def dfs(value, idx):
    if len(value) == m:
        print(' '.join(map(str, value)))
        return
    for i in range(idx, n+1):
        value.append(i)
        dfs(value, i)
        value.pop()


dfs([], 1)
