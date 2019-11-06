import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
time = [list(map(int, input().split())) for _ in range(N)]
time.sort(key=lambda x:x[1] - x[0])
used = [0] * 25
cnt = 0
for i in range(len(time)):
    s, e = time[i]
    for j in range(s, e+1):
        if used[j] == 0 or j == s or j == e+1:
            used[j] = 1
        else:
            break
    else:
        cnt += 1
print(cnt)