
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from aluraflix.views import VideosViewSet, CategoriasViewSet
router = routers.DefaultRouter()
router.register('videos', VideosViewSet, basename='videos')
router.register('categorias', CategoriasViewSet, basename='categorias')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    
]
