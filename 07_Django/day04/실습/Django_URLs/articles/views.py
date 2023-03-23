from django.shortcuts import render

# Create your views here.


def throw(request):
    return render(request, 'articles/throw.html')


def catch(request):
    data = request.GET.get('message')
    content = {
        'data': data,
    }
    return render(request, 'articles/catch.html', content)


def number_print_index(request):
    return render(request, 'articles/number_print_index.html')


def number_print(request, number):
    content = {
        'number': number
    }
    return render(request, 'articles/number_print.html', content)


def calculate_index(request):
    # a = 5
    # content = {
    #     'a': a
    # }
    return render(request, 'articles/calculate_index.html')


def calculate(request, number1, number2):
    content = {
        "plus": number1 + number2,
        "minus": number1 + number2,
        "multi": number1 * number2,
        "quotient": number1 // number2
    }
    return render(request, 'articles/calculate.html', content)
