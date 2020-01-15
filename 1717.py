import sys

sys.stdin = open('input.txt', 'r')

def find(n):
    if n == s[n]:
        return n
    else:
        return s[n]

n, m = map(int, input().split())
s = list(range(n+1))
for i in range(m):
    print(s)
    c, f, e = map(int, input().split())
    if c == 0:
        s[e] = find(f)
    elif c == 1:
        # print(f, find(e))
        if find(f) == find(e):
            print('YES')
        else:
            print('NO')
