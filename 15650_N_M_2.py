import sys

N, M = map(int, sys.stdin.readline().split())


def solve(value, idx):
    if len(value) == M:
        print(' '.join(map(str, value)))
        return
    for i in range(idx, N+1):
        value.append(i)
        solve(value, i+1)
        value.pop()


solve([], 1)
