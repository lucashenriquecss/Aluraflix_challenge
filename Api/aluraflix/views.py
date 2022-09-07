from django.shortcuts import render
from rest_framework import viewsets, filters
from aluraflix.serializers import VideosSerializer
from aluraflix.models import Videos

class VideosViewSet(viewsets.ModelViewSet):
    queryset = Videos.objects.all()

    serializer_class = VideosSerializer