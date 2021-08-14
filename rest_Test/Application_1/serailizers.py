from Application_1.models import  Singer_demo,Song_demo,Writer
from rest_framework import serializers

class Singer_serializer(serializers.ModelSerializer):
    class Meta:Singer_demo
    fields=['id','name','gender','age','total']


class Song_serializer(serializers.ModelSerializer):
     songs=Singer_serializer(read_only=True,many=True)
     class Meta: Song_demo
     fields = ['id', 'song_lyrics', 'language', 'release_year', 'singers','writer']



class Writer_serializer(serializers.ModelSerializer):
    writers=Song_serializer(read_only=True,many=False)
    class Meta: Writer
    fields = ['name','language']