# 토마토 : https://www.acmicpc.net/problem/7569
import sys
from collections import deque
m, n, h = list(map(int, sys.stdin.readline().split()))

queue = deque()
maps = []

for _ in range(h):
    maps_ = []
    for _ in range(n):
        maps_.append(list(map(int, input().split())))
    maps.append(maps_)

for i in range(h):
    for j in range(n):
        for k in range(m):
            if maps[i][j][k] == 1:
                queue.append([i, j, k])

dz = [0, 0, 0, 0, -1, 1]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, - 1, 1, 0, 0, ]

while queue:
    z, x, y = queue.popleft()

    for i in range(6):
        nz = z + dz[i]
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and maps[nz][nx][ny] == 0:
            queue.append([nz, nx, ny])
            maps[nz][nx][ny] = maps[z][x][y] + 1

check_tot = False
result = -2

for i in maps:
    for j in i:
        for k in j:
            if (k == 0):
                check_tot = True
            result = max(result, k)

if check_tot:
    print(-1)
elif (result == -1):
    print(0)
else:
    print(result - 1)
