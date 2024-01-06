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