from django.shortcuts import render
from django.http import HttpResponse
from receipts.models import Receipt,ReceiptItem,Employee

def hello(request):
    return render(request, 'hello.html')
