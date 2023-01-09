locations = ['서울', '서울', '대전', '부산', '대전']
result = {}
for location in locations:
    if location in result:
        result[location] += 1
    else:
        result[location] = 1
print(result)


result = {}
for location in locations:
    print(result.get(location, 0) + 1)
    result[location] = result.get(location, 0) + 1

    # .get 쓰는 방법도 있음. locatoin이 키에 속하면 키의 값을 주고
    #  가져올 키의 값이 없으면 0을 줌(0 안쓰면 defalt는 None)
print(result)
