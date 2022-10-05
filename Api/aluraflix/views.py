from django.shortcuts import render
from rest_framework import viewsets, filters

from aluraflix.serializers import VideosSerializer,CategoriasSerializer,VideoPorCategoriasSerializer
from aluraflix.models import Videos, Categorias

class VideosViewSet(viewsets.ModelViewSet):
    """"Exibindo todos os videos"""
    queryset = Videos.objects.all()
    serializer_class = VideosSerializer

class CategoriasViewSet(viewsets.ModelViewSet):
    """"Exibindo todos os categorias"""
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer



class VideosPorCategoriasViewSet(viewsets.ModelViewSet):
    """Filtrando videos por categorias"""
    def get_queryset(self):
        queryset =Videos.objects.filter(categoriaId_id=self.kwargs['pk'])
        return queryset
    serializer_class = VideoPorCategoriasSerializer


