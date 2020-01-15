import sys

sys.stdin = open('input.txt', 'r')


def f(n, k, s):
    global operator, result, N
    if n == k:
        result.append(s)
        return s
    else:
        for i in range(4):
            if operator[i] > 0:
                operator[i] -= 1
                if i == 0:
                    f(n + 1, k, s + nums[n])
                elif i == 1:
                    f(n + 1, k, s - nums[n])
                elif i == 2:
                    f(n + 1, k, s * nums[n])
                elif i == 3:
                    f(n + 1, k, int(s / nums[n]))
                operator[i] += 1


N = int(input())
nums = list(map(int, input().split()))
# +, -, *, %
operator = list(map(int, input().split()))
result = []
f(1, N, nums[0])
print(max(result))
print(min(result))
