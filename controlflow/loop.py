def get_loop():
    count = 0
    while count < 5:
        print(count)
        count += 1
    count = 0
    while True:
        if count >= 5:
            break
        if count == 2:
            count += 1
            continue
        print(count)
        count += 1
    count = 0
    while count < 5:
       print(count)
       count += 1
    else:
        print("done")
    count = 0
    while count < 5:
        if count == 1:
            break
        print(count)
        count += 1
    else:
        print("done")
    # while True:
    #     word = input("Enter:")
    #     if word == "ok":
    #         break
    #     print("next")
    some_list = [1, 2, 3, 4, 5]
    # i = 0
    # while i < len(some_list):
    #     print(some_list[i])
    #     i += 1
    for i in some_list:
        print(i)
    for s in "abcde":
        print(s)

    for word in ["My", "name", "is", "Mike"]:
        if word == "name":
            continue
        if word == "Mike":
            break
        print(word)
    for fruit in ["apple", "banana", "orange"]:
        print(fruit)
    else:
        print("I ate all!")
    for fruit in ["apple", "banana", "orange"]:
        if fruit == "banana":
          print("stop eating")
          break
        print(fruit)
    else:
        print("I ate all!")
    num_list = [0, 1, 2, 3, 4, 5]
    for i in num_list:
        print(i)
    for i in range(10):
        print(i)
    for i in range(2, 10):
        print(i)
    for i in range(2, 10, 3):
        print(i)
    for _ in range(10):
        print("hello")
    for i, fruit in enumerate(["apple", "banana", "orange"]):
        print(i, fruit)