import sys

sys.stdin = open('input.txt', 'r')

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def get_dis(a, b):
    sx, sy = a
    ex, ey = b
    return abs(sx - ex) + abs(sy - ey)


def kill(temp, temp_board):
    global N, M
    cnt = 0
    for i in range(len(temp)):
        if temp[i] == None:
            continue
        x, y = temp[i]
        if temp_board[x][y] == 1:
            temp_board[x][y] = 0
            cnt += 1
    next_board = []
    total = 0
    for i in range(N + 1):
        if i == 0:
            next_board.append([0] * M)
        elif i == N:
            next_board.append([0] * M)
        else:
            next_board.append(temp_board[i - 1])
            total += sum(temp_board[i - 1])
    return next_board, total, cnt


def board_copy():
    global N, M
    temp = []
    for i in range(N + 1):
        temp.append(board[i].copy())
    return temp


def f(n, k, m, z, s):
    global maxV, board
    if n == m:
        kill_point = 0
        nb = board_copy()
        while 1:
            # print(nb, s)
            nb, check, cnt = kill(attack_list(s, nb), nb)
            # print(cnt, check)
            kill_point += cnt
            if check == 0:
                break
        if kill_point > maxV:
            maxV = kill_point
        return
    else:
        for i in range(z, k):
            if used[i] == 0:
                used[i] = 1
                f(n + 1, k, m, i, s + [(N, i)])
                used[i] = 0


def get_enemy(archer, temp_board):
    visited = [[0] * M for _ in range(N + 1)]
    xx, yy = archer
    visited[xx][yy] = 1
    q = []
    q.append((xx, yy))
    while q:
        x, y = q.pop(0)
        if temp_board[x][y] == 1:
            # print(xx, yy, visited[x][y])
            # print(visited)
            return x, y
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            # dis = get_dis(archer, (nx, ny))
            if 0 <= nx <= N and 0 <= ny < M and visited[nx][ny] == 0:
                # if temp_board[nx][ny] == 1:
                #     return nx, ny
                # else:
                if visited[x][y] <= D:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1


def attack_list(temp, temp_board):
    global M, N, D
    attack = []
    for i in range(len(temp)):
        attack.append(get_enemy(temp[i], temp_board))
    # print(attack, temp)
    # print(temp_board)
    return attack


N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
board.append([0] * M)
maxV = 0
used = [0] * M
f(0, M, 3, 0, [])
print(maxV)
