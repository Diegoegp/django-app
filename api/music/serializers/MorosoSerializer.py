from rest_framework import serializers
from api.music.models.MorosoModel import User, Moroso

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = ['title', 'artist']
        fields = '__all__'

class MorosoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moroso
        fields = '__all__'