from rest_framework import serializers
from App_1.models import Candidate

class c_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Candidate
        fields=['id','name','score']