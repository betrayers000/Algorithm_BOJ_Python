import sys

sys.stdin = open('input.txt')

def dfs(start):
    stack = [start]
    result = []
    visited = [0] * (N + 1)
    while stack:
        n = stack.pop()
        if visited[n] == 0:
            result.append(str(n))
            stack.extend(sorted(table[n], reverse=True))
            visited[n] = 1
    return result

def bfs(start):
    q = [start]
    result = []
    visited = [0] * (N + 1)
    while q:
        n = q.pop(0)
        if visited[n] == 0:
            result.append(str(n))
            q.extend(sorted(table[n]))
            visited[n] = 1
    return result

N, M, V = map(int, input().split())
table = [[]]
for _ in range(N):
    table += [[]].copy()

for _ in range(M):
    s, e = map(int, input().split())
    table[s].append(e)
    table[e].append(s)

print(table)
print(" ".join(dfs(V)))
print(" ".join(bfs(V)))