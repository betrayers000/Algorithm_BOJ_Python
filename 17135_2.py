import sys

sys.stdin = open('input.txt', 'r')

def get_dis(a, b):
    sx, sy = a
    ex, ey = b
    return abs(sx - ex) + abs(sy - ey)

def get_archer_position():
    global M
    result = []
    for i in range(M-2):
        for j in range(i+1, M-1):
            for k in range(j+1, M):
                result.append((i, j, k))
    return result

def get_enemy_position():
    global N, M
    result = {}
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
               result[i, j] = 1
    return result

def round(archers):
    global N, M
    result = []
    for p in archers:
        temp = {}
        for key in enemy.keys():
            d = get_dis(key, (N, p))
            if temp.get(d) == None:
                temp[d] = []
            temp[d].append(key)
        print(temp)


N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
archer_position = get_archer_position()
enemy = get_enemy_position()
for archers in archer_position:
    round(archers)



