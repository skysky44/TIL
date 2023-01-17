n = int(input())
scorings = map(int, input().split())
score = 0
bonus = 0

for scoring in scorings:
    if scoring == 1:
        score += 1 + bonus
        bonus += 1
    else:
        bonus = 0

print(score)
