from itertools import permutations
import sys

n, m = map(int, sys.stdin.readline().split())


def solution(visited):
    if len(visited) == m:
        print(' '.join(map(str, visited)))
        return
    for i in range(1, n + 1):
        if i in visited:
            continue

        solution(visited + [i])


solution([])
