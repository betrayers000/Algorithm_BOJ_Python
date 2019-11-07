import sys
sys.stdin = open('input.txt', 'r')

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def moving(c, rc):
    global top, bottom, x, y, main, sub, N, M
    nx, ny = x + dx[c-1], y + dy[c-1]
    check = False
    if 0<= nx < N and 0<= ny < M:
        check = True
        # print(main, sub)
        if ((c == 1 or c ==2 ) and (rc == 3 or rc == 4)) or ((rc == 1 or rc == 2) and (c == 3 or c == 4)):
            bl = (bottom -1)%4
            br = (bottom +1)%4
            sub[1] = main[bottom]
            sub[3] = main[top]
            temp = main[:]
            temp[0] = main[bl]
            temp[2] = main[br]
            main = sub[:]
            sub = temp[:]
            top = 3
            bottom = 1
        # print(main, sub)
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
        else:
            main[bottom] = board[nx][ny]
            board[nx][ny] = 0
        x = nx
        y = ny
        # print(main, sub, top, bottom)
        # print(board)
        res.append(str(main[top]))
    return check

N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))
main = [0, 0, 0, 0]
sub = [0, 0, 0, 0]
top, bottom = 1, 3
# print(board)
temp = 0
res = []
for com in command:
    # print(com)
    if moving(com, temp):
        temp = com
print("\n".join(res))



