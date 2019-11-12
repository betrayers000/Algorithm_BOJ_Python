import sys
import time
start = time.time()
sys.stdin = open('input.txt', 'r')


dx = [0, 1, 0, -1, -1, 1, 1, -1]
dy = [1, 0, -1, 0, -1, -1, 1, 1]

def growth():
    for i in range(N*N):
        x, y = adx[i]
        y_list = info[i]
        temp_list = []
        total = 0
        # for k in range(len(y_list)-1, -1, -1):
        #     year = y_list[k]
        for year in sorted(y_list):
            if land[x][y] >= year:
                temp_list.append(year + 1)
                land[x][y] -= year
            else:
                total += year // 2
        info[i] = temp_list
        land[x][y] += total + food[x][y]

def breed():
    global N
    # print('breed')
    # print(info)
    for i in range(N*N):
        temp = info[i]
        x, y = adx[i]
        for z in temp:
            if z % 5 == 0:
                for k in range(8):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        n = idx[nx][ny]
                        info[n].append(1)

# def give():
#     global food
#     for i in range(N):
#         for j in range(N):
#             land[i][j] += food[i][j]

N, M, K = map(int, input().split())
food = [list(map(int, input().split())) for _ in range(N)]
idx = [[0]*N for _ in range(N)]
adx = [0] * (N*N)
n = 0
for i in range(N):
    for j in range(N):
        idx[i][j] = n
        adx[n] = [i, j]
        n += 1
info = []
for _ in range(N*N):
    info += [[]].copy()
land = [[5] * N for _ in range(N)]
for _ in range(M):
    x, y, z = (map(int, input().split()))
    info[idx[x-1][y-1]].append(z)

yer = 0
# print(info)
# print(wood)
while yer < K:
    # print(yer)
    # print(yer, info)
    # 자기 나이만큼 양분을 흡수하고 1살 먹는다/ 양분이 없으면 죽는다
    # 죽은 나무가 양분이 된다. 죽은 나무의 나이 //2
    # 나무가 여러개 있으면 가장 나이가 적은 나무가 양분을 흡수한다.
    growth()
    # 5의 배수일시에 주변으로 나이가 1인 나무가 생긴다.
    breed()
    # 땅에 양분이 추가 된다 양분은 info
    # give()
    yer += 1
# print(yer, info)
total = 0
# print(info)
for i in info:
    total += len(i)
print(total)
print(time.time()-start)