import sys
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4suNtaXFEDFAUf&categoryId=AV4suNtaXFEDFAUf&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=&pageSize=10&pageIndex=1
ite = int(sys.stdin.readline().strip())


def make_visited(maps):
    visited = [[False]*n for _ in range(n)]
    for i in range(len(maps)):
        for x in range(len(maps)):
            if maps[i][x] == 1:
                visited[i][x] = True
    return visited


def dfs(maps):
    for i in range(len(maps)):
        if i == 0 or i == len(maps) - 1:
            continue
        for x in range(len(maps)):
            if x == 0 or x == len(maps) - 1:
                continue


while ite:
    n = int(sys.stdin.readline().strip())
    maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    visited = make_visited(maps)

    dfs(maps)
