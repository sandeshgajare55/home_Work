from django.urls import path
from App1.views import BookListView

urlpatterns = [
    path('books/', BookListView.as_view()),
]