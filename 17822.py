import sys

sys.stdin = open('input.txt', 'r')


def rotation(d, line, k):
    # d : 회전방향
    # line : 회전 시킬 리스트
    # k : 회전 칸
    # 리스트 인덱스를 이용해서 재배치 시키면서 회전
    global N, M
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
    # 탐색을 통해 값이 동일하면 이웃한 값을 0으로 변경해준다.
    # temp 에 시작값을 넣어주어서 바닥값이 변경되어도 체크 할수 있게 한다.
    global N, M
    cnt = 0
    for i in range(N):
        for j in range(M):
            temp = board[i][j]
            s = [(i, j)]
            if temp == 0:
                continue
            while s:
                x, y = s.pop()
                for k in range(4):
                    ni, nj = x + dx[k], y + dy[k]
                    # 회전 효과를 주기위해서 nj 범위를 아래와 같이 한다.
                    # 파이썬 특징상 -M 이면 0과 같기 때문
                    if 0 <= ni < N and -M <= nj <= M:
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
    # 변경된 값의 유무를 확인하여 True False를 반환한다.
    if cnt == 0:
        return False
    else:
        return True


def change():
    # 평균값을 구하고 값을 변경하는 함수
    # cnt 가 0일 경우 return 해준다. 해주지 않으면 런타임 오류가 발생
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
    if cnt == 0:
        return
    avg = total / cnt
    # print(avg)
    for val in temp:
        i, j = val
        if board[i][j] > avg:
            board[i][j] -= 1
        elif 0 < board[i][j] < avg:
            board[i][j] += 1


N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
command = [list(map(int, input().split())) for _ in range(T)]
for j in range(T):
    x, d, k = command[j]
    for i in range(1, N + 1):
        if i % x == 0:
            board[i - 1] = rotation(d, board[i - 1], k)
    visited = [[0] * M for _ in range(N)]
    ans = delete_line()
    # delete_line 함수의 결과를 체크하여 chage 함수 호출을 한다.
    if not ans:
        change()
    # print(board)
total = 0
for i in range(N):
    total += sum(board[i])
print(total)