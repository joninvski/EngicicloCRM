from django.db import models
import os

# Create your models here.


def get_image_path(instance, filename):
        return os.path.join('photos', str(instance.id), filename)

class Poster(models.Model):
    nome_centro = models.CharField('Nome do Centro', max_length=120)
    titulo = models.CharField('Titulo', max_length=120)
    financiamento = models.CharField('Financiamento', max_length=120)
    autores = models.TextField('Autores', blank=True)
    descricao = models.TextField('Descricao', blank=True)
    resumo = models.TextField('Resumo', blank=True)
    data = models.DateTimeField('Data de introducao')
    poster = models.ImageField('Imagem do poster', upload_to=get_image_path, blank=False)

    def __unicode__(self):
        return unicode(self.nome_centro)
