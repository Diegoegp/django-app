from api.music.models.MorosoModel import User, Moroso
from api.music.serializers.MorosoSerializer import MorosoSerializer
from rest_framework import generics

class moroso_request_base(generics.ListCreateAPIView):
    queryset = Moroso.objects.all()
    serializer_class = MorosoSerializer

class moroso_request_full(generics.RetrieveUpdateDestroyAPIView):
    queryset = Moroso.objects.all()
    serializer_class = MorosoSerializer
