# 잘못된 풀이..
my_list = ['서울', '서울', '대전', '광주', '서울', '대전', '부산', '부산']
cnt = 0
for i in range(len(my_list)):
    for j in range(i+1, len(my_list)):
        if my_list[i] == my_list[j]:
            cnt += 1
print(cnt)

# 풀이
locations = ['서울', '서울', '대전', '광주', '서울', '대전', '부산', '부산']
result = []
for location in locations:
    if location not in result:
        result.append(location)

print(result)
print(len(result))
print(set(locations))
print(len(set(locations)))

# 순서대로 출력해야하면 set 말고 반복문 써야함. 순서가 다시 정렬 되기 때문
