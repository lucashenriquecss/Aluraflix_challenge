from django.db import models

# Create your models here.
CATEGORIA = (
        ("B","Backend"),
        ("F","Frontend"),
        ("C","Cloud"),
        ("D","Devops"),
    )
class Videos(models.Model):
    id = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=100,blank=False)
    categoria = models.CharField(max_length=1, blank=False,choices=CATEGORIA)
    descricao = models.CharField(max_length=200,blank=True)
    data_lancamento = models.DateField()
    url = models.URLField(max_length=200,blank=False)

    def __str__(self):
        return self.titulo