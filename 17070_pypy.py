import sys

sys.stdin = open('input.txt', 'r')

# 파이프 종류
# 2 : 두칸 가로 (도착점 바로 옆칸) 가로랑 대각선만 연결가능
# 3 : 두칸 세로 (도착점 바로 아래칸) 세로랑 대각선만 연결가능
# 4 : 네칸 대각선 (도착점 바로 대각선 밑) 전부 연결가능
# 1 : 파이프 연결이 안되는 칸 파이프가 없는 칸

def insert(i, j):
    for val in table[i][j]:
        if val == 2:
            if j+1 < N and board[i][j+1] != 1:
                table[i][j+1].append(2)
                board[i][j+1] = 5
            if i+1 < N and j +1 < N and board[i+1][j+1] != 1:
                if board[i+1][j] != 1 and board[i][j+1] != 1:
                    table[i+1][j+1].append(4)
                    board[i+1][j + 1] = 5
        if val == 3:
            if i+1 < N  and board[i+1][j] != 1:
                table[i+1][j].append(3)
                board[i+1][j] = 5
            if i + 1 < N and j + 1 < N and board[i+1][j+1] != 1:
                if board[i+1][j] != 1 and board[i][j+1] != 1:
                    table[i + 1][j + 1].append(4)
                    board[i+1][j + 1] = 5
        if val == 4:
            if j+1 < N and board[i][j+1] != 1:
                table[i][j+1].append(2)
                board[i][j + 1] = 5
            if i+1 < N and board[i+1][j] != 1:
                table[i+1][j].append(3)
                board[i+1][j] = 5
            if i + 1 < N and j + 1 < N and board[i+1][j+1] != 1:
                if board[i+1][j] != 1 and board[i][j+1] != 1:
                    table[i + 1][j + 1].append(4)
                    board[i+1][j + 1] = 5


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
board[0][0], board[0][1] = 1, 5
table = [[[] for _ in range(N)] for _ in range(N)]
table[0][0] = [2]
table[0][1] = [2]
for i in range(N):
    for j in range(N):
        if board[i][j] == 5:
            insert(i, j)
# for i in range(N):
#     print(table[i])
print(len(table[N-1][N-1]))