from django.urls import path
from session_App import views
urlpatterns=[
    path('',views.show)
]