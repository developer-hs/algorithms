# 로봇 청소기 : https://www.acmicpc.net/problem/14503
import sys
from collections import deque
m, n = list(map(int, sys.stdin.readline().split()))

r, c, d = list(map(int, sys.stdin.readline().split()))

maps = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def change_direction(d):
    if(d == 0):
        return 3
    elif(d == 1):
        return 0
    elif(d == 2):
        return 1
    elif(d == 3):
        return 2


def back(d):
    if d == 0:
        return 2
    elif d == 1:
        return 3
    elif d == 2:
        return 0
    elif d == 3:
        return 1


def solution():
    global r, c, d
    answer = 1
    queue = deque()
    queue.append((r, c, d))
    maps[r][c] = 2
    while queue:
        x, y, d = queue.popleft()
        copy_d = d
        for i in range(4):
            copy_d = change_direction(copy_d)
            mx = x + dx[copy_d]
            my = y + dy[copy_d]
            if 0 <= mx < m and 0 <= my < n and maps[mx][my] == 0:
                answer += 1
                maps[mx][my] = 2
                queue.append((mx, my, copy_d))
                break
            elif i == 3:
                mx = x + dx[back(d)]
                my = y + dy[back(d)]
                queue.append((mx, my, d))
                if maps[mx][my] == 1:
                    return answer

    return answer


print(solution())
