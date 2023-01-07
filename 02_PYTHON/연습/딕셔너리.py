# 파이썬 유치원반 위키독스
# 연습문제 2-4
# 031
temp = {}
# 032
ice = {'메로나': 1000, '폴라포': 1200, '빵빠레': 1800}
# 033
ice['죠스바'] = 1200
ice['월드콘'] = 1500

# 034
print(ice['메로나'])
print('메로나 가격: ', ice['메로나'])
# 035
ice['메로나'] = 1300
print('메로나 가격: ', ice['메로나'])

# 036
del ice['메로나']
# ice.pop('메로나')
print(ice)

# 037
price = {'메로나': 1000, '폴라포': 1200}
inven = {'메로나': 10, '폴라포': 3}

# 038
# 딕셔너리 정수형에는 '원'문자열을 바로 이어 붙이기 안됨
print('메로나', str(price['메로나'])+'원', '재고', str(inven['메로나'])+'개')
print('폴라포', str(price['폴라포'])+'원', '재고', str(inven['폴라포'])+'개')

# 040
# '누가바'라는 key가 없음

# 연습문제 2-5
# 041
ice = {
    '메로나': [300, 20],
    '비비빅': [400, 3],
    '죠스바': [250, 100]
}
# 042
print(ice['메로나'][0], '원')

# 043
print(ice['메로나'][1], '개')

# 044
ice['월드콘'] = [500, 7]

# 045
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(list(icecream.keys()))  # key 타입을 list로
# 046
print(list(icecream.values()))
# 047
# sum(icecream.values()) 하면 쉽게 됨
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
total = 0
for i in list(icecream.values()):
    total += i
print(total)

# 048 #icecream.update(new_product) 하면 쉽게 추가 가능
new_product = {'팥빙수': 2700, '아맛나': 1000}
for key in new_product:
    icecream[key] = new_product[key]
print(icecream)

# 049 # result = dict(zip(keys, vals)) 하면 쉽게 됨

keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = {}
for i in range(len(keys)):
    result[keys[i]] = vals[i]
print(result)

# 050
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

result2 = dict(zip(date, close_price))
print(result2)

# 추가 연습
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [{'10500': '원'}, {'10300': '달러'}, {
    '10100': '엔'}, {'10800': '유로'}, {'11000': '프랑'}]
result3 = dict(zip(date, close_price))
print(result3)
print(result3['09/06']['10300'])
