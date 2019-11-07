import sys

<<<<<<< HEAD
sys.stdin = open('input.txt', 'r')
=======
sys.stdin = open('input.txt')
>>>>>>> d95b6b32849b61917487119189d3135e2a64d100

dm = [(0, 1), (0, -1), (1, 0), (-1, 0)]
dh = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (2, -1), (2, 1), (1, -2), (1, 2)]


<<<<<<< HEAD
def enque(x, y, k, d):
    global front, rear, q, H, W, K
    rear = (rear + 1) % (H * W * (K + 1))
    q[rear] = (x, y, k, d)


def f(x, y, k, d):
=======
def enque(x, y, k):
    global front, rear, q, H, W, K, N
    rear = (rear + 1) % N
    q[rear] = (x, y, k)


def f(x, y, k):
>>>>>>> d95b6b32849b61917487119189d3135e2a64d100
    global H, W, K, kc
    for z in range(4):
        nx, ny = x + dm[z][0], y + dm[z][1]
        if 0 <= nx < H and 0 <= ny < W and board[nx][ny] == 0:
<<<<<<< HEAD
            if dic.get((nx, ny, k)) == None:
                enque(nx, ny, k, d + 1)
                # q.append((nx, ny, k, d+1))
                dic[(nx, ny, k)] = d + 1
=======
            if visited[nx][ny][k] == 0:
                enque(nx, ny, k)
                visited[nx][ny][k] = visited[x][y][k] + 1
>>>>>>> d95b6b32849b61917487119189d3135e2a64d100
    if k > 0:
        for z in range(8):
            nx, ny = x + dh[z][0], y + dh[z][1]
            if 0 <= nx < H and 0 <= ny < W and board[nx][ny] == 0:
<<<<<<< HEAD
                if dic.get((nx, ny, k + 1)) == None:
                    enque(nx, ny, k - 1, d + 1)
                    # q.append((nx, ny, k-1, d+1))
                    dic[(nx, ny, k - 1)] = d + 1
    return 0
=======
                if visited[nx][ny][k-1] == 0:
                    enque(nx, ny, k-1)
                    visited[nx][ny][k - 1] = visited[x][y][k] + 1

>>>>>>> d95b6b32849b61917487119189d3135e2a64d100


K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]
# start = (0, 0) / end = (H-1, W-1)
<<<<<<< HEAD
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
=======
visited = [[0] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        visited[i][j] = [0] * (K + 1)
N = H * W * (K + 1)
q = [0] * N
front, rear = 0, 0
enque(0, 0, K)
visited[0][0] = [1] * (K + 1)
while front != rear:
    front = (front + 1) % N
    x, y, k = q[front]
    f(x, y, k)

minV = 9999999
for i in visited[H - 1][W - 1]:
    if minV > i and i != 0:
        minV = i
if minV == 9999999:
    minV = 0
print(minV - 1)
>>>>>>> d95b6b32849b61917487119189d3135e2a64d100
