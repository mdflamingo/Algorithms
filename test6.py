import collections


def is_valid(x, y, n, board):
    return 0 <= x < n and 0 <= y < n and board[x][y] != '#'


def solve(board, n):
    start_x, start_y = None, None
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'S':
                start_x, start_y = i, j
                break
        if start_x is not None:
            break
    queue = collections.deque([(start_x, start_y, 0, True)])
    visited = [[False] * n for _ in range(n)]
    while queue:
        x, y, steps, is_knight = queue.popleft()
        if board[x][y] == 'F':
            return steps
        for dx, dy in [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y, n, board) and not visited[new_x][new_y]:
                if board[new_x][new_y] == 'K' and is_knight:
                    queue.append((new_x, new_y, steps + 1, False))
                elif board[new_x][new_y] != 'G' or not is_knight:
                    queue.append((new_x, new_y, steps + 1, is_knight))
                visited[new_x][new_y] = True
                if board[new_x][new_y] == 'G':
                    is_knight = False
    return -1


n = int(input())

board = [list(input()) for _ in range(n)]

print(solve(board, n))
