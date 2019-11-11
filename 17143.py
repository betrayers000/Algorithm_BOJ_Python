import sys
sys.stdin = open('input.txt', 'r')

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]
back = [0, 2, 1, 4, 3]

# 딕셔너리 이용한 풀이 pypy 통과하지만 python 시간초과
def moving(key, val):
    global R, C
    x, y = key
    s, d, z, = val[0]
    ox, oy = x, y
    for i in range(s):
        x , y = x + dx[d], y + dy[d]
        if 0<= x < R and 0<= y < C:
            continue
        else:
            d = back[d]
            for j in range(2):
                x, y = x + dx[d], y + dy[d]

    if temp.get((x, y)) == None:
        temp[(x, y)] = [(s, d, z)]
    else:
        temp[(x, y)].append((s, d, z))

def catch(t, shark):
    global R, res
    for i in range(R):
        if shark.get((i, t)) != None:
            res+= shark[(i, t)][0][2]
            del shark[(i, t)]
            return

R, C, M = map(int, input().split())
shark = {}
for _ in range(M):
    x, y, s, d, z = map(int, input().split())
    shark[(x-1, y-1)] = [(s, d, z)]
t = 0
res = 0
if shark != {}:
    while t < C:
        # print(shark)
        catch(t, shark)
        temp = {}
        for key, val in shark.items():
            moving(key, val)
        for key, val in temp.items():
            if len(val) > 1:
                val.sort(key=lambda x:x[2])
                temp[key] = [val.pop()]
        shark = temp
        t += 1
print(res)