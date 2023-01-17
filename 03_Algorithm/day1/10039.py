score_list = []
for _ in range(5):
    score = int(input())
    if score >= 40:
        score_list.append(score)
    else:
        score_list.append(40)


average = int(sum(score_list)/5)
print(average)
