# 숙바꼭질 : https://www.acmicpc.net/problem/1697
from collections import deque
import sys
n, k = map(int, sys.stdin.readline().split())

visited = [False] * 100001

queue = deque()
queue.append((n, 0))
while queue:
    dis, sec = queue.popleft()
    if not visited[dis]:
        visited[dis] = True
        if dis == k:
            print(sec)
            sys.exit()

        sec += 1

        temp = [dis*2, dis+1, dis-1]
        for t in temp:
            if t <= 100000 and t >= 0:
                queue.append((t, sec))
