from rest_framework import serializers
from aluraflix.models import Videos,Categorias

class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = ['titulo','descricao','data_lancamento','url']
        # def validate_titulo(self,url):
        #     if  url.isalph():
        #         raise serializers.ValidationError({'url':"Por favor não insira numeros, insira urls de videos"})
        #     return url


class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'

    def validate_titulo(self,titulo):
        if  not titulo.isalph():
            raise serializers.ValidationError("Por favor não insira numeros ")
        return titulo