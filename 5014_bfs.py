# 스타트링크 : https://www.acmicpc.net/problem/5014
import sys
from collections import deque

f, s, g, u, d = list(map(int, sys.stdin.readline().split()))


def bfs(start: int):
    visited = [False]*(f+1)
    visited[start] = True
    queue = deque([(start, 0)])
    while queue:
        x, sec = queue.popleft()
        if x == g:
            return sec
        sec += 1
        if x + u <= f and not visited[x+u]:
            visited[x+u] = True
            queue.append((x+u, sec))
        if x - d >= 1 and not visited[x-d]:
            visited[x-d] = True
            queue.append((x-d, sec))
    return -1


answer = bfs(s)

if answer == -1:
    print("use the stairs")
else:
    print(answer)
