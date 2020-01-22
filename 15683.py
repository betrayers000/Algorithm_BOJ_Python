import sys

sys.stdin = open('input.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def search(i, j):
    global N, M
    d = board[i][j]
    for k in range(4):
        x, y = i, j
        if d == 1:
            # 바라보고 있는방향
            while 1:
                x, y = x + dx[k], y+dy[k]
                if 0<= x < N and 0<= y < M and board[x][y] != 6:
                    if 0< board[x][y] < 6:
                        continue
                    maps[i][j][k].add((x, y))
                else:
                    break
        elif d == 2:
            # 바라보고있는 방향과 반대방향
            while 1:
                x, y = x+dx[k], y+dy[k]
                if 0<= x < N and 0<= y < M and board[x][y] != 6:
                    if 0< board[x][y] < 6:
                        continue
                    maps[i][j][k].add((x, y))
                else:
                    break
            # 반대방향
            z = (k+2) % 4
            while 1:
                x, y = x+dx[z], y+dy[z]
                if 0<= x < N and 0<= y < M and board[x][y] != 6:
                    if 0< board[x][y] < 6:
                        continue
                    maps[i][j][k].add((x, y))
                else:
                    break
        elif d == 3:
            # 직각방향/ 바라보는방향과 그옆방향
            while 1:
                x, y = x+dx[k], y+dy[k]
                if 0<= x < N and 0<= y < M and board[x][y] == 0:
                    if 0< board[x][y] < 6:
                        continue
                    maps[i][j][k].add((x, y))
                else:
                    break
            z = (k + 1)%4
            while 1:
                x, y = x+dx[z], y+dy[z]
                if 0<= x < N and 0<= y < M and board[x][y] != 6:
                    if 0< board[x][y] < 6:
                        continue
                    maps[i][j][k].add((x, y))
                else:
                    break
        elif d == 4:
            # 바라보는방향과 좌우 방향
            while 1:
                x, y = x+dx[k], y+dy[k]
                if 0<= x < N and 0<= y < M and board[x][y] != 6:
                    if 0< board[x][y] < 6:
                        continue
                    maps[i][j][k].add((x, y))
                else:
                    break
            z = (k + 1)%4
            while 1:
                x, y = x+dx[z], y+dy[z]
                if 0<= x < N and 0<= y < M and board[x][y] != 6:
                    if 0< board[x][y] < 6:
                        continue
                    maps[i][j][k].add((x, y))
                else:
                    break
            z = (k - 1) % 4
            while 1:
                x, y = x + dx[z], y + dy[z]
                if 0 <= x < N and 0 <= y < M and board[x][y] != 6:
                    maps[i][j][k].add((x, y))
                else:
                    break
        elif d == 5:
            # 전방향 방향에 상관없이
            for z in range(4):
                x, y = i, j
                while 1:
                    x, y = x + dx[z], y + dy[z]
                    if 0 <= x < N and 0 <= y < M and board[x][y] != 6:
                        if 0 < board[x][y] < 6:
                            continue
                        maps[i][j][k].add((x, y))
                    else:
                        break
            return


def f(n, k, s):
    global blank, maxV
    if n == k:
        # print(s, len(s))
        if maxV < len(s):
            maxV = len(s)
        return
    else:
        for i in range(k):
            x, y = cctv[i]
            if used[x][y] == 0:
                used[x][y] = 1
                for mp in maps[x][y]:
                    if mp != set():
                        f(n+1, k, s | mp)
                used[x][y] = 0



N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cctv = []
blank = 0
info = {}
maps = [[[set(),set(),set(),set()] for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if 0< board[i][j] < 6:
            cctv.append((i, j))
        elif board[i][j] == 0:
            blank += 1
for i in range(len(cctv)):
    x, y = cctv[i]
    search(x, y)
used = [[0] * M for _ in range(N)]
maxV = 0
f(0, len(cctv), set())
print(blank - maxV)