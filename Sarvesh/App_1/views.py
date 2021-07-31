from django.shortcuts import render
from .models import Person
# Create your views here.

def show(request):
    t=Person.objects.all()
    b1={'val':t}
    return render(request,'show.html',b1)
