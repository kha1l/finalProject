from rest_framework import viewsets, mixins
from music.models import Song, Genre
from .serializers import SongSerializer, GenreSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class SongViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated]


class SongYourViewSet(viewsets.ViewSet):
    @staticmethod
    def list(request):
        queryset = Song.objects.filter(user=request.user.id)
        serializer = SongSerializer(queryset, many=True)
        return Response(serializer.data)


class GenreViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticated]
