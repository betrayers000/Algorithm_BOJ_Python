import sys
sys.stdin = open('input.txt', 'r')

def get_dis(a, b):
    sx, sy = a
    ex, ey = b
    return abs(sx-ex) + abs(sy - ey)

def f(n, k, m, z, s):
    global minV
    if n == m:
        res = check(s)
        if minV > res:
            minV = res
        return
    else:
        for i in range(z, k):
            if used[i] == 0:
                used[i] = 1
                f(n+1, k, m, i, s + [chik[i]])
                used[i] = 0

def check(temp):
    total = 0
    for i in range(len(home)):
        mv = 99999
        for j in range(len(temp)):
            dis = get_dis(home[i], temp[j])
            if mv > dis:
                mv = dis
        total += mv
    return total



N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
chik = []
home = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            chik.append((i, j))
        elif board[i][j] == 1:
            home.append((i, j))
# print(chik, home)
minV = N*N*N*N
used = [0] * len(chik)
f(0, len(chik), M, 0, [])
print(minV)
