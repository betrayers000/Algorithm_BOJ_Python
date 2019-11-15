import sys

sys.stdin = open('input.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

key = ['a', 'b', 'c', 'd', 'e', 'f']
door = ['A', 'B', 'C', 'D', 'E', 'F']

keys = {}
check = {
    'A': False,
    'B': False,
    'C': False,
    'D': False,
    'E': False,
    'F': False
}

def search(i, j, d):
    global N, M
    q = []
    q.append((i, j))
    visit = [[0] * M for _ in range(N)]
    visit[i][j] = d
    while q:
        x, y = q.pop(0)
        if board[x][y] == '1':
            return visit[x][y]
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == 0:
                fl = board[nx][ny]
                if fl in key:
                    keys[fl] = (nx, ny, visit[x][y] + 1)
                elif fl not in door and fl != "#":
                    q.append((nx, ny))
                    visit[nx][ny] = visit[x][y] + 1
    print(keys)


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
res = 0
si, sj = 0, 0
for i in range(N):
    for j in range(M):
        if board[i][j] == '0':
            si, sj = i, j
# search(si, sj, 1)
# print(keys)

