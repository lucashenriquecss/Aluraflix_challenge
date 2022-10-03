from django.db import models

# Create your models here.
class Categorias(models.Model):
    titulo = models.CharField(max_length=50,blank=False)
    cor =models.CharField(max_length=100,blank=False)
    def __str__(self):
        return self.titulo


class Videos(models.Model):
    titulo = models.CharField(max_length=100,blank=False)
    categoriaId = models.ForeignKey(Categorias,on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200,blank=True)
    data_lancamento = models.DateField()
    url = models.URLField(max_length=200,blank=False)

    def __str__(self):
        return self.titulo