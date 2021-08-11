from django.shortcuts import render
from .models import Person
from App_1.forms import person_Info
from App_1.models import Person
from  django import forms
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def show(request):
    t=Person.objects.all()
    b1={'val':t}
    return render(request,'show.html',b1)

@login_required
def person_show(request):
     form=person_Info()
     if request.method == 'POST':
         form = forms.person_Info(request.POST)
         if form.is_valid():
             form.save()
             print('p_name : ', form.cleaned_data['p_name'])
             print('p_sal : ', form.cleaned_data['p_sal'])
             print('p_gender: ',form.cleaned_data['p_gender'])
         return render(request,'abc.html',{'form':form})

# def form_views(request):
#     form=Warrior()
#     if request.method=='POST':
#         form=person_Info(request.POST)
#         if form.is_valid():
#             form.save()
#             print('p_name : ', form.cleaned_data['p_name'])
#             print('p_sal : ', form.cleaned_data['p_sal'])
#             print('p_gender: ', form.cleaned_data['p_gender'])
#         return render(request, 'abc.html', {'form': form})
