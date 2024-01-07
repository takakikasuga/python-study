def get_dict():
    d = {"x": 10, "y": 20}
    print(d)
    print(type(d))
    print(d["x"])
    print(d["y"])
    d["x"] = 100
    print(d)
    d["z"] = 200
    print(d)
    d[1] = 10000
    print(d)
    print(dict(a=10, b=20))
    print(dict([("a", 10), ("b", 20)]))
    d = {"x": 10, "y": 20}
    print(d)
    print(d.keys())
    print(type(d.keys()))
    print(d.values())
    print(type(d.values()))
    d2 = {"x": 1000, "j": 500}
    d.update(d2)
    print(d)
    print(d2)
    print(d.get("x"))
    print(d.get("z"))
    print(type(d.get("z")))
    print(d.get("z", "alter value"))
    print(d.pop("x"))
    print(d)
    del d["y"]
    print(d)
    d = {"a": 100, "b": 200}
    print(d)
    d.clear()
    print(d)
    d = {"a": 100, "b": 200}
    print("a" in d)
    print("j" in d)


