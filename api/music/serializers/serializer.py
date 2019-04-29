from rest_framework import serializers
from api.music.models.models import Songs, Genres

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        #fields = ['title', 'artist']
        fields = '__all__'

class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = '__all__'