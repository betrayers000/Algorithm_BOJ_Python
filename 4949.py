while True:
    word = list(input())
    if word == ['.']:
        break
    s = []
    for i in range(len(word)):
        if word[i] == "(":
            s.append(")")
        elif word[i] == ")":
            if s != []:
                if s.pop() != ")":
                    s.append(1)
                    break
            else:
                s.append(1)
                break
        elif word[i] == "[":
            s.append("]")
        elif word[i] == "]":
            if s != []:
                if s.pop() != "]":
                    s.append(1)
                    break
            else:
                s.append(1)
                break
    # print(word, s)
    if s == []:
        print('yes')
    else:
        print('no')
