import sys

sys.stdin = open('input.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def f(i, j):
    global N, L, R
    s = [(i, j)]
    temp_visit[i][j] = 1
    total = 0
    temp = []
    while s:
        x, y = s.pop()
        temp.append((x, y))
        total += country[x][y]
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and temp_visit[nx][ny] == 0:
                if L <= abs(country[x][y] - country[nx][ny]) <= R:
                    s.append((nx, ny))
                    temp_visit[nx][ny] = 1
    # print(temp)
    if len(temp) == 1:
        return False
    for t in temp:
        x, y = t
        print(country[x][y], total//len(temp))
        country[x][y] = total // len(temp)
    print(temp)
    return True
N, L, R = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(N)]
tn = 0
while tn < 5:
    temp = 0
    temp_visit = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if temp_visit[i][j] == 0:
                if f(i, j):
                    temp += 1
    # print(country)
    if temp == 0:
        break
    tn += 1
print(tn)