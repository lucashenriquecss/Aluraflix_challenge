from rest_framework import serializers
from aluraflix.models import Videos

class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = ['titulo','categoria','descricao','data_lancamento','url']
