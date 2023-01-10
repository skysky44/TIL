# # sum : Built-in scope
# print(sum([1, 2, 3]))

# # sum : Global scope
# sum = 1 + 2

# print(type(sum), sum)
# print(sum([1, 2, 3]))


a = 5


def boo():
    global a  # global scope의 a를 바꿔줌
    a = 3
    print(a)


boo()
