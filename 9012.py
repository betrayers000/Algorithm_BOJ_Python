T = int(input())
for tc in range(T):
    ps = list(input())
    s = []
    for i in range(len(ps)):
        if ps[i] == "(":
            s.append("(")
        elif ps[i] == ")":
            if s != []:
                s.pop()
            else:
                s.append(")")
                break
    if s == []:
        print('YES')
    else:
        print('NO')