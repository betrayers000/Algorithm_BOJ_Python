import sys
sys.stdin = open ('input.txt', 'r')

import heapq

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def f(x, y):
    global N
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < N and 0<= ny < N:
            dp[nx][ny] = min(dp[x][y] + board[nx][ny], dp[nx][ny])
            heapq.heappush(q, (dp[nx][ny], (nx, ny)))
cnt = 1
while 1:
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    if N == 0:
        break
    dp = [[99999999] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    q = []
    front = -1
    heapq.heappush(q, (0, (0, 0)))
    dp[0][0] = board[0][0]
    while q:
        x, y = heapq.heappop(q)[1]
        if visited[x][y] == 0:
            f(x, y)
        if x == N-1 and y == N-1:
            break
        visited[x][y] = 1
    print(f"Problem {cnt}: {dp[-1][-1]}")
    cnt += 1
