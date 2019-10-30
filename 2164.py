N = int(input())
cards = [0] * (N*2)
front, rear = -1, -1
for i in range(1, N+1):
    rear += 1
    cards[rear] = i
while rear != front:
    front += 2
    rear += 1
    cards[rear] = cards[front]
print(cards[rear-1])