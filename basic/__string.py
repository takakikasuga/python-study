def get_string():
     s1 = "test"
     print(s1)
     print("I don't know")
     print('I don\'t know')
     print('Hello \nHow are you?')
     print(r'C:\name\name')
     print('##################')
     print("""\
     Line1
     Line2
     Line3\
     """)
     print('##################')
     print('Hi!' * 3 + 'Mike.')
     print('Py' + 'thon')
     print('Py''thon')
     s2 = ("aaaaaaaaaaaaaaaa""bbbbbbbbbbb")
     print(s2)
     s3 = "aaaaaaaaaaaaaaaa"\
          "bbbbbbbbbbb"
     print(s3)
     word = 'python'
     print(word[0])
     print(word[1])
     print(word[-1])
     print(word[0:2])
     print(word[:2])
     print(word[2:5])
     print(word[2:])
     word = "j" + word[1:]
     print(word)
     print(word[:])
     n = len(word)
     print(n)
     s = "My name is Mike. Hi Mike."
     print(s)
     print(s.startswith('My'))
     print(s.startswith('X'))
     print(s.find("Mike"))
     print(s.rfind("Mike"))
     print(s.count("Mike"))
     print(s.capitalize())
     print(s.title())
     print(s.upper())
     print(s.lower())
     print(s.replace("Mike", "Nancy"))
     print("a is {}".format("a"))
     print("a is {}".format("test"))
     print("a is {} {} {}".format(1,2,3))
     print("a is {0} {1} {2}".format(1,2,3))
     print("a is {2} {1} {0}".format(1,2,3))
     print("My name is {0} {1}.".format("Junya", "Hayashi"))
     print("My name is {name} {family}.".format(name="Junya", family="Hayashi"))
