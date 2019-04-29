from api.music.models.models import Genres
from api.music.serializers.serializer import GenresSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def genres_request_base(request, format=None):
    if request.method == 'GET':
        snippets = Genres.objects.all()
        serializer = GenresSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GenresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'DELETE'])
def genres_request_full(request, pk, format=None):
    try:
        snippet = Genres.objects.get(pk=pk)
    except Genres.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GenresSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GenresSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)