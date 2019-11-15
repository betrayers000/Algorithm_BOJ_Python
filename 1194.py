import sys

sys.stdin = open('input.txt', 'r')

from collections import deque
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

keys = 'abcdef'
doors = 'ABCDEF'
def search(i, j):
    global N, M
    q = deque()
    q.append((i, j, ""))
    # q = [0] * (N*M*10)
    # front, rear = -1, -1
    # rear += 1
    # q[rear] = (i, j, "")
    visit[(i, j, "")] = 1
    # while front != rear:
    while q:
        r = q.popleft()
        # front += 1
        # r = q[front]
        x, y, key = r
        for k in range(4):
            temp = key
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != "#":
                fl = board[nx][ny]
                if visit.get((nx, ny, key)) == None:
                    if fl in doors and fl.lower() not in key:
                        continue
                    else:
                        if fl in keys and fl not in key:
                            temp += fl
                        visit[(nx, ny, temp)] = visit[r] + 1
                        if (nx, ny) in end_point:
                            return visit[r]
                        # rear += 1
                        # q[rear] = (nx, ny, temp)
                        q.append((nx, ny, temp))

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
res = 0
si, sj = 0, 0
visit = {}
end_point = []
for i in range(N):
    for j in range(M):
        if board[i][j] == '0':
            si, sj = i, j
        if board[i][j] == "1":
            end_point.append((i, j))
res = search(si, sj)
if res == None:
    print(-1)
else:
    print(res)

