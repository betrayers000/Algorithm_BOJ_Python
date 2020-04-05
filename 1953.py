import sys

sys.stdin = open('input.txt', 'r')

def f():
    global N
    group = [0] * (N+1)
    visit = [0] * (N+1)
    for i in range(1, N+1):
        if visit[i] == 0:
            visit[i] = 1
            for j in range(1, N+1):
                if table[i][j] == 0 and visit[j] == 0:
                    group[j] = 2
                    visit[j] = 1
    res = []
    for i in range(1, N+1):
        if group[i] == 2:
            res.append(i)
    return res



N = int(input())
table = [[1]*(N+1) for _ in range(N+1)]
for i in range(N):
    edge = list(map(int, input().split()))
    for j in range(len(edge)):
        if j != 0:
            table[i+1][edge[j]] = 0
            table[edge[j]][i+1] = 0
# for i in range(N+1):
#     print(table[i])
result = f()
print(len(result))
print(" ".join(map(str, sorted(result))))
print(N- len(result))
print(" ".join(map(str, sorted(set(list(range(1, N+1)))-set(result)))))
