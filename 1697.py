import sys

sys.stdin = open('input.txt')

d = [-1, 1, 2]


def bfs():
    global N, K
    visited = [0] * 100001
    q = [0] * 100001
    f, r = -1, -1
    r += 1
    q[r] = N
    visited[N] = 1
    while f != r:
        f += 1
        n = q[f]
        for i in range(3):
            if i == 2:
                nx = n * d[i]
            else:
                nx = n + d[i]
            if 0 <= nx <= 100000 and visited[nx] == 0:
                # print(n, nx, visited[n])
                r += 1
                q[r] = nx
                visited[nx] = visited[n] + 1
                if nx == K:
                    return visited[nx] - 1


N, K = map(int, input().split())
print(bfs())
