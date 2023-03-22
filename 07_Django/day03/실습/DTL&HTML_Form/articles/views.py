from django.shortcuts import render
import random
# Create your views here.


def today_dinner(request):
    foods = ['치킨', '삼겹살', '짜장면']
    food = random.choice(foods)
    content = {
        'food': food,
    }
    return render(request, 'articles/today_dinner.html', content)


def throw(request):
    return render(request, 'articles/throw.html')


def catch(request):
    data = request.GET.get('message')
    content = {
        'data': data
    }
    return render(request, 'articles/catch.html', content)


def lotto_create(request):
    return render(request, 'articles/lotto_create.html')


def lotto(request):
    count = request.GET.get('count')
    lotto_all = [i for i in range(1, 46)]
    lotto_results = []
    for _ in range(int(count)):
        lotto_nums = random.sample(lotto_all, 6)
        lotto_results.append(lotto_nums)

    content = {
        'lotto_results': lotto_results,
    }
    return render(request, 'articles/lotto.html', content)
