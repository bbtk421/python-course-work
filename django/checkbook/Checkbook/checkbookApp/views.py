from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'checkbookApp/index.html')

def create_account(request):
    return render(request, 'checkbookApp/CreateNewAccount.html')

def balance(request):
    return render(request, 'checkbookApp/BalanceSheet.html')

def transaction(request):
    return render(request, 'checkbookApp/AddTransaction.html')