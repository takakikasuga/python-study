def get_none():
    is_empty = None
    print("is_empty", is_empty)
    print("type(is_empty)", type(is_empty))
    # isはオブジェクトが同一かどうかを判定する
    if is_empty is None:
        print("None hello")
    if is_empty is not None:
        print("Not None hello")
    print("1 == True", 1 == True)
    print("1 is True", 1 is True)