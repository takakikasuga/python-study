def get_falsy():
    is_ok = True
    if is_ok:
        print("Boolean True hello")
    else:
        print("Boolean False hello")
    is_ok = ""
    if is_ok:
        print("String True hello")
    else:
        print("String False hello")
    is_ok = []
    if is_ok:
        print("Array True hello")
    else:
        print("Array False hello")
