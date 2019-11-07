import sys
sys.stdin = open('input.txt', 'r')

def set_pillar(i, j, k, d):
    x1, y1 = area[i]
    x2, y2 = area[j]
    x3, y3 = area[k]
    board[x1][y1] = d
    board[x2][y2] = d
    board[x3][y3] = d

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs():
    global N, M, safe
    visited = [[0] * M for _ in range(N)]
    q = [0] * (N * M)
    front, rear = -1, -1
    cnt = 0
    for ar in virus:
        x, y = ar
        rear += 1
        q[rear] = (x, y)
        visited[x][y] = 1
    while front != rear:
        front += 1
        x, y = q[front]
        for k in range(4):
            nx, ny = x+dxy[k][0], y+dxy[k][1]
            if 0<= nx < N and 0<= ny < M:
                if visited[nx][ny] == 0 and board[nx][ny] == 0:
                    rear += 1
                    q[rear] = (nx, ny)
                    visited[nx][ny] = 1
                    cnt += 1
                    if safe-cnt < maxV:
                        return 0
    return safe-cnt

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
virus = []
area = []
safe = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            virus.append((i, j))
        elif board[i][j] == 0:
            safe += 1
            area.append((i, j))
# print(safe, virus, area)
maxV = 0
for i in range(safe-2):
    for j in range(i+1, safe-1):
        for k in range(j+1, safe):
            set_pillar(i, j, k, 1)
            res = bfs()
            if maxV < res:
                maxV = res
            set_pillar(i, j, k, 0)
print(maxV-3)
