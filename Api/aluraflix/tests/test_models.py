from rest_framework.test import APITestCase
from aluraflix.models import Videos
from django.urls import reverse

"""Testando models Videos""" #perfoming test on videos


class VideoModelTestCase(APITestCase):
    #realizando teste de unidade
    def setup(self):
        self.video = Videos(
            titulo = 'Video backend',
            descricao = 'Video backend description',
            data_lancamento = '2002-08-05',
            url='https://www.youtube.com/watch?v=l9nh1l8ZIJQ'
        )

    def test_verifica_atributos_video(self):
        self.assertEqual(self.video.titulo, 'Video backend')
        self.assertEqual(self.video.descricao, 'Video backend  description')
        self.assertEqual(self.video.data_lancamento, '2002-08-05')
        self.assertEqual(self.video.url, 'https://www.youtube.com/watch?v=l9nh1l8ZIJQ')
