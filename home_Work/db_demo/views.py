from django.shortcuts import render
from django.http import HttpResponse
from db_demo.models import book_Demo

def show_All(request):
    t=book_Demo.objects.all()
    bookdict={'val':t}
    return render(request,'show_ALl.html',bookdict)

#def author_Show(request):
 #   return render(request,'author_Show.html')

