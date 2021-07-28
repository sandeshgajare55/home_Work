from django.shortcuts import render
from django.http import HttpResponse
from db_demo.models import book_Demo

def show_All(request):
    t=book_Demo.objects.all()
    bookdict={'val':t}
    return render(request,'show_ALl.html',bookdict)

def author_Show(request):
    t2 = book_Demo.objects.all()
    bookdict2 = {'val': t2}
    return render(request,'Specific_Book.html',bookdict2)

