T = int(input())
for _ in range(T):
    sentence = input().split()
    new_sentence = []
    for i in sentence:
        new_sentence.append(i[::-1])
    for j in new_sentence:
        print(j, end=" ")
