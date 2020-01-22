import sys

sys.stdin = open('input.txt', 'r')

def f(n):
    global students, total
    s = []
    history = []
    s.append(n)
    now = -1
    visited[n] = 1
    cnt = 1
    while s:
        m = s.pop()
        now = students[m]
        if visited[now] == 0:
            s.append(now)
            visited[now] = 1
            history.append(now)
            cnt += 1
    # print(n, now)
    if n == now:
        total += cnt
        return True
    for i in history:
        visited[i] = 0
    return False



T = int(input())
for tc in range(T):
    n = int(input())
    students = [0] + list(map(int, input().split()))
    # print(students)
    total = 0
    # table = [[]]
    # for _ in range(n):
    #     table += [[]].copy()
    # for i in range(n):
    #     table[i+1].append(students[i])
    # print(table)
    visited = [0] * (n + 1)
    for i in range(n):
        f(i+1)
    print(n-total)

