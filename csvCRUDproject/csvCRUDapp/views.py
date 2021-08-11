from django.shortcuts import render
from django.views.generic import ListView
from .models import  Student_data
# Create your views here.

class Student_list_view(ListView):
    model=Student_data
