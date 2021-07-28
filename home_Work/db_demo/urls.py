from django.urls import path
from .import views

urlpatterns=[
    path("All/",views.show_All,name='show_ALl'),
   path("Author/",views.author_Show,name='show_Author')
]