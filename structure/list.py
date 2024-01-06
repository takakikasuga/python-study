def get_list():
    l = [1, 20, 4, 50, 2, 1, 2]
    print(l)
    print(l[0])
    print(l[-1])
    print(l[-2])
    print(l[0:2])
    print(l[:2])
    print(l[2:5])
    print(l[2:])
    print(l[:])
    print(len(l))
    print(type(l))
    print(list("abcdefg"))
    n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(n[::2])
    print(n[::-1])
    a = ["a", "b", "c"]
    n = [1, 2, 3]
    x = [a, n]
    print(x)
    print(x[0])
    print(x[1])
    print(x[0][1])
    print(x[1][2])
    s = ["a", "b", "c", "d", "e", "f", "g"]
    print(s)
    s[0] = "X"
    print(s)
    s[2:5] = ["C", "D", "E"]
    print(s)
    s[2:5] = []
    print(s)
    s[:] = []
    print(s)
    n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n.append(100)
    print(n)
    n.insert(0, 200)
    print(n)
    print(n.pop())
    print(n)
    print(n.pop(0))
    print(n)
    print(n.pop(0))
    del n[0]
    print(n)
    n = [1, 2, 2, 2, 3]
    n.remove(2)
    print(n)
    n.remove(2)
    print(n)
    n.remove(2)
    print(n)
    a = [1, 2, 3, 4, 5]
    b = [6, 7, 8, 9, 10]
    a += b
    print(a)
    x = [1, 2, 3, 4, 5]
    y = [6, 7, 8, 9, 10]
    x.extend(y)
    print(x)
