drama = {'name': '더 글로리', 'writer': '김은숙'}
print(drama['name'])
print(drama.get('director'))  # None(키의 값이 없으면)

print(drama.get('dirctor', 0))  # None 일 때 0을 출력
