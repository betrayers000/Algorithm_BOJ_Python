import sys

sys.stdin = open('input.txt', 'r')


def find(n):
    if par[n] == n:
        return n
    else:
        return find(par[n])

def same(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return True
    else:
        return False

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        par[y] = x


N, M = map(int, input().split())
label = list(input().split())
edge = []
for _ in range(M):
    s, e, w = map(int, input().split())
    if label[s - 1] != label[e - 1]:
        edge.append((s, e, w))
edge.sort(key=lambda x: x[2])
par = list(range(N + 1))
print(edge, par)
total = 0
for i in range(len(edge)):
    s, e, w = edge[i]
    if not same(s, e):
        total += w
        union(s, e)
        print(par)
print(total)
