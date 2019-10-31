import sys
sys.stdin = open('input.txt', 'r')

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def moving(c, rc):
    global top, bottom, x, y
    nx, ny = x + dx[c-1], y + dy[c-1]
    if c == 1:
        #오른쪽
        top = (top + 1)%4
        bottom = (bottom + 1)%4
    elif c == 2:
        #왼쪽
        top = (top - 1) % 4
        bottom = (bottom - 1) % 4
    elif c == 3:
        #위쪽
        top = (top + 1) % 4
        bottom = (bottom + 1) % 4
    elif c == 4:
        #아래
        top = (top - 1) % 4
        bottom = (bottom - 1) % 4
    if board[nx][ny] == 0:
        board[nx][ny] = main[bottom]
    elif main[bottom] == 0:
        main[bottom] = board[nx][ny]
    x = nx
    y = ny

N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))
main = [0, 0, 0, 0]
sub = [0, 0]
top, bottom = 2, 0
print(board)
moving(4, 0)
print(main, top, bottom)




