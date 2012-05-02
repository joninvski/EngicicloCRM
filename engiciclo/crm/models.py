#!/usr/bin/python
# -*- coding: latin-1 -*-

from django.db import models
import os
import uuid

# Create your models here.
def get_image_path(instance, filename):
        return os.path.join('photos', str(uuid.uuid1()), filename)

class Poster(models.Model):
    nome_centro = models.CharField('Nome Oficial do Centro', max_length=150)
    titulo = models.CharField('Título', max_length=150)
    entidade_financiadora = models.CharField('Entidade Financiadora', max_length=150)
    centro_de_investigacao = models.CharField('Centro de Investigação', max_length=150)
    autores = models.TextField('Autores', max_length=1000)
    resumo = models.TextField('Resumo', max_length=2000)
#    data = models.DateTimeField('Data de introducao')
    poster = models.ImageField('Imagem', upload_to=get_image_path, blank=False)
    descricao_da_foto = models.TextField('Descrição da imagem', max_length=2000)

    def __unicode__(self):
        return unicode(self.nome_centro)
