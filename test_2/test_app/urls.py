from django.urls import path
from .import views

urlpatterns=[
    path("Category1/",views.cat_1,name='Category 1'),
    path("Category2/",views.cat_2,name='Category 2'),
]