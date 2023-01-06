import json
from pprint import pprint
with open('data/movie.json', 'r', encoding='utf8') as f:
    movie = json.load(f)
    pprint(movie)
    print(type(movie))
    print(movie['title'])

print('=======================================================')

with open('data/movies.json', 'r', encoding='utf8') as f:
    movie = json.load(f)
    # pprint(movie)
    print(type(movie))
    print(movie[0])
print(movie[0]['title'])  # adult의 value 출력:
print(movie[0].keys())  # 키들만 리스트로 출력
