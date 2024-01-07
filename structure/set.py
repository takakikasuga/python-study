def get_set():
    a = {1, 2, 3, 4, 5, 1, 2}
    print(a)
    print(type(a))
    b = {2, 3, 3, 6, 7}
    print(b)
    print(type(b))
    print(a - b)
    print(b - a)
    print(a & b)
    print(a | b)
    print(a ^ b)
    s = {1, 2, 3, 4, 5}
    print(s)
    s.add(6)
    print(s)
    s.remove(6)
    print(s)
    s.clear()
    print(s)
    a = {}
    print(a)
    print(type(a))