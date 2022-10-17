
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from aluraflix.views import VideosViewSet, CategoriasViewSet,VideosPorCategoriasViewSet
from django.views.generic import TemplateView
schema_view = get_schema_view(
   openapi.Info(
      title="Documentação de Aluraflix",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="email@emai.com"),
      license=openapi.License(name="Lucas"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
router = routers.DefaultRouter()
router.register('videos', VideosViewSet, basename='videos')
router.register('categorias', CategoriasViewSet, basename='categorias')

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('control/', admin.site.urls),
    path('', include(router.urls)),
    path('categorias/<int:pk>/videos/', VideosPorCategoriasViewSet.as_view({'get': 'list'})),
    
]
handler404 = 'aluraflix.views.handler404'
