import sys

sys.stdin = open('input.txt', 'r')

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def f(i, j):
    global N, maxV
    q = [0] * (N*N)
    f, r = -1, -1
    r += 1
    q[r] = (i, j)
    visited = [[0] * N for _ in range(N)]
    visited[i][j] = 1
    temp = [1]
    while f!= r:
        f+=1
        x, y = q[f]
        for a, b in dxy:
            nx, ny = x+a, y+b
            if 0<= nx < N and 0<= ny < N:
                if board[x][y] < board[nx][ny]:
                    if dp[nx][ny] != 0:
                        visited[nx][ny] = visited[x][y] + dp[nx][ny]
                    else:
                        r += 1
                        q[r] = (nx, ny)
                        visited[nx][ny] = max(visited[x][y] + 1, visited[nx][ny])
                    temp.append(visited[nx][ny])
    dp[i][j] = max(temp)
    if dp[i][j] > maxV:
        maxV = dp[i][j]

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
maxV = 0
for i in range(N):
    for j in range(N):
        f(i, j)
print(maxV)