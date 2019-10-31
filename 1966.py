T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    q = [0] * (N * 2)
    f, r = -1, -1
    for i in range(N):
        r += 1
        q[r] = (i, nums[i])
        k = r
        while k > f:
            if q[k - 1][1] < q[k][1]:
                f += 1
                r += 1
                q[r] = q[f]
                q[f] = 0
                k -= 1
            else:
                break
        print(q, f, r)
