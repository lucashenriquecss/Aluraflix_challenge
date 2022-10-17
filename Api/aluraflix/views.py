from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from aluraflix.serializers import VideosSerializer,CategoriasSerializer,VideoPorCategoriasSerializer
from aluraflix.models import Videos, Categorias



def handler404(request, exception):
    return render(request,'404.html')

class VideosViewSet(viewsets.ModelViewSet):
    """"Exibindo todos os videos"""
    queryset = Videos.objects.all()
    serializer_class = VideosSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['titulo']
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
  
    

class CategoriasViewSet(viewsets.ModelViewSet):
    """"Exibindo todos os categorias"""
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]



class VideosPorCategoriasViewSet(viewsets.ModelViewSet):
    """Filtrando videos por categorias"""
    def get_queryset(self):
        queryset =Videos.objects.filter(categoriaId_id=self.kwargs['pk'])
        return queryset
    serializer_class = VideoPorCategoriasSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


