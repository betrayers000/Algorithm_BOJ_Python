import sys

sys.stdin = open('input.txt', 'r')

dx = [(-1, -1, -1), (-1, -1, -1), (0, -1, -1), (0, 1, 1),
      (0, -1, -1), (0, 1, 1), (1, 1, 1), (1, 1, 1)]
dy = [(0, -1, -1), (0, 1, 1), (-1, -1, -1), (-1, -1, -1),
      (1, 1, 1), (1, 1, 1), (0, -1, -1), (0, 1, 1)]


def bfs(x, y):
    global kx, ky
    q = []
    q.append((x, y))
    visited[x][y] = 1
    while q:
        i, j = q.pop(0)
        for k in range(8):
            nx, ny = i, j
            for z in range(3):
                nx, ny = nx + dx[k][z], ny + dy[k][z]
                if nx == kx and ny == ky and z != 2:
                    break
            else:
                if 0 <= nx < 10 and 0<= ny < 9 and visited[nx][ny] == 0:
                    if nx == kx and ny == ky:
                        return visited[i][j]
                    visited[nx][ny] = visited[i][j] + 1
                    q.append((nx, ny))




# 10 * 9


sx, sy = map(int, input().split())
kx, ky = map(int, input().split())
visited = [[0] * 9 for _ in range(10)]
print(bfs(sx, sy))
