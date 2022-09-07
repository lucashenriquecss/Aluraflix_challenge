from django.shortcuts import render
from rest_framework import viewsets, filters
from aluraflix.serializers import VideosSerializer,CategoriasSerializer
from aluraflix.models import Videos, Categorias

class VideosViewSet(viewsets.ModelViewSet):
    """"Exibindo todos os videos"""
    queryset = Videos.objects.all()
    serializer_class = VideosSerializer

class CategoriasViewSet(viewsets.ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer