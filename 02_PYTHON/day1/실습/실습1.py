# 정수형 숫자를 입력 받고, 10을 더해서 출력하세요.
print(int(input('정수형 숫자를 입력해주세요 > '))+10)

# 좋아하는 음식을 입력 받고, 출력하세요.
print('좋아하는 음식 : ' + input('좋아하는 음식을 입력해주세요 > '))

# 이름과 태어난 년도를 입력 받고, 출력하세요.(단, 태어난 년도를 나이로 변환해서 출력하세요.)
name = input('이름을 입력해주세요 > ')
year = int(input('태어난 년도를 입력해주세요 > '))
age = 2023 - year + 1
print('저의 이름은 ' + name + '이고, 올해 나이는 ' + str(age) + '세 입니다.')
# old를 string 으로 변환해야 함. 문자열 + 숫자 + 문자열 안 됨

# 개선
print('{}는 {}살입니다.'.format(name, age))
print(f'{name}는 {age}살입니다.')


# 문장 두 개를 입력 받고, 두 문장을 연결해서 출력하세요.
first_sentence = input('첫 번째 문장을 입력해주세요 > ')
second_sentence = input('두 번째 문장을 입력해주세요 > ')
print(first_sentence+second_sentence)

# 정수형 숫자 한 개를 입력 받고, 정수형 숫자의 부호를 바꿔서 출력하세요.
number = int(input('정수형 숫자를 입력해주세요 > '))
print(-number)

# 정수형 숫자 두 개를 입력 받고, 두 정수형 숫자에 대한 아래 산술 연산 결과를 출력하세요.
number1 = int(input('첫 번째 정수형 숫자를 입력해주세요 > '))
number2 = int(input('두 번째 정수형 숫자를 입력해주세요 > '))
plus = number1 + number2
minus = number1 - number2
multiply = number1 * number2
quotient = number1 // number2
remainder = number1 % number2
print('더하기 연산 : ' + str(plus))
print('빼기 연산 : ' + str(minus))
print('곱하기 연산 : ' + str(multiply))
print('몫 연산 : ' + str(quotient))
print('나머지 연산 : ' + str(remainder))

# 정수형 숫자 세 개를 입력 받고, 세 정수형 숫자의 평균을 출력하세요.
number1 = int(input('첫 번째 정수형 숫자를 입력해주세요 > '))
number2 = int(input('두 번째 정수형 숫자를 입력해주세요 > '))
number3 = int(input('세 번째 정수형 숫자를 입력해주세요 > '))
average = (number1 + number2 + number3)/3
print(int(average))

# 정수형 숫자 다섯 개를 입력 받고, 다섯 개의 정수형 숫자를 리스트 객체에 저장해서 출력하세요.
number1 = int(input('첫 번째 정수형 숫자를 입력해주세요 > '))
number2 = int(input('두 번째 정수형 숫자를 입력해주세요 > '))
number3 = int(input('세 번째 정수형 숫자를 입력해주세요 > '))
number4 = int(input('네 번째 정수형 숫자를 입력해주세요 > '))
number5 = int(input('다섯 번째 정수형 숫자를 입력해주세요 > '))
list = [number1, number2, number3, number4, number5]
print(list)

# 문자열 하나와 정수형 숫자 한 개를 입력 받고, 문자열을 정수형 숫자만큼 반복해서 출력하세요.
string = input('문자열을 입혁해주세요 > ')
number = int(input('정수형 숫자를 입력해주세요 > '))
print(string*number)

# 정수형 숫자 다섯 개를 입력 받고, 입력할 때 마다 입력한 정수형 숫자들의 합을 출력하세요.
number1 = int(input('첫 번째 정수형 숫자를 입력해주세요 > '))
print(number1)
number2 = int(input('두 번째 정수형 숫자를 입력해주세요 > '))
print(number1 + number2)
number3 = int(input('세 번째 정수형 숫자를 입력해주세요 > '))
print(number1 + number2 + number3)
number4 = int(input('네 번째 정수형 숫자를 입력해주세요 > '))
print(number1 + number2 + number3 + number4)
number5 = int(input('다섯 번째 정수형 숫자를 입력해주세요 > '))
print(number1 + number2 + number3 + number4 + number5)

# 개선
result = 0
result += int(input('첫 번째 정수형 숫자를 입력해주세요 > '))
print(result)
