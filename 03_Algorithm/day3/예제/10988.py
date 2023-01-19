word = input()
word_re = word[::-1]
if word == word_re:
    print(1)
else:
    print(0)
