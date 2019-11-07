import sys

sys.stdin = open('input.txt', 'r')

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
ng = [1, 2, 3, 2]


def curv(x, y, d, g):
    if g == 0:
        return 1
    nx, ny = x + dx[d], y + dy[d]
    if 0 <= x < 100 and 0 <= y < 100:
        res.append({(x, y), (nx, ny)})
        if curv(nx, ny, ng[d], g-1) == 1:
            return 1


N = int(input())
res = []
board = [[0] * 15 for _ in range(15)]
for _ in range(N):
    y, x, d, g = map(int, input().split())
    curv(x, y, d, 2 ** g)
print(res)
cnt = 0
for i in range(len(res)-3):
    for j in range(i+1, len(res)-2):
        for k in range(j+1, len(res)-1):
            for l in range(k+1, len(res)):
                if len(res[i] | res[j] | res[k] | res[l]) == 4:
                    print(res[i] | res[j] | res[k] | res[l])
                    cnt += 1
print(cnt)
