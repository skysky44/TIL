from django.shortcuts import render

# Create your views here.


def berners_lee(request):
    return render(request, 'berners_lee.html')
