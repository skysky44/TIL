
# 홀수/짝수

num = int(input('자연수를 입력하세요 > '))
if num <= 0:
    print('양의 정수를 입력하세요')
elif num % 2 == 0:
    print('짝수')
else:
    print('홀수')

num = int(input('양의 정수를 입력하세요 > '))
if num % 2 == 0:
    print('짝수')
else:
    print('홀수')
