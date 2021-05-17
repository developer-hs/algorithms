# 안전영역 : https://www.acmicpc.net/problem/2468
import sys
from collections import deque
num = int(sys.stdin.readline().strip())
maps = []
numbers = []
answer_li = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(num):
    li = list(map(int, sys.stdin.readline().split()))
    maps.append(li)
    for i in li:
        if i not in numbers:
            numbers.append(i)

numbers = sorted(numbers)


def bfs(visited, start):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append(start)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < num and 0 <= ny < num and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
    return True


while numbers:
    visited = [[False]*num for _ in range(num)]
    target = numbers.pop(0)
    for i in range(num):
        for x in range(num):
            if target >= maps[i][x]:
                visited[i][x] = True
    answer = 0
    for i in range(len(visited)):
        for x in range(len(visited)):
            if visited[i][x] == False:
                bfs(visited, (i, x))
                answer += 1
    answer_li.append(answer)

if max(answer_li) >= 1:
    print(max(answer_li))
else:
    print(1)
