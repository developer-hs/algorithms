from collections import deque
import sys

maps = [['.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', 'X', 'X', '.', 'X', 'X', 'X'], ['.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', 'X', 'X', 'X'], ['.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.'], ['.', '.', 'X', 'X', 'X', 'X', 'X', '.', 'L', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.'], [
    '.', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.'], ['X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', 'X', 'X', 'X', 'X', '.', '.', '.'], ['.', '.', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', 'X', 'X', 'X', '.', '.', '.', '.'], ['.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', '.', 'X', 'X', 'X', 'L', '.', '.', '.']]
birds = [(3, 8), (7, 13)]
r, c = map(int, sys.stdin.readline().split())
# for y in range(r):
#     arr = list(sys.stdin.readline().replace("\n", ""))
#     maps.append(arr)
#     for x in range(len(arr)):
#         if arr[x] == "L":
#             birds.append((y, x))

time = [[0 for _ in range(c)] for _ in range(r)]


def melt_time_set(maps: list):
    visitied = [[False for _ in range(c)] for _ in range(r)]
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    queue = deque()
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] == "." or maps[y][x] == "L":
                queue.append((y, x))  # 바다이거나 백조인 부분
                visitied[y][x] = True
    print(queue)
    print(time)
    print(visitied)

    # 마지막으로 빙하가 녹은 시간
    last_time = 0
    while queue:
        y, x = queue.popleft()
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and not visitied[ny][nx] and maps[ny][nx] != "L":
                queue.append((ny, nx))
                time[ny][nx] = time[y][x] + 1
                visitied[ny][nx] = True
                last_time = time[ny][nx]
    return last_time


_min, _max = 0, melt_time_set(maps)
aswer = _max

print(_min, _max)
