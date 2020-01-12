import sys

sys.stdin = open('input.txt', 'r')

N = int(input())
# 길이 N 만큼의 리스트를 만든다
table = [[]]
for _ in range(N):
    table += [[]].copy()

# 만들어 둔 리스트에 작업이 끝나는 시간을 기준으로 넣어준다.
for i in range(N):
    t, p = map(int, input().split())
    if i + t < N+1:
        table[i+t].append((t, p))
# print(table)
dp = [0] * (N+1)
for i in range(N+1):
    maxP = 0
    # 해당 일에 끝나는 일중에 가장 효율이 좋은 일을 선택한다.
    # 해당 일에 끝나는 일과 그일을 시작하기전에 저장된 값을 더해서 최대값을 구한다.
    if len(table[i]) > 0:
        for t, p in table[i]:
            maxp = dp[i-t] + p
            if maxp > maxP:
                maxP = maxp
    # 해당 일에 일을 하는 경우와 일을 하지않는 경우(dp[i-1]) 중 큰 값을 선택한다.
    dp[i] = max(dp[i-1], maxP)
print(max(dp))