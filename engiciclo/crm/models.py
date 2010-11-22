from django.db import models

# Create your models here.

class Vendedor(models.Model):
    nome = models.CharField('Nome do Vendedor', max_length=120)

    def __unicode__(self):
        return unicode(self.nome)

class Morada(models.Model):
    rua = models.CharField('Rua numero e andar', max_length=200)
    localidade = models.CharField(max_length=40)
    codigo_postal = models.CharField(max_length=20)
    concelho = models.CharField(max_length=40)
    distrito = models.CharField(max_length=40)
    pais = models.CharField(max_length=20, default='Portugal')

    def __unicode__(self):
        return unicode(self.rua) + ', ' + unicode(self.localidade)

class CodigoLER(models.Model):
    numero = models.IntegerField()
    descricao = models.TextField('Descricao do codigo')
    comentatio = models.TextField('Comentario ao codigo', blank=True)
    perigoso = models.BooleanField('Residuo Perigoso', default=False)

    def __unicode__(self):
        return unicode(self.numero) + ': ' +  self.descricao

class Empresa(models.Model):
    nome = models.CharField('Nome da Empresa', max_length=200)
    nif = models.IntegerField(null='True')
    data_inicio = models.DateField('Data Inicio do cliente', null=True)
    cliente = models.BooleanField('Cliente Actual')

    n_entrada = models.IntegerField('Numero de Entrada', blank=True, null=True)
    n_facturacao = models.IntegerField('Numero de facturacao', null=True, blank=True)
    comentario = models.TextField('Comentario Geral', max_length=1000, blank=True)

    cliente_berner = models.CharField(max_length=50, blank=True)
    vendedores = models.ManyToManyField(Vendedor, null=True, blank=True)
    moradas = models.ManyToManyField(Morada)

    def __unicode__(self):
        return unicode(self.nome)

class TipoServicoContratado(models.Model):
    tipo = models.CharField('Tipo de Servico contratado', max_length=20)
    descricao = models.TextField('Descricao do tipo de Servico contratado', blank=True, max_length=200)

    def __unicode__(self):
        return unicode(self.tipo)

class Contrato(models.Model):
    numero = models.CharField('Numero do contrato', max_length=20)
    data_inicio = models.DateField('Data inicio do contrato', null=True)
    data_fim = models.DateField('Data fim do Contrato', null=True)
    data_rescisao = models.DateField('Data rescisao', null=True)
    empresa = models.ForeignKey('Empresa')
    moradas = models.ManyToManyField(Morada)

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
    data_nascimento = models.DateField('Data Nascimento', blank=True, null=True)
    telefone = models.CharField('Telefone', max_length=14)
    fax = models.CharField('Fax', max_length=14, blank=True)
    movel = models.CharField('Telemovel', max_length=14, blank=True)
    email = models.EmailField('Email', null=True, blank=True)
    contacto_principal = models.BooleanField('Contacto principal da empresa')

    def __unicode__(self):
        return unicode(self.nome)

class Transportadora(models.Model):
    nome = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.nome)


class Recolha(models.Model):
    data_pedido_recolha = models.DateTimeField('Data Recolha Planeada')
    recolha_efectuada = models.DateTimeField('Data Recolha Efectuada', blank=True)
    data_combinada_recolha = models.DateTimeField('Data planeada da recolha', blank=True)
    acompanhamento_tecnico = models.BooleanField('Teve acompanhamento tecnico')
    transportadora = models.ForeignKey(Transportadora)
    empresa = models.ForeignKey(Empresa)
    codigosLER = models.ManyToManyField(CodigoLER)
    moradas = models.ManyToManyField(Morada)

    def __unicode__(self):
        return unicode(self.data_pedido_recolha) + " " + unicode(self.empresa) + " " + unicode(self.transportadora)

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
    n_facturacao = models.IntegerField('Numero de Facturacao')
    n_campanha = models.IntegerField('Numero de Campanha', null=True)
    n_fontes = models. IntegerField('Numero de Fontes', null=True)
    n_trabalhadores = models.IntegerField('Numero de Trabalhadores', null=True)
    data_abertura = models.DateTimeField('Data Abertura da proposta')
    data_entrega = models.DateTimeField('Data Entrega da Proposta')
    empresa = models.ForeignKey('Empresa')
    contrato = models.ForeignKey('Contrato')
    moradas = models.ManyToManyField(Morada)
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

    pedido_de_consulta = models.ManyToManyField('Proposta')

    def __unicode__(self):
        return unicode(str(self.n_proposta) + ": " + str(self.empresa))

class ObservacaoEmpresa(models.Model):
    texto = models.TextField('Texto da Observacao',max_length=400)
    data_observacao = models.DateTimeField('Data da Observacao', null=True)
    empresa = models.ForeignKey(Empresa)
    colaboradores = models.ManyToManyField(Colaborador, null=True)

    def __unicode__(self):
        return unicode(self.texto) + ': '  + unicode(self.texto)

class Alerta(models.Model):
    data_introducao = models.DateTimeField('Data de introducao')
    data_alerta = models.DateTimeField('Data de aviso do alerta')
    responsavel_resolucao = models.ManyToManyField(Colaborador, null=True, blank=True, related_name='responsavel_solucao')
    colaborador = models.ManyToManyField(Colaborador)
    data_resolucao = models.DateTimeField('Data de resolucao')
    empresa = models.ForeignKey(Empresa)

    def __unicode__(self):
        return unicode(self.data_introducao) + " " + unicode(self.empresa)

class EstadoAlerta(models.Model):
    estado = models.CharField(max_length=25)
    alerta = models.ForeignKey(Alerta)

    def __unicode__(self):
        return unicode(self.estado)

class PedidoDeConsulta(models.Model):
    data_introducao = models.DateTimeField('Data de introducao')
    colaboradores = models.ManyToManyField(Colaborador)
    proposta = models.ForeignKey(Proposta, blank=True, null=True)
    empresa = models.ForeignKey(Empresa, blank=True, null=True)
    comentario = models.TextField('Pedido de consulta')

    def __unicode__(self):
        return unicode(self.data_introducao) + ' ' + unicode(self.colaboradores)

class Sirapa(models.Model):
    data_introducao = models.DateTimeField('Data de introducao')
    colaboradores = models.ManyToManyField(Colaborador)
    id_sirapa = models.CharField(max_length=32)
    senha = models.CharField(max_length=32)

    def __unicode__(self):
        return unicode(self.id_sirapa)
