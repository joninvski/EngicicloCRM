from django.db import models

# Create your models here.
class Empresa(models.Model):
    nome = models.CharField('Nome da Empresa', max_length=200)
    data_inicio = models.DateField('Data Inicio do cliente')
    cliente = models.BooleanField('Cliente Actual')

    n_entrada = models.IntegerField('Numero de Entrada')
    n_facturacao = models.IntegerField('Numero de facturacao')
    comentario = models.CharField(max_length=1000)

    def __unicode__(self):
        return unicode(self.nome)

class ServicoContratado(models.Model):
    TIPOS_SERVICO = (
              ('SIR', 'SIRAPA'),
              ('CON', 'CONSULTADORIA'),
              ('SEG', 'SEGURANCA'),
              ('RES', 'RESIDUOS'),
              ('OUT', 'OUTROS'),
    )
    empresa = models.ForeignKey(Empresa)
    tipo_servico = models.CharField(max_length=3, choices=TIPOS_SERVICO)
    morada = models.CharField(max_length=200)
    valor_contratado = models.FloatField(max_length=200)

class Morada(models.Model):
    empresa = models.ForeignKey(Empresa)
    rua_numero_andar = models.CharField(max_length=200)
    codigo_postal = models.CharField(max_length=20)
    cidade = models.CharField(max_length=20)
    pais = models.CharField(max_length=20, default='Portugal')

    def __unicode__(self):
        return unicode(self.rua_numero_andar)

class Pessoa(models.Model):
    empresa = models.ForeignKey(Empresa)
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField('Data Nascimento')

    def __unicode__(self):
        return unicode(self.nome)

class Transportadora(models.Model):
    nome = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.nome)

class Recolha(models.Model):
    data_pedido_recolha = models.DateTimeField('Data Recolha Planeada')
    recolha_efectuada = models.DateTimeField('Data Recolha Efectuada')
    acompanhamento_tecnico = models.BooleanField('Teve acompanhamento tecnico')
    transportadora = models.ForeignKey(Transportadora)
    empresa = models.ForeignKey(Empresa)

    def __unicode__(self):
        return unicode(self.data_pedido_recolha)
