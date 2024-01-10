def get_inner_function():
    def outer(a, b):
        def plus(c, d):
            return c + d
        r = plus(a, b)
        print(r)
    outer(1, 2)