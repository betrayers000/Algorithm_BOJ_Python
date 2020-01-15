import sys

sys.stdin = open('input.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def melting(N, M):
    visited = [[0] * M for _ in range(N)]
    s = [(0, 0)]
    visited[0][0] = 1
    cnt = 0
    while s:
        x, y = s.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0:
                    if board[nx][ny] == 0:
                        s.append((nx, ny))
                        visited[nx][ny] = 1
                    elif board[nx][ny] == 1:
                        board[nx][ny] = 0
                        visited[nx][ny] = 1
                        cnt += 1
    return cnt

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
res = 0
while 1:
    result = melting(N, M)
    if result == 0:
        break
    cnt += 1
    res = result
print(cnt)
print(res)
