N, K = map(int, input().split())
nums = list(range(1, N + 1))
front, rear = -1, -1
res = []
while sum(nums) != 0:
    for i in range(K):
        rear = (rear + 1) % N
        if nums[rear] == 0:
            while 1:
                rear = (rear + 1) % N
                if nums[rear] != 0:
                    break
    # print(rear)
    res.append(str(nums[rear]))
    nums[rear] = 0
print(f"<{', '.join(res)}>")
