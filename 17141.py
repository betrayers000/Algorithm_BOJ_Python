import sys

sys.stdin = open('input.txt', 'r')

def f(n, k, m,z, s):
    global minV
    if n == m:
        res = bfs(s)
        if res == 0:
            return
        if minV > res:
            minV = res
        return
    else:
        for i in range(z, k):
            if used[i] == 0:
                used[i] = 1
                f(n+1, k, m, i, s + [virus[i]])
                used[i] = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(temp):
    global N, wall
    visited = [[0] * N for _ in range(N)]
    q = [0] * (N*N)
    front, rear = -1, -1
    for t in temp:
        x, y = t
        rear += 1
        q[rear] = t
        visited[x][y] = 1
    while front != rear:
        front += 1
        x, y = q[front]
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
                if visited[nx][ny] == 0:
                    rear += 1
                    q[rear] = (nx, ny)
                    visited[nx][ny] = visited[x][y] + 1
    maxV = 0
    total = 0
    for i in range(N):
        mx = max(visited[i])
        c = visited[i].count(0)
        total += c
        if maxV < mx:
            maxV = mx
    if total - wall == 0:
        return maxV
    else:
        return 0

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
virus = []
minV = 3000
wall = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            virus.append((i, j))
            board[i][j] = 0
        elif board[i][j] == 1:
            wall += 1
used = [0] * len(virus)
f(0, len(virus), M,0, [])
if minV == 3000:
    minV = 0
print(minV-1)


