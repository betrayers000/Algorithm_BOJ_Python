import sys

sys.stdin = open('input.txt')

import heapq as h


def f(nw, n):
    for i in range(len(table[n])):
        v, w = table[n][i]
        if dp[v] > nw + w:
            dp[v] = nw+w
            h.heappush(q, (dp[v], v))

V, E = map(int, input().split())
K = int(input())
table = [[]]
for _ in range(V):
    table += [[]].copy()
for _ in range(E):
    s, e, w = map(int, input().split())
    table[s].append((e, w))
dp = [987654321] * (V + 1)
visit = [0] * (V + 1)
q = []
dp[K] = 0
h.heappush(q, (dp[K], K))
while q:
    w, n = h.heappop(q)
    if visit[n] == 0:
        f(w, n)
        visit[n] = 1
for i in range(1, len(dp)):
    if dp[i] == 987654321:
        print('INF')
    else:
        print(dp[i])
