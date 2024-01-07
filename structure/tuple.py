def get_tuple():
    t = (1, 2, 3, 4, 5 ,1, 2)
    print(t)
    print(type(t))
    print(t[0])
    print(t[-1])
    print(t[2:5])
    print(t.index(1))
    print(t.index(1, 1))
    print(t.count(1))
    t = 1, 2, 3
    print(type(t))
    t = 1,
    print(t)
    print(type(t))
    t = ()
    print(t)
    print(type(t))
    t = (1)
    print(t)
    print(type(t))
    t = (1,)
    print(t)
    print(type(t))
    t = ("test")
    print(t)
    print(type(t))
    t = ("test",)
    print(t)
    print(type(t))
    new_tuple = (1, 2, 3, 4, 5) + (6, 7, 8, 9, 10)
    print(new_tuple)
    print(type(new_tuple))
    new_tuple = (1,) + (6, 7, 8, 9, 10)
    print(new_tuple)
    print(type(new_tuple))
    num_tuple = (10, 20)
    print(num_tuple)
    x, y = num_tuple
    print("x = ", x)
    print("y = ", y)
    min, max = 10, 100
    print("min = ", min)
    print("max = ", max)
    i = 10
    j = 20
    tmp = i
    i = j
    j = tmp
    print("i = ", i)
    print("j = ", j)
    a = 100
    b = 200
    print("a = ", a)
    print("b = ", b)
    a, b = b, a
    print("a = ", a)
    print("b = ", b)
