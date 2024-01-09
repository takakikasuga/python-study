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