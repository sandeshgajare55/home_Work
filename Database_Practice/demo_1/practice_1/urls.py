from django.urls import path
from .import views

urlpatterns=[
    path("All/",views.show,name='show')
]