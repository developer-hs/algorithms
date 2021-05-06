import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

maps = [list(map(int, sys.stdin.readline().strip())) for _ in range(m)]

dist = [[-1]*n for _ in range(m)]

queue = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue.append((0, 0))

dist[0][0] = 0
while queue:
    x, y = queue.popleft()

    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        if 0 <= mx < m and 0 <= my < n:
            if dist[mx][my] == -1:
                if maps[mx][my] == 0:
                    dist[mx][my] = dist[x][y]
                    queue.appendleft((mx, my))
                else:
                    dist[mx][my] = dist[x][y] + 1
                    queue.append((mx, my))

print(dist[m-1][n-1])
