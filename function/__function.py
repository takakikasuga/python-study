def get_function():
    def say_something():
        s = "hi"
        return s

    say_something()
    print(type(say_something))
    result = say_something()
    print(result)

    def what_is_this(color):
        if(color == "red"):
            return "tomato"
        elif(color == "green"):
            return "green pepper"
        else:
            return "I don't know"
    result = what_is_this("red")
    print(result)

    def add_num(a: int, b: int) -> int:
        return a + b
    r = add_num(10, 20)
    print(r)

    def menu(entree="beef", drink="wine", dessert="ice"):
        print("dessert = ", dessert)
        print("entree = ", entree)
        print("drink = ", drink)
    menu()
    menu(entree="beef", dessert="ice", drink="beer")
    def test_func(x, l=None):
        if l is None:
            l = []
        l.append(x)
        return l
    y = [1, 2, 3]
    r = test_func(100, y)
    print(r)
    y = [1, 2, 3]
    r = test_func(200, y)
    print(r)
    r = test_func(100)
    print(r)
    r = test_func(100)
    print(r)
    def say_something(word, *args):
        print("word = ", word)
        for arg in args:
            print(arg)
    say_something("Hi", "Mike", "Nance")
    t = ("Mike", "Nancy")
    say_something("Hi", *t)
    def menu(**kwargs):
        print(kwargs)
        for k, v in kwargs.items():
            print(k, ":", v)
    menu(entree="chicken", dessert="ice", drink="beer")
    d = {
        "entree": "beef",
        "drink": "ice",
        "dessert": "beer",
    }
    menu(**d)
    def menu(food, *args, **kwargs):
        print("food = ", food)
        print("args = ", args)
        print("kwargs = ", kwargs)
    menu("banana", "apple", "orange", entree="beef", drink="beer")
