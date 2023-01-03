dust = int(input('미세먼지 농도를 입력하세요 > '))
if 0 <= dust <= 30:
    print('좋음')
elif 30 < dust <= 80:
    print('보통')
elif 80 < dust <= 150:
    print('나쁨')
elif 151 < dust:
    print('매우나쁨')

# 위에서부터 순차적으로 가기 때문에

dust = int(input('미세먼지 농도를 입력하세요 > '))
if dust <= 30:
    print('좋음')
elif dust <= 80:
    print('보통')
elif dust <= 150:
    print('나쁨')
elif dust:
    print('매우나쁨')
