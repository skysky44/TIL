# while문으로 풀기
# 양 끝 인덱스에서부터 가운데로 접근
word = 'level'
i = 0
while i <= len(word)-1-i:
    i += 1
    if word[i] == word[len(word)-1-i]:
        pass
    else:
        print(0)
        break
    if i == len(word)-1-i:
        print(1)
