from dataclasses import field
from rest_framework import serializers
from aluraflix.models import Videos,Categorias

class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = '__all__'
      


class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'


class VideoPorCategoriasSerializer(serializers.ModelSerializer):
    """Serializer para videos por categoria"""
    video_nome = serializers.ReadOnlyField(source='categoriaId.nome')
    class Meta:
        model = Videos
        exclude = ['categoriaId'] #menos o id fk irá aparecer