import sys

sys.stdin = open('input.txt')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dfs(sx, sy, n):
    s = [(sx, sy)]
    visited[sx][sy] = 1
    while s:
        x, y = s.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 and board[nx][ny] > n:
                    s.append((nx, ny))
                    visited[nx][ny] = 1


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
result = 1
n = 1
while 1:
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] > n and visited[i][j] == 0:
                dfs(i, j, n)
                cnt += 1
    n += 1
    if cnt == 0:
        break
    if result < cnt:
        result = cnt
print(result)
