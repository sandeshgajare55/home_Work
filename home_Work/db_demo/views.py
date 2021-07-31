from django.shortcuts import render
from django.http import HttpResponse
from db_demo.models import book_Demo
from db_demo.forms import  book_Form
from django import forms
def show_All(request):
    t=book_Demo.objects.all()
    bookdict={'val':t}
    return render(request,'show_ALl.html',bookdict)

def author_Show(request):
    t2 = book_Demo.objects.all()
    bookdict2 = {'val': t2}
    return render(request,'author_Show.html',bookdict2)

def user(request):
    form=forms.userRegistration()
    if request.method == 'POST':
        form = forms.userRegistration(request.POST)
        if form.is_valid():
            print('Form Valid')
            print('s_Name : ',form.cleaned_data['s_Name'])
            print('s_Marks : ', form.cleaned_data['s_Marks'])
    return render(request, 'xyz.html', {'form':form})


def form_demo(request):
    form = book_Form()
    if request.method == 'POST':
        form = book_Form(request.POST)
        if form.is_valid():
            form.save()
            print('b_Name : ', form.cleaned_data['b_Name'])
            print('b_Cost : ', form.cleaned_data['b_Cost'])
            print('b_Author : ', form.cleaned_data['b_Author'])
    pro={'form':form}
    return render(request,'pqr.html',pro)