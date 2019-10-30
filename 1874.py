N = int(input())
nums = list(range(1, N+1))
i_num = [int(input()) for _ in range(N)]
res = []
i = 0
s = []
for n in nums:
    s.append(n)
    res.append("+")
    # print("+")
    while s:
        if i_num[i] == s[-1]:
            s.pop()
            i += 1
            res.append("-")
            # print("-")
        else:
            break
if s == []:
    print("\n".join(res))
else:
    print('NO')