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