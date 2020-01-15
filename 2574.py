import sys

sys.stdin = open('input.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(sx, sy, N, M):
    s = [(sx, sy)]
    visited[sx][sy] = 1
    while s:
        x, y = s.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] != 0 and visited[nx][ny] == 0:
                    s.append((nx, ny))
                    visited[nx][ny] = 1
                elif board[nx][ny] == 0 and visited[nx][ny] == 0:
                    if board[x][y] > 0:
                        board[x][y] -= 1
        if board[x][y] == 0:
            ice_check[x][y] = 1

# def find():
#     check = 0
#     for i in range(N):
#         for j in range(M):
#             if board[i][j] != 0 and mel[i][j] == 0:
#                 dfs(i, j, N, M)
#                 check += 1
#             if check > 1:
#                 return check
#     return check

def find(ice, N, M):
    check = 0
    for i, j in ice:
        if visited[i][j] == 0 and ice_check[i][j] == 0:
            dfs(i, j, N, M)
            check += 1
            if check > 1:
                return check
    return check

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# ice 리스트를 만들어서 얼음 만넣어준다.
# ice_check 리스트를 만들어서 녹았는지 안녹았는지 체크해준다.
ice = []
ice_check = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j] != 0:
            ice.append((i, j))
# print(ice)
time = 0
while 1:
    visited = [[0] * M for _ in range(N)]
    result = find(ice, N, M)
    if result > 1 or result == 0:
        if result == 0:
            time = 0
        break
    time += 1
print(time)