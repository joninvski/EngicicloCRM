#!/usr/bin/python
# -*- coding: latin-1 -*-

from django.db import models
import os
import uuid

# Create your models here.
def get_image_path(instance, filename):
        return os.path.join('photos', str(uuid.uuid1()), filename)

class Poster(models.Model):
    nome_centro = models.CharField('Nome do Centro', max_length=150)
    titulo = models.CharField('Título', max_length=150)
    financiamento = models.CharField('Financiamento', max_length=150)
    autores = models.TextField('Autores')
    descricao_da_foto = models.TextField('Descrição da foto',)
    resumo = models.TextField('Resumo')
#    data = models.DateTimeField('Data de introducao')
    poster = models.ImageField('Imagem do poster', upload_to=get_image_path, blank=False)

    def __unicode__(self):
        return unicode(self.nome_centro)
