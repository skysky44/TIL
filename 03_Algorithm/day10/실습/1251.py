
# # import sys
# # sys.stdin = open('input.txt')

word = list(input())
result = []
for i in range(1, len(word)-1):
    for j in range(i+1, len(word)):
        x, y, z = word[:i][::-1], word[i:j][::-1], word[j:][::-1]
        result.append(''.join(x+y+z))

print(sorted(result)[0])


# # 실패코드
# word = list(input())  # 알바벳 하나씩 리스트로
# ascii = list(map(ord, word))  # 아스키코드 번호로 바꾼다

# # 아스키코드가 빠르면 사전 앞에 나온다..?
# # 첫번째 자른 부분 인덱스
# cut1 = ascii.index(min(ascii[:-2]))
# # 두번째 자른 부분 인덱스
# cut2 = ascii.index(min(ascii[cut1+1:-1]))

# # 구한 인덱스로 word 잘라서 뒤집기


# new_word = word[0:cut1+1][::-1] + \
#     word[cut1+1:cut2+1][::-1]+word[cut2+1:len(word)]
# # 다시 단어로 출력하기
# for i in new_word:
#     print(i, end='')


# for i in range(0, cut1+1):
#     print(word[i])
# for i in range(cut1+1, cut2+1):
#     print(word[i])
# for i in range(cut2+1, len(word)):
#     print(word[i])
