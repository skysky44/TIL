score = [list(map(int, input().split())) for _ in range(5)]
total_score = []
for i in score:
    total_score.append(sum(i))
result = max(total_score)
print(total_score.index(result)+1, result)
