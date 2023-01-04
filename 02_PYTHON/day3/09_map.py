# map
print(len)
print(type(len))

# 함수호출
# Input을 넣어서 함수를 실행시켰다.
print(len([1, 2, 3]))

# map 함수
# 첫번째 인자(Input)으로 함수를 받아서
# 두번째 인자(input)인 가능한 객체의 모든 요소에 적용!
numbers = ['1', '2', '3']
result = 0
for number in numbers:
    result += int(number)
print(result)


numbers = ['1', '2', '3']
new_number = []
for number in numbers:
    new_number.append(int(number))
print(new_number)

# 첫번째 인자(Input)으로 함수를 받아서
# 두번째 인자(input)인 반복가능한 객체의 모든 요소에 적용!
numbers = ['1', '2', '3']
new_new_numbers = map(int, numbers)
print(new_new_numbers)
print(list(new_new_numbers))
# map 프린트하면..<map object at 0x000001B3270DBA90> 나옴
# 보여지는 것은 이렇게 나오지만 .. 함수가 적용된 결과로 나옴
# range 처럼 머릿속에 그려봐야 됨.
