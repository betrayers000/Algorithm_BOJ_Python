import sys

sys.stdin = open('input.txt', 'r')

def find():
    global K, W, N
    q = [0] * (N+1)
    front, rear = -1, -1
    res = [0] *(N+1)
    for i in range(1, N+1):
        if ind[i] == 0:
            rear+= 1
            q[rear] = i
            res[i] = time[i-1]
    while front != rear:
        front += 1
        s = q[front]
        for i in range(len(table[s])):
            v = table[s][i]
            ind[v] -= 1
            res[v] = max(res[v], res[s] + time[v-1])
            if ind[v] == 0:
                rear += 1
                q[rear] = v
    return res

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    time = list(map(int, input().split()))
    table = []
    for _ in range(N+1):
        table += [[]].copy()
    ind = [0] * (N+1)
    for _ in range(K):
        s, e = map(int, input().split())
        table[s].append(e)
        ind[e] += 1
    W = int(input())
    ans = find()
    print(ans[W])
    # print(table)
    # print(ans)