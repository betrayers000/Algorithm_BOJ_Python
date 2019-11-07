import sys

sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]
cnt = 0
for i in range(N-1, -1, -1):
    if K == 0:
        break
    n = K//coin[i]
    K = K - (coin[i] * n)
    cnt += n
print(cnt)