import sys

sys.stdin = open('input.txt', 'r')

from collections import deque

# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]


# 불을 먼저 지르고 그다음 탐색하는것 deque 사용하지 않을시
# python 에서는 시간초과 뜸
# def fire():
#     global W, H, sx, sy
#     # q = [0] * (W * H)
#     # f, r = -1, -1
#     q = deque()
#     for i in range(H):
#         for j in range(W):
#             if board[i][j] == "*":
#                 # r += 1
#                 # q[r] = (i, j)
#                 q.append((i, j))
#                 times[i][j] = 1
#             elif board[i][j] == "@":
#                 board[i][j] = "."
#                 sx = i
#                 sy = j
#     # while f != r:
#     while q:
#         # f += 1
#         # x, y = q[f]
#         x, y = q.popleft()
#         for k in range(4):
#             nx, ny = x + dx[k], y + dy[k]
#             if 0 <= nx < H and 0 <= ny < W and times[nx][ny] == 0:
#                 if board[nx][ny] == ".":
#                     times[nx][ny] = times[x][y] + 1
#                     # r += 1
#                     # q[r] = (nx, ny)
#                     q.append((nx, ny))
#
#
# def bfs():
#     global sx, sy, H, W
#     # q = [0] * (W * H)
#     # f, r = -1, -1
#     # r += 1
#     # q[r] = (sx, sy, 1)
#     q = deque()
#     q.append((sx, sy, 1))
#     while q:
#         # f += 1
#         # x, y, t = q[f]
#         x, y, t = q.popleft()
#         if x == H - 1 or x == 0 or y == W - 1 or y == 0:
#             return t
#         for k in range(4):
#             nx, ny = x + dx[k], y + dy[k]
#             if 0 <= nx < H and 0 <= ny < W and board[nx][ny] == ".":
#                 if t +1 < times[nx][ny] or times[nx][ny] == 0:
#                     # r += 1
#                     # q[r] = (nx, ny, t+1)
#                     q.append((nx, ny, t+1))
#                     times[nx][ny] = -1
#     return "IMPOSSIBLE"
#
# T = int(input())
# for tc in range(1, T + 1):
#     W, H = map(int, input().split())
#     board = [list(input()) for _ in range(H)]
#     times = [[0] * W for _ in range(H)]
#     sx, sy = 0, 0
#     # print(board)
#     fire()
#     # print(times)
#     print(bfs())

# 들어오는 순서로 불이 먼저 붙냐 사람이 먼저 오냐를 확인
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs():
    global H, W, sx, sy, visited
    q = [0] * (H * W)
    f, r = -1, -1
    temp = []
    visited = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if board[i][j] == "*":
                r += 1
                q[r] = (i, j, 1)
                visited[i][j] = 1
            elif board[i][j] == "@":
                temp = (i, j, 2)
                board[i][j] = "."
                visited[i][j] = 1
    r += 1
    q[r] = temp
    while f != r:
        f += 1
        x, y, k = q[f]
        if x == 0 or x == H - 1 or y == 0 or y == W - 1:
            if k == 2:
                return visited[x][y]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < H and 0 <= ny < W and visited[nx][ny] == 0:
                if board[nx][ny] == ".":
                    r += 1
                    q[r] = (nx, ny, k)
                    visited[nx][ny] = visited[x][y] + 1
    return "IMPOSSIBLE"


T = int(input())
for tc in range(1, T + 1):
    W, H = map(int, input().split())
    board = [list(input()) for _ in range(H)]
    times = [[0] * W for _ in range(H)]
    sx, sy = 0, 0
    print(bfs())
