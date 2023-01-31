import sys
sys.stdin = open('input.txt')
words = []
max_word = 0
for _ in range(5):
    word = list(input())
    words.append(word)
    if max_word < len(word):
        max_word = len(word)

for i in range(max_word):
    for j in range(5):
        try:
            words[j][i]
            print(words[j][i], end='')
        except:
            pass
