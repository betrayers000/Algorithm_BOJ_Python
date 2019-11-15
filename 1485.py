import sys

sys.stdin = open('input.txt', 'r')

def f(n, k, s):
    if n == k:
        if check_square(s):
            return 1
        return 0
    else:
        for i in range(k):
            if used[i] == 0:
                used[i] = 1
                if f(n+1, k, s +[i]) == 1:
                    return 1
                used[i] = 0
    return 0

def check_square(temp):
    line = 0
    for i in range(4):
        x1, y1 = point[temp[i]]
        if i == 3:
            x2, y2 = point[temp[0]]
        else:
            x2, y2 = point[temp[i+1]]
        res = abs(x1-x2) **2 + abs(y1-y2) ** 2
        if i > 0 and res != line:
            return False
        line = res
    line = 0
    for i in range(2):
        x1, y1 = point[temp[i]]
        x2, y2 = point[temp[i + 2]]
        res = abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2
        if i > 0 and res != line:
            return False
        line = res
    return True


T = int(input())
for t in range(1, T+1):
    point = []
    for _ in range(4):
        point.append(list(map(int, input().split())))
    used = [0] * 4
    print(f(0, 4, []))

