N = int(input())
nums = list(map(int, input().split()))
# 기본값을 -1을 준다.
res = ["-1"] * N
s = []
for i in range(N):
    n = nums[i]
    while s:
        # 스택이 빌때까지 돈다.
        # 지금 값이 스택 값보다 크다면
        # 해당인덱스에 지금값을 넣어주고
        # 해당 값을 빼준다
        if s[-1][0] < n:
            res[s[-1][1]] = str(n)
            s.pop()
        else:
            # 지금 값이
            # 더 작을경우에는 바로 break해준다
            # s.append((n, i))
            break
    # 다 비교후 현재값을 추가해준다.
    # 다음 값 비교를 위해서
    s.append((n, i))
# print(s)
print(" ".join(res))

