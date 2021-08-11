
from rest_framework import serializers
from App_1.models import Players

class c_Serial(serializers.ModelSerializer):
    class Meta:
        model=Players
        fields=['id','name','sport']