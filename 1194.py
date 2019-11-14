import sys

sys.stdin = open('input.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

key = ['a', 'b', 'c', 'd', 'e', 'f']
door = ['A', 'B', 'C', 'D', 'E', 'F']


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
res = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == '0':
            print(i, j)
print(res)
