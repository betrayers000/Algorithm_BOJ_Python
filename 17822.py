import sys

sys.stdin = open('input.txt', 'r')


def cycle(d, line, k):
    global N, M
    temp = []
    if d == 0:
        for z in range(k):
            temp = []
            temp.append(line[-1])
            for i in range(len(line) - 1):
                temp.append(line[i])
            line = temp
    else:
        for z in range(k):
            temp = []
            for i in range(1, len(line)):
                temp.append(line[i])
            temp.append(line[0])
            line = temp
    return line


dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def delete_line():
    global N, M
    cnt = 0
    for i in range(N):
        for j in range(M):
            temp = board[i][j]
            s = [(i, j)]
            # print(temp)
            # print(board)
            if temp == 0:
                continue
            # 연속된 부분 전부 지워야 한다.
            # 지금 코드로는 연속된 부분을 못지움 두개만 지우고 끝난다
            # stack에 넣어서 계속 봐야 한다.
            while s:
                x, y = s.pop()
                for k in range(4):
                    ni, nj = x + dx[k], y + dy[k]
                    if 0 <= ni < N and -1 <= nj <= M:
                        if nj == M:
                            nj = 0
                        if visited[ni][nj] == 0:
                            if temp == board[ni][nj]:
                                board[x][y] = 0
                                board[ni][nj] = 0
                                visited[x][y] = 1
                                visited[ni][nj] = 1
                                cnt += 1
                                s.append((ni, nj))
    if cnt == 0:
        return False
    else:
        return True


def change():
    global N, M
    total = 0
    cnt = 0
    temp = []
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                total += board[i][j]
                cnt += 1
                temp.append((i, j))
    avg = total / cnt
    # print(avg)
    for val in temp:
        i, j = val
        if board[i][j] > avg:
            board[i][j] -= 1
        elif board[i][j] == avg:
            continue
        else:
            board[i][j] += 1


N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
command = [list(map(int, input().split())) for _ in range(T)]
# print(board)
for j in range(T):
    x, d, k = command[j]
    # print(x, d, k)
    # print(board)
    for i in range(1, N + 1):
        if i % x == 0:
            # print(i)
            board[i - 1] = cycle(d, board[i - 1], k)
    # print(board)
    visited = [[0] * M for _ in range(N)]
    ans = delete_line()
    # print(board)
    # print(ans)
    if not ans:
        change()
# print(board)
total = 0
for i in range(N):
    total += sum(board[i])

print(total)
