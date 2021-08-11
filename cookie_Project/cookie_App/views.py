from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def set_cookie(request):
   response= render(request,'setcookie.html')
   response.set_cookie('name','Sandesh')
   return response

def set_cookie_2(request):
   res=render(request,'setcookie_2.html')
   res.set_cookie('name_2','Sarvesh')
   return res

def get_cookie(request):
   #name=request.COOKIES['name']
   name=request.COOKIES.get('name')
   #name = request.COOKIES.get('name',default)
   return render(request,'getcookie.html',{'name':name})

def get_cookie_2(request):
   name_2=request.COOKIES.get('name_2')
   return render(request,'getcookie_2.html',{'name_2':name_2})

# def del_cookie(request):
#    delete.COOKIES('name',path="")

@login_required()
def show(request):
   return render(request,'abc.html')