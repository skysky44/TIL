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

    accountbook = AccountBook(note=note, description=description, category=category, amount=amount, date=date)
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


def select(request):
    category=request.GET.get('category')
    if category == '전체':
        accountbook_selects = AccountBook.objects.all()
        # account_self = '전체'
    else:
        accountbook_selects = AccountBook.objects.filter(category=request.GET.get('category'))
        # account_self = accountbook_selects[0].category
    context = {
        'accountbook_selects': accountbook_selects,
        # 'account_self': account_self,
        }

    return render(request, 'accountbooks/index2.html', context)

# def order1(request, account_category):
#     accountbook_selects = AccountBook.objects.filter(category=account_category).order_by('pk')
#     context = {
#         'accountbook_selects': accountbook_selects,
#     }
#     return render(request, 'accountbooks/index2.html', context)

# def order2(request, account_category):
#     accountbook_selects = AccountBook.objects.filter(category=account_category).order_by('amount')
#     context = {
#         'accountbook_selects': accountbook_selects,
#     }
#     return render(request, 'accountbooks/index2.html', context)

# def order3(request, account_category):
#     accountbook_selects = AccountBook.objects.filter(category=account_category).order_by('date')
#     context = {
#         'accountbook_selects': accountbook_selects,
#     }    
#     return render(request, 'accountbooks/index2.html', context)