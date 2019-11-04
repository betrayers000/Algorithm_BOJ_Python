import sys

sys.stdin = open('input.txt')

dm = [(0, 1), (0, -1), (1, 0), (-1, 0)]
dh = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (2, -1), (2, 1), (1, -2), (1, 2)]


def enque(x, y, k, d):
    global front, rear, q, H, W, K, N
    rear = (rear + 1) % N
    q[rear] = (x, y, k, d)


def f(x, y, k, d):
    global H, W, K, kc
    for z in range(4):
        nx, ny = x + dm[z][0], y + dm[z][1]
        if 0 <= nx < H and 0 <= ny < W and board[nx][ny] == 0:
            if dic.get((nx, ny, k)) == None:
                enque(nx, ny, k, d + 1)
                # q.append((nx, ny, k, d+1))
                dic[(nx, ny, k)] = d + 1
                if nx == H - 1 and ny == W - 1:
                    return d + 1
    if k > 0:
        for z in range(8):
            nx, ny = x + dh[z][0], y + dh[z][1]
            if 0 <= nx < H and 0 <= ny < W and board[nx][ny] == 0:
                if dic.get((nx, ny, k - 1)) == None:
                    enque(nx, ny, k - 1, d + 1)
                    # q.append((nx, ny, k-1, d+1))
                    dic[(nx, ny, k - 1)] = d + 1
                    if nx == H - 1 and ny == W - 1:
                        return d + 1
    return -1


K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]
# start = (0, 0) / end = (H-1, W-1)
dic = {}
N = H * W * (K + 1)
q = [0] * N
front, rear = 0, 0
enque(0, 0, K, 0)
ans = -1
while front != rear:
    front = (front + 1) % N
    x, y, k, d = q[front]
    # if x == H - 1 and y == W - 1:
    #     break
    ans = f(x, y, k, d)
    if ans != -1:
        break
# res = []
# for i in range(K + 1):
#     ans = dic.get((H - 1, W - 1, i))
#     if ans != None:
#         res.append(ans)
# if res == []:
#     print(-1)
# else:
#     print(min(res))
print(ans)