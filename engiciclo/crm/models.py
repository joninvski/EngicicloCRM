from django.db import models

# Create your models here.

class Morada(models.Model):
    rua_numero_andar = models.CharField(max_length=200)
    codigo_postal = models.CharField(max_length=20)
    cidade = models.CharField(max_length=20)
    pais = models.CharField(max_length=20, default='Portugal')

    def __unicode__(self):
        return unicode(self.rua_numero_andar)

class EmpresaMorada(models.Model):
    rua_numero_andar = models.CharField(max_length=200)
    codigo_postal = models.CharField(max_length=20)
    cidade = models.CharField(max_length=20)
    pais = models.CharField(max_length=20, default='Portugal')
    empresa = models.ForeignKey('Empresa')

    def __unicode__(self):
        return unicode(self.rua_numero_andar)

class Empresa(models.Model):
    nome = models.CharField('Nome da Empresa', max_length=200)
    nif = models.IntegerField(null='True')
    data_inicio = models.DateField('Data Inicio do cliente', null=True)
    cliente = models.BooleanField('Cliente Actual')

    n_entrada = models.IntegerField('Numero de Entrada', null=True)
    n_facturacao = models.IntegerField('Numero de facturacao', null=True)
    comentario = models.CharField(max_length=1000)

    def __unicode__(self):
        return unicode(self.nome)

class TipoServicoContratado(models.Model):
    tipo = models.CharField('Tipo de Servico contratado', max_length=20)
    descricao = models.CharField('Descricao do tipo de Servico contratado', blank=True, max_length=200)

    def __unicode__(self):
        return unicode(self.tipo)

class Contrato(models.Model):
    numero = models.IntegerField('Numero do contrato')
    data_inicio = models.DateField('Data inicio do contrato', null=True)
    data_fim = models.DateField('Data fim do Contrato', null=True)
    empresa = models.ForeignKey('Empresa')
    moradas = models.ManyToManyField(EmpresaMorada)

    def __unicode__(self):
        return unicode(self.numero) + " " + unicode(self.empresa) + " " + unicode(self.data_inicio)

class ServicoContratado(models.Model):
    contrato = models.ForeignKey(Contrato)
    morada = models.ManyToManyField(Morada, null='True')
    valor_contratado = models.FloatField(max_length=200)
    tipo_servico_contratado = models.ForeignKey(TipoServicoContratado)

    def __unicode__(self):
        return unicode(self.tipo_servico_contratado)


class Pessoa(models.Model):
    empresa = models.ForeignKey(Empresa)
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField('Data Nascimento', null=True)
    telefone = models.IntegerField('Telefone', null=True)
    fax = models.IntegerField('Telefone', null=True)
    movel = models.IntegerField('Telemovel', null=True)
    email = models.EmailField('Email', null=True)
    contacto_principal = models.BooleanField('Contacto Principal')


    def __unicode__(self):
        return unicode(self.nome)

class Transportadora(models.Model):
    nome = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.nome)

class Recolha(models.Model):
    data_pedido_recolha = models.DateTimeField('Data Recolha Planeada')
    recolha_efectuada = models.DateTimeField('Data Recolha Efectuada', null=True)
    acompanhamento_tecnico = models.BooleanField('Teve acompanhamento tecnico')
    transportadora = models.ForeignKey(Transportadora)
    empresa = models.ForeignKey(Empresa)

    def __unicode__(self):
        return unicode(self.data_pedido_recolha)

class Colaborador(models.Model):
    nome =  models.CharField('Colaborador',max_length=140)

    def __unicode__(self):
        return unicode(self.nome)

class TipoProposta(models.Model):
    tipo = models.CharField('Tipo de proposta',max_length=20)

    def __unicode__(self):
        return unicode(self.tipo)

class Proposta(models.Model):
    n_proposta = models.IntegerField('Numero da Proposta')
    n_facturacao = models.IntegerField('Numero da Proposta')
    n_campanha = models.IntegerField('Numero de campanha', null=True)
    n_fontes = models. IntegerField('Numero de Fontes', null=True)
    n_trabalhadores = models.IntegerField('Numero de Trabalhadores', null=True)
    data_abertura = models.DateTimeField('Data Abertura da proposta')
    data_entrega = models.DateTimeField('Data Entrega da Proposta')
    empresa = models.ForeignKey('Empresa')
    contrato = models.ForeignKey('Contrato')
    moradas = models.ManyToManyField(EmpresaMorada)
    responsavel = models.ManyToManyField(Colaborador)
    DECISOES_POSIVEIS = (
        ('S', 'Sim'),
        ('N', 'Nao'),
        ('I', 'Indefinido'),
        ('A', 'Adiado'),
    )
    decisao = models.CharField('Decisao da proposta', max_length=1, choices=DECISOES_POSIVEIS)
    data_decisao = models.DateField('Data da decisao', null=True)

    valor_proposta = models.FloatField('Valor da proposta')

    tipo_proposta = models.ForeignKey(TipoProposta)

    def __unicode__(self):
        return unicode(str(self.n_proposta) + ": " + str(self.empresa))

class ObservacaoEmpresa(models.Model):
    texto = models.CharField('Texto da Observacao',max_length=400)
    data_observacao = models.DateTimeField('Data da Observacao', null=True)
    empresa = models.ForeignKey(Empresa)
    colaboradores = models.ManyToManyField(Colaborador, null=True)

    def __unicode__(self):
        return unicode(self.texto) + ': '  + unicode(self.texto)
