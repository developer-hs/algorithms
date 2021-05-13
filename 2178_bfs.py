import sys
from collections import deque
'''
4 6
101111
101010
101011
111011

----
15
----
'''
n, m = list(map(int, sys.stdin.readline().split()))
maps = [str(sys.stdin.readline().strip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dist = [[0]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]

queue = deque()
queue.append((0, 0))
visited[0][0] = True
dist[0][0] = 1

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and maps[nx][ny] == "1":
                queue.append((nx, ny))
                visited[nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1

print(dist[-1][-1])
