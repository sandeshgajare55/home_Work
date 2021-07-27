from django.shortcuts import render
from django.http import HttpResponse

def show_All(request):
    return render(request,'show_ALl.html')

def author_Show(request):
    return render(request,'author_Show.html')

