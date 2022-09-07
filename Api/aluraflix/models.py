from django.db import models

# Create your models here.
class Videos(models.Model):
    CATEGORIA = (
        ("Backend","Backend"),
        ("Frontend","Frontend"),
        ("Cloud","Cloud"),
        ("Devops","Devops"),
    )
    id = models.IntegerField(_("Id"), primary_key=True)
    titulo = models.CharField(max_length=100,blank=False)
    categoria = models.CharField(max_length=200, blank=False,choices=CATEGORIA)
    descricao = models.CharField(max_length=200,blank=True)
    url = models.URLField(max_length=200,blank=False)

    def __str__(self):
        self.titulo