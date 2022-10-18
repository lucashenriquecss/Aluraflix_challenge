from django.test import TestCase
from aluraflix.models import Categorias,Videos


class CategoriasTestCase(TestCase):
    def setUp(self):
        Categorias.objects.create(
            nome='backend',
            cor='azul'
        )
    def test_create_categoria(self):
        categoria = Categorias.objects.get(nome='backend')
        self.assertEquals(categoria.__str__(), 'backend')


class VideosTestCase(TestCase):
    def setUp(self):
        Videos.objects.create(
            titulo='backend',
            categoriaId='backend',
            descricao='teste',
            data_lancamento='2022-05-22',
            url='https://www.youtube.com/watch?v=JIV6fcPN1tU'
        )
    def test_create_video(self):
        video = Videos.objects.get(titulo='backend')
        self.assertEquals(video.__str__(), 'backend')