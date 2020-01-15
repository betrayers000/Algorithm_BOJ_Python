import sys

sys.stdin = open('input.txt', 'r')

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def dfs(sx, sy, n):
    global N
    cnt = 0
    s = [(sx, sy)]
    while s:
        x, y = s.pop()
        visited[x][y] = n
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = n
                    cnt += 1
                    s.append((nx, ny))
    dic[n] = cnt
    return



N = int(input())
board = [list(map(int, list(input()))) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dic = {}
n = 1
for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and visited[i][j] == 0:
            dfs(i, j, n)
            n += 1
print(len(dic))
for val in sorted(dic.values()):
    print(val)
