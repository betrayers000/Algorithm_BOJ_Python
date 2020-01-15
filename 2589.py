import sys

sys.stdin = open('input.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(sx, sy):
    q = [(sx, sy)]
    visited[sx][sy] = 1
    maxV = 0
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<= nx < L and 0 <= ny < W and board[nx][ny] == "L":
                if visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    if maxV < visited[nx][ny]:
                        maxV = visited[nx][ny]
    return maxV - 1

L, W = map(int, input().split())
board = [list(input()) for _ in range(L)]
result = 0
for i in range(L):
    for j in range(W):
        visited = [[0] * W for _ in range(L)]
        if board[i][j] == "L":
            res = bfs(i, j)
            if result < res:
                result = res
print(result)