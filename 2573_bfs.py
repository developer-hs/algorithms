# 빙산 : https://www.acmicpc.net/problem/2573
import sys
from collections import deque
import copy
m, n = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]


def check_ice_lump(start, visited):
    queue = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue.append(start)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            mx, my = dx[i] + x, dy[i] + y
            if 0 <= mx < m and 0 <= my < n and not visited[mx][my]:
                queue.append((mx, my))
                visited[mx][my] = True
    return visited


def start_finder():
    visited = init_visited()
    starting_points = []
    for i in range(m):
        for x in range(n):
            if not visited[i][x]:
                visited = check_ice_lump((i, x), visited)
                starting_points.append((i, x))

    return starting_points


def init_visited():
    visited = [[False] * n for _ in range(m)]
    for i in range(m):
        for x in range(n):
            if maps[i][x] == 0:
                visited[i][x] = True
    return visited


def solution(maps, year):
    copy_maps = copy.deepcopy(maps)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    starting_points = deque(start_finder())
    visited = init_visited()
    if not starting_points:
        return 0
    if len(starting_points) >= 2:
        return year
    while starting_points:
        x, y = starting_points.popleft()
        visited[x][y] = True
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if 0 <= mx < m and 0 <= my < n and copy_maps[mx][my] == 0:
                if maps[x][y] >= 1:
                    maps[x][y] = maps[x][y] - 1
            elif not visited[mx][my]:
                visited[mx][my] = True
                starting_points.append((mx, my))

    return solution(maps, year+1)


print(solution(maps, 0))
