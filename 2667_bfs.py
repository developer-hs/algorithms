import sys
from collections import deque
size = int(sys.stdin.readline().strip())
maps = [list(map(int, sys.stdin.readline().strip())) for _ in range(size)]
visited = [[False]*size for _ in range(size)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(start, maps):
    answer = 0
    queue = deque()
    queue.append(start)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < size and 0 <= ny < size and maps[nx][ny] == 1:
                maps[nx][ny] += 1
                answer += 1
                queue.append((nx, ny))
                visited[nx][ny] = True
        if not answer:
            answer = 1
    return answer


cnt = 0
answer = []
for i in range(len(maps)):
    for x in range(len(maps[0])):
        if maps[i][x] == 1:
            bfs_ = bfs((i, x), maps)
            if bfs_:
                cnt += 1
                answer.append(bfs_)


print(cnt)
for a in sorted(answer):
    print(a)
