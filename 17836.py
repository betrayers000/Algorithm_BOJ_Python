import sys

sys.stdin = open('input.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs():
    global N, M, T
    q = [0] * (N * M)
    front, rear = -1, -1
    rear += 1
    q[rear] = (0, 0)
    ex, ey = N - 1, M - 1
    visited[0][0] = 1
    ans = (N*M)+1
    while front != rear:
        front += 1
        x, y = q[front]
        if x == gram[0] and y == gram[1]:
            temp = abs(x-ex) + abs(y-ey)
            ans = visited[x][y] + temp
        if x == ex and y == ey:
            res = min(ans, visited[x][y])
            if res - 1 > T:
                return "Fail"
            return res - 1
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                if board[nx][ny] != 1:
                    rear += 1
                    q[rear] = (nx, ny)
                    visited[nx][ny] = visited[x][y] + 1
    if ans != (N*M)+1:
        if ans-1 <= T:
            return ans-1
    return "Fail"


N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
gram = 0
visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            gram = (i, j)
print(bfs())
# print(visited)
