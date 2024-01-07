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