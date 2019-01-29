def powerFinder(x,y):
    i = range(x)
    j = range(y)
    for d in i:
        for c in j:
            a = d ** c
            print(a)
            b = c ** d
            print(b)
            e = d ** d
            f = c ** c
            for m in [a, b, e, f]:
                print(m)
