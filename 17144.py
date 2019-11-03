import sys

sys.stdin = open('input.txt', 'r')

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
idx_0 = [0, 1, 2, 3, 3]
idx_1 = [0, 3, 2, 1, 1]

def create_dirc(i, j, d):
    global R, C
    for k in range(4):
        while 1:
            ri, rj = i, j
            if d == 0:
                i = i + dx[idx_0[k]]
                j = j + dy[idx_0[k]]
                if 0 <= i < R and 0 <= j < C and board[i][j] != -1:
                    dirc[i][j] = idx_0[k]
                else:
                    i, j = ri, rj
                    dirc[i][j] = idx_0[k+1]
                    break
            else:
                i = i + dx[idx_1[k]]
                j = j + dy[idx_1[k]]
                if 0 <= i < R and 0 <= j < C and board[i][j] != -1:
                    dirc[i][j] = idx_1[k]
                else:
                    i, j = ri, rj
                    dirc[i][j] = idx_1[k+1]
                    break

def diffusion(x, y):
    global R, C
    temp = []
    n = board[x][y]
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0<= nx < R and 0<= ny < C and board[nx][ny] != -1:
            if temp_d.get((nx, ny)) != None:
                temp_d[(nx, ny)] += n//5
            else:
                temp_d[(nx, ny)] = n//5
            temp.append((nx, ny))
    board[x][y] = n - ((n//5)*len(temp))
    return temp

def cleaning():
    global R, C
    visited = [[0] * C for _ in range(R)]
    s = dust[:]
    temp = []
    while s:
        x, y = s.pop()
        n = dirc[x][y]
        if n != -1:
            nx, ny = x + dx[n], y + dy[n]
            if board[nx][ny] != -1:
                visited[nx][ny] = board[x][y]
        else:
            visited[x][y] = board[x][y]
    for i in range(R):
        for j in range(C):
            if board[i][j] != -1:
                board[i][j] = visited[i][j]
                temp.append((i, j))
    return temp

R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
purifier = []
dust = []
dirc = [[-1] * C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if board[i][j] == -1:
            purifier.append((i, j))
        elif board[i][j] != 0:
            dust.append((i, j))
for i in range(2):
    x, y = purifier[i]
    create_dirc(x, y, i)
time = 0
while time < T:
    temp = []
    temp_d = {}
    for i in range(len(dust)):
        x, y = dust[i]
        temp.extend(diffusion(x, y))
    for key in temp_d.keys():
        x, y = key
        val = temp_d[key]
        board[x][y] += val
    dust.extend(temp)
    dust = cleaning()
    time += 1

total = 0
for i in range(R):
    for j in range(C):
        if board[i][j] != -1:
            total += board[i][j]
print(total)