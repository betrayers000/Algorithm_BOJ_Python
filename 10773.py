K = int(input())
nums = []
for _ in range(K):
    n = int(input())
    if n == 0:
        nums.pop()
    else:
        nums.append(n)
print(sum(nums))