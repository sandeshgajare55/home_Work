from django.contrib import admin
from .models import book_Demo


class book_admin(admin.ModelAdmin):
     list_display = ['id','b_Name','b_Cost','b_Author'],
admin.site.register(book_Demo,book_admin)
