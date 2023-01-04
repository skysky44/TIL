a = input()
print(a)  # '2 5'
# 원하는 것은 숫자 2와 숫자 5
# 1. 문자열을 가각 쪼갠 요소를 가진 리스트로 변환 _>.split
b = a.split()
print(b)  # ['2', '5']

# 2. 각 요소를 숫자로 변환
c = map(int, b)
print(c)  # map ~
print(list(c))  # [2, 5]

# 3. 각각 변수에 저장
d, e = list(c)
