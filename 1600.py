import sys

sys.stdin = open('input.txt', 'r')

dm = [(0, 1), (0, -1), (1, 0), (-1, 0)]
dh = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (2, -1), (2, 1), (1, -2), (1, 2)]


def enque(x, y, k, d):
    global front, rear, q, H, W, K
    rear = (rear + 1) % (H * W * (K + 1))
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
    if k > 0:
        for z in range(8):
            nx, ny = x + dh[z][0], y + dh[z][1]
            if 0 <= nx < H and 0 <= ny < W and board[nx][ny] == 0:
                if dic.get((nx, ny, k + 1)) == None:
                    enque(nx, ny, k - 1, d + 1)
                    # q.append((nx, ny, k-1, d+1))
                    dic[(nx, ny, k - 1)] = d + 1
    return 0


K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]
# start = (0, 0) / end = (H-1, W-1)
dic = {}
q = [0] * (H * W * (K + 1))
front, rear = 0, 0
enque(0, 0, K, 0)
while front != rear:
    front = (front + 1) % (H * W * (K + 1))
    x, y, k, d = q[front]
    if x == H - 1 and y == W - 1:
        break
    f(x, y, k, d)
res = []
for i in range(K):
    ans = dic.get((H - 1, W - 1, i))
    if ans != None:
        res.append(ans)
print(min(res))
