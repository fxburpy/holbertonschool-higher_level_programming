def a(b, c):
    d = []
    for i in c:
        if i not in b:
            d.append(i)
    return d
