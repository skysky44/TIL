from django.shortcuts import render, redirect
from .models import AccountBook
# Create your views here.


def index(request):
    accountbooks = AccountBook.objects.all()
    context = {
        'accountbooks': accountbooks,
    }
    return render(request, 'accountbooks/index.html', context)


def detail(request, account_book_pk):
    accountbook = AccountBook.objects.get(pk=account_book_pk)
    context = {
        'accountbook': accountbook
    }
    return render(request, 'accountbooks/detail.html', context)


def new(request):
    return render(request, 'accountbooks/new.html')


def create(request):
    note = request.POST.get('note')
    description = request.POST.get('description')
    category = request.POST.get('category')
    amount = request.POST.get('amount')
    date = request.POST.get('date')

    accountbook = AccountBook(
        note=note, description=description, category=category, amount=amount, date=date)
    accountbook.save()

    return redirect("accountbooks:detail", accountbook.pk)


def edit(request, account_book_pk):
    accountbook = AccountBook.objects.get(pk=account_book_pk)

    context = {
        'accountbook': accountbook
    }

    return render(request, 'accountbooks/edit.html', context)


def update(request, account_book_pk):
    accountbook = AccountBook.objects.get(pk=account_book_pk)

    accountbook.note = request.POST.get('note')
    accountbook.description = request.POST.get('description')
    accountbook.category = request.POST.get('category')
    accountbook.amount = request.POST.get('amount')
    accountbook.date = request.POST.get('date')

    accountbook.save()

    return redirect('accountbooks:detail', accountbook.pk)


def delete(request, account_book_pk):
    accountbook = AccountBook.objects.get(pk=account_book_pk)

    accountbook.delete()
    return redirect('accountbooks:index')


def copy(request, account_book_pk):
    accountbook = AccountBook.objects.get(pk=account_book_pk)
    new_accountbook = AccountBook()
    new_accountbook.note = accountbook.note
    new_accountbook.description = accountbook.description
    new_accountbook.category = accountbook.category
    new_accountbook.amount = accountbook.amount
    new_accountbook.date = accountbook.date
    new_accountbook.save()

    return redirect('accountbooks:index')


# 분류와 정렬을 한가지 함수 order로 해결 select 삭제


def order(request):
    ord = request.GET.get('order_by', '')
    category = request.GET.get('category', '')

    if category == ('전체' or ''):
        accountbooks = AccountBook.objects.all()
    else:
        accountbooks = AccountBook.objects.filter(category=category)
    if ord == '최신순':
        accountbooks = accountbooks.order_by('-date')
    elif ord == '사용금액순':
        accountbooks = accountbooks.order_by('-amount')
    else:
        pass

    context = {
        'accountbooks': accountbooks,
    }

    context = {
        'accountbooks': accountbooks,
    }

    return render(request, 'accountbooks/index.html', context)
