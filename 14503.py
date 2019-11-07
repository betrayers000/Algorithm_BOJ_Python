import sys
sys.stdin = open('input.txt', 'r')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

dirc = [3, 0, 1, 2]
back = [2, 3, 0, 1]

def search(x, y, d):
    global N, M, cnt
    n = d
    for i in range(4):
        n = dirc[n]
        nx, ny = x, y
        nx, ny = nx + dx[n], ny + dy[n]
        # print(x, y, n, nx, ny, board[nx][ny])
        if 0 <= nx < N and 0<= ny < M and board[nx][ny] != 1 and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            cnt += 1
            return nx, ny, n
    nx, ny = x + dx[back[n]], y + dy[back[n]]
    # print(nx, ny, n)
    if board[nx][ny] != 1:
        return nx, ny, n
    else:
        return




N, M = map(int, input().split())
sx, sy, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
cnt = 1
visited[sx][sy] = 1
while 1:
    ans = search(sx, sy, d)
    # print(ans)
    # for _ in range(N):
    #     print(visited[_])
    # print()
    # for _ in range(N):
    #     print(board[_])
    # print()
    if ans != None:
        sx, sy, d = ans
    else:
        break
print(cnt)