import sys
from collections import deque

maps = []
birds = []
# R, C = map(int, sys.stdin.readline().split())
R, C = 8, 17

# maps = [sys.stdin.readline().strip() for _ in range(R)]
maps = ['...XXXXXX..XX.XXX', '....XXXXXXXXX.XXX', '...XXXXXXXXXXXX..', '..XXXXX.LXXXXXX..',
        '.XXXXXX..XXXXXX..', 'XXXXXXX...XXXX...', '..XXXXX...XXX....', '....XXXXX.XXXL...']

for r in range(R):
    for c in range(C):
        if maps[r][c] == "L":
            birds.append((r, c))

time = [[0 for _ in range(C)] for _ in range(R)]


def melting_time(maps: list):
    visitied = [[False for _ in range(C)] for _ in range(R)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    for r in range(R):
        for c in range(C):
            if maps[r][c] == "." or maps[r][c] == "L":
                queue.append((r, c))
                visitied[r][c] = True
    last_time = 0
    while queue:
        row, col = queue.popleft()
        for k in range(4):
            _row = row + dx[k]
            _col = col + dy[k]
            if 0 <= _row < R and 0 <= _col < C and not visitied[_row][_col] and maps[_row][_col] != "L":
                queue.append((_row, _col))
                time[_row][_col] = time[row][col] + 1
                visitied[_row][_col] = True
                last_time = time[_row][_col]
    return last_time


def bfs(start: tuple, maps: list, mid: int, end: tuple):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append(start)
    visitied = [[False for _ in range(C)] for _ in range(R)]
    while queue:
        row, col = queue.popleft()
        visitied[row][col] = True
        for i in range(4):
            _row = row + dx[i]
            _col = col + dy[i]
            if 0 <= _row < R and 0 <= _col < C and not visitied[_row][_col]:
                visitied[_row][_col] = True
                if _row == end[0] and _col == end[1]:
                    return True
                if time[_row][_col] <= mid:
                    queue.append((_row, _col))
    return False


_min, _max = 0, melting_time(maps)
answer = _max

while _min <= _max:
    mid = (_min + _max) // 2
    if bfs(birds[0], maps, mid, birds[1]):
        answer = mid
        _max = mid - 1
    else:
        _min = mid + 1
print(answer)
