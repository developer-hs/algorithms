from collections import deque


def solution(board):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    queue = deque()
    queue.append((0, 0, -1, 0))
    visited = {(0, 0, 0): 0, (0, 0, 1): 1, (0, 0, 2): 2, (0, 0, 3): 3}
    answer = float("inf")
    while queue:
        x, y, dire, cost = queue.popleft()
        for i in range(4):
            _x, _y = x + dx[i], y+dy[i]
            if 0 <= _x < len(board[0]) and 0 <= _y < len(board) and not board[_x][_y]:
                new_cost = cost
                if dire == -1:
                    new_cost += 100
                elif (dire - i) % 2 == 0:
                    new_cost += 100
                else:
                    new_cost += 600
                if _x == len(board) - 1 and _y == len(board) - 1:
                    answer = min(answer, new_cost)
                elif visited.get((_x, _y, i)) is None or visited.get((_x, _y, i)) > new_cost:
                    visited[(_x, _y, i)] = new_cost
                    queue.append((_x, _y, i, new_cost))
    return answer


print(solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [
      1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]))
