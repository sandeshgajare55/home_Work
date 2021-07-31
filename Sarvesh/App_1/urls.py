from django.urls import path
from App_1 import views
urlpatterns=[
    path('Show/',views.show,name='show')
]