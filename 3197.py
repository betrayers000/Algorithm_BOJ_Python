import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def melting():
    global R, C, maxT
    q = [0] *(R*C)
    front, rear = -1, -1
    for i in range(len(water)):
        rear += 1
        q[rear] = water[i]
    while front != rear:
        front += 1
        x, y = q[front]
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < R and 0 <= ny < C and board[nx][ny] == "X":
                if times[nx][ny] == 0:
                    rear += 1
                    q[rear] = (nx, ny)
                    times[nx][ny] = times[x][y] + 1
                    if times[nx][ny] > maxT:
                        maxT = times[nx][ny]
def f(n, k):
    if n == 0:
        return 1
    if find(n):
        if f(n//2, k) == 1:
            return 1
    else:
        if len(res) > 0:
            return 1
        if f(n + ((k-n)//2), k) == 1:
            return 1

def find(n):
    global R, C
    q = deque()
    visited = [[0] * C for _ in range(R)]
    # front, rear = -1, -1
    check = set()
    for s in swan:
        # rear += 1
        # q[rear] = s
        q.append(s)
    visited[swan[0][0]][swan[0][1]] = 1
    visited[swan[1][0]][swan[1][1]] = 2
    # while front != rear:
    while q:
        # front += 1
        # x, y = q[front]
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x +dx[k], y+dy[k]
            if 0 <= nx < R and 0 <= ny < C and times[nx][ny] <= n and times[nx][ny] != 0:
                if visited[nx][ny] != visited[x][y]:
                    r = len(check)
                    check.add((nx, ny))
                    if r == len(check):
                        res.append(n)
                        return True
                    visited[nx][ny] = visited[x][y]
                    # rear += 1
                    # q[rear] = (nx, ny)
                    q.append((nx, ny))
    return False



R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
water = []
times = [[0] * C for _ in range(R)]
swan = []
maxT = 0
res = []
for i in range(R):
    for j in range(C):
        if board[i][j] == ".":
            water.append((i, j))
            times[i][j] = 1
        elif board[i][j] == "L":
            swan.append((i, j))
melting()
f(maxT//2, maxT)
print(min(res) - 1)