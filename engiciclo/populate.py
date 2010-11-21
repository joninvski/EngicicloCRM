#import settings

from django.contrib.auth.models import User
#from django.contrib.sites.models import Site
#from django.contrib.flatpages.models import FlatPage

import os
import datetime
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from crm.models import Empresa, TipoServicoContratado, ServicoContratado, Pessoa, Transportadora, Contrato, Morada, Proposta, Recolha, ObservacaoEmpresa, Colaborador, TipoProposta
mport crm.models

os.system("python manage.py reset crm --noinput ")

############ ADMIN #############
try:
    u = User.objects.create(
        username='root',
        first_name='',
        last_name='',
        email='',
        is_superuser=True,
        is_staff=True,
        is_active=True,
    )
    u.set_password('toor')
    u.save()

except Exception as e:
    print str(e) + "Database user not saved"

################################

################################
#Moradas
################################
morada_a = Morada()
morada_a.rua_numero_andar = "Rua Carvalho n.3 11Esq"
morada_a.codigo_postal = "2800"
morada_a.cidade = "2902"
morada_a.pais = "Portugal"
morada_a.save()

morada_b = Morada()
morada_b.rua_numero_andar = "Rua Manel Jakim n.3 11Esq"
morada_b.codigo_postal = "2100"
morada_b.cidade = "2222"
morada_b.pais = "Portugal"
morada_b.save()

morada_c = Morada()
morada_c.rua_numero_andar = "Rua Pedro Esteve n.1 2Esq"
morada_c.codigo_postal = "2110"
morada_c.cidade = "2223"
morada_c.pais = "Portugal"
morada_c.save()


################################
#Empresas
################################

bosh = Empresa()
bosh.nome= "Bosh"
bosh.nif = 1234124
bosh.data_inicio = datetime.date(2005, 12, 12)
bosh.cliente = True
bosh.n_entrada = 32
bosh.n_facturacao = 32
bosh.comentario = 'Comentario'
bosh.save()

ferrari = Empresa()
ferrari.nome= "Ferrari"
ferrari.nif = 234412
ferrari.data_inicio = datetime.date(2009, 12, 12)
ferrari.cliente = False 
ferrari.n_entrada = 10101
ferrari.n_facturacao = 20203
ferrari.comentario = 'Comentario'
ferrari.save()

porsche = Empresa()
porsche.nome= "Porshe"
porsche.nif = 1231414
porsche.data_inicio = datetime.date(2009, 12, 12)
porsche.cliente = False 
porsche.n_entrada = 10101
porsche.n_facturacao = 20203
porsche.comentario = 'Comentario'
porsche.save()

talho_joao = Empresa()
talho_joao.nome= "Talho do senhor Joao"
talho_joao.nif = 123124
talho_joao.data_inicio = datetime.date(2001, 12, 12)
talho_joao.cliente = False
talho_joao.n_entrada = 13213
talho_joao.n_facturacao = 2213
talho_joao.comentario = 'Boa carne'
talho_joao.save()

talho_joao = Empresa()
talho_joao.nome= "Oficina do senhor Manel"
talho_joao.data_inicio = datetime.date(2000, 11, 01)
talho_joao.cliente = True
talho_joao.n_entrada = 131424
talho_joao.n_facturacao = 123123
talho_joao.comentario = 'Arranja carros'
talho_joao.save()

################################
#Empresa Morada
################################
empresa_morada_a = Morada()
empresa_morada_a.rua_numero_andar = "Rua Carvalho n.3 11Esq"
empresa_morada_a.codigo_postal = "2800"
empresa_morada_a.cidade = "Lisboa"
empresa_morada_a.pais = "Portugal"
empresa_morada_a.empresa = bosh
empresa_morada_a.save()

empresa_morada_b = Morada()
empresa_morada_b.rua_numero_andar = "Rua Manel Jakim n.3 11Esq"
empresa_morada_b.codigo_postal = "2100"
empresa_morada_b.cidade = "Lisboa"
empresa_morada_b.pais = "Portugal"
empresa_morada_b.empresa = talho_joao
empresa_morada_b.save()

empresa_morada_c = Morada()
empresa_morada_c.rua_numero_andar = "Rua Pedro Esteve n.1 2Esq"
empresa_morada_c.codigo_postal = "2110"
empresa_morada_c.cidade = "Lisboa"
empresa_morada_c.pais = "Portugal"
empresa_morada_c.empresa = talho_joao
empresa_morada_c.save()

################################
#Pessoas
################################
joao = Pessoa()
joao.nome = "Joao"
joao.data_nascimento = datetime.date(1984, 05, 02)
joao.empresa = talho_joao
joao.save()

guida = Pessoa()
guida.nome = "Guida"
guida.data_nascimento = datetime.date(1983, 03, 04)
guida.empresa = talho_joao
guida.save()

joaquim = Pessoa()
joaquim.nome = "Joaquim"
joaquim.data_nascimento = datetime.date(1981, 01, 01)
joaquim.empresa = ferrari
joaquim.save()

pedro = Pessoa()
pedro.nome = "Pedro"
pedro.data_nascimento = datetime.date(1980, 01, 01)
pedro.empresa = bosh
pedro.save()

afonso = Pessoa()
afonso.nome = "Afonso"
afonso.data_nascimento = datetime.date(1980, 01, 01)
afonso.empresa = bosh
afonso.save()

################################
#Tipo de servico contratado
################################
contrato_bosh = Contrato()
contrato_bosh.numero = 1
contrato_bosh.data_inicio = datetime.date(1980, 01, 01)
contrato_bosh.data_fim = datetime.date(1990, 01, 01)
contrato_bosh.empresa = bosh
contrato_bosh.save()
contrato_bosh.moradas.add(empresa_morada_a, empresa_morada_b)

contrato_talho = Contrato()
contrato_talho.numero = 2
contrato_talho.data_inicio = datetime.date(1980, 01, 01)
contrato_talho.data_fim = datetime.date(1990, 01, 01)
contrato_talho.empresa = bosh
contrato_talho.save()
contrato_talho.moradas.add(empresa_morada_c)

################################
#Tipo de servico contratado
################################
tipo_servico_sirapa = TipoServicoContratado()
tipo_servico_sirapa.tipo = "SIRAPA"
tipo_servico_sirapa.descricao = "Insercao de dados no sistema sirapa"
tipo_servico_sirapa.save()

tipo_servico_consultadoria = TipoServicoContratado()
tipo_servico_consultadoria.tipo = "Consultadoria"
tipo_servico_consultadoria.descricao = "Apoio e consultadoria a clientes"
tipo_servico_consultadoria.save()

tipo_servico_seguranca = TipoServicoContratado()
tipo_servico_seguranca.tipo = "Seguranca"
tipo_servico_seguranca.descricao = "Apoio e consultadoria em seguranca e higiene do trabalho"
tipo_servico_seguranca.save()

tipo_servico_residuos = TipoServicoContratado()
tipo_servico_residuos.tipo = "Residuos"
tipo_servico_residuos.descricao = "Apanha de residuos"
tipo_servico_residuos.save()

tipo_servico_outros = TipoServicoContratado()
tipo_servico_outros.tipo = "Outros"
tipo_servico_outros.descricao = "Tipos de Servico que nao se enquandrem nos restantes"
tipo_servico_outros.save()

################################
# Servicos
################################
servico_contratado_bosh = ServicoContratado()
servico_contratado_bosh.numero = 1
servico_contratado_bosh.valor_contratado = 123451
servico_contratado_bosh.tipo_servico_contratado = tipo_servico_seguranca
servico_contratado_bosh.contrato = contrato_bosh
servico_contratado_bosh.save()
servico_contratado_bosh.morada.add(morada_c)
servico_contratado_bosh.morada.add(morada_b)

servico_contratado_talho = ServicoContratado()
servico_contratado_talho.numero = 2
servico_contratado_talho.valor_contratado = 100
servico_contratado_talho.contrato = contrato_talho
servico_contratado_talho.tipo_servico_contratado = tipo_servico_residuos
servico_contratado_talho.save()
servico_contratado_talho.morada.add(morada_a)

#############################
#Transportadoras
#############################
dhl = Transportadora()
dhl.nome = "dhl"
dhl.save()

twa = Transportadora()
twa.nome = "twa"
twa.save()

zap = Transportadora()
zap.nome = "zap"
zap.save()

###########################
# Recolha
###########################
recolha_a = Recolha()
recolha_a.data_pedido_recolha =  datetime.date(2005, 12, 12)
recolha_a.recolha_efectuada = datetime.date(2010, 12, 12)
recolha_a.acompanhamento_tecnico = True
recolha_a.transportadora = zap
recolha_a.empresa = bosh
recolha_a.save()

recolha_b = Recolha()
recolha_b.data_pedido_recolha =  datetime.date(2005, 12, 10)
recolha_b.recolha_efectuada = datetime.date(2010, 12, 10)
recolha_b.acompanhamento_tecnico = False
recolha_b.transportadora = twa
recolha_b.empresa = ferrari
recolha_b.save()

recolha_c = Recolha()
recolha_c.data_pedido_recolha =  datetime.date(2005, 10, 4)
recolha_c.recolha_efectuada = datetime.date(2010, 12, 6)
recolha_c.acompanhamento_tecnico = True
recolha_c.transportadora = twa
recolha_c.empresa = talho_joao
recolha_c.save()

recolha_d = Recolha()
recolha_d.data_pedido_recolha =  datetime.date(2005, 10, 4)
recolha_d.recolha_efectuada = datetime.date(2010, 12, 6)
recolha_d.acompanhamento_tecnico = True
recolha_d.transportadora = twa
recolha_d.empresa = talho_joao
recolha_d.save()

##########################3
# Colaboradores
##########################3
joao = Colaborador()
joao.nome = "Joao Trindade"
joao.save()

guida = Colaborador()
guida.nome = "Ana Gomes"
guida.save()

tiago = Colaborador()
tiago.nome = "Tiago Santos"
tiago.save()

jakim = Colaborador()
jakim.nome = "Joaquim Esteves"
jakim.save()

peralta = Colaborador()
peralta.nome = "Peralta Esteves"
peralta.save()

####################################
# Tipo proposta 
####################################
prop_consultadoria = TipoProposta()
prop_consultadoria.tipo = "Consultadoria"
prop_consultadoria.save()

prop_equipamento = TipoProposta()
prop_equipamento.tipo = "Equipamento"
prop_equipamento.save()

prop_residuos = TipoProposta()
prop_residuos.tipo = "Residuos"
prop_residuos.save()

####################################
# Proposta
####################################
proposta_bosh = Proposta()
proposta_bosh.n_proposta = 1
proposta_bosh.n_facturacao = 1
proposta_bosh.n_campanha = 1
proposta_bosh.n_fontes = 1
proposta_bosh.n_trabalhadores = 33
proposta_bosh.data_abertura =  datetime.date(2005, 12, 11)
proposta_bosh.data_entrega =  datetime.date(2005, 12, 12)
proposta_bosh.empresa = bosh
proposta_bosh.contrato = contrato_bosh
proposta_bosh.decisao = 'I'
proposta_bosh.data_decisao = datetime.date(2005, 12, 12)
proposta_bosh.valor_proposta = 1000
proposta_bosh.tipo_proposta = prop_equipamento
proposta_bosh.save()
proposta_bosh.moradas.add(empresa_morada_a, empresa_morada_b)
proposta_bosh.responsavel.add(peralta)

proposta_talho = Proposta()
proposta_talho.n_proposta = 2
proposta_talho.n_facturacao = 1
proposta_talho.n_campanha = 1
proposta_talho.n_fontes = 2
proposta_talho.n_trabalhadores = 2
proposta_talho.data_abertura =  datetime.date(2001, 1, 10)
proposta_talho.data_entrega =  datetime.date(2001, 1, 13)
proposta_talho.empresa = talho_joao
proposta_talho.contrato = contrato_talho
proposta_talho.decisao = 'S'
proposta_talho.data_decisao = datetime.date(2005, 2, 7)
proposta_talho.valor_proposta = 2000
proposta_talho.tipo_proposta = prop_residuos
proposta_talho.save()
proposta_talho.responsavel.add(peralta)
proposta_talho.moradas.add(empresa_morada_c)

##########################3
# Observacao Empresa
##########################3
obs_a = ObservacaoEmpresa()
obs_a.texto = "Bom pagador"
obs_a.data_observacao = datetime.date(2010, 12, 6)
obs_a.empresa = bosh
obs_a.save()
obs_a.colaboradores.add(peralta)


obs_b = ObservacaoEmpresa()
obs_b.texto = "Afinal e mau pagador"
obs_b.data_observacao = datetime.date(2010, 12, 7)
obs_b.empresa = bosh
obs_b.save()
obs_b.colaboradores.add(peralta)

obs_c = ObservacaoEmpresa()
obs_c.texto = "Somente falando com eles"
obs_c.data_observacao = datetime.date(2009, 12, 7)
obs_c.empresa = ferrari
obs_c.save()
obs_c.colaboradores.add(tiago)

obs_d = ObservacaoEmpresa()
obs_d.texto = "Tem mto lixo"
obs_d.data_observacao = datetime.date(2009, 12, 5)
obs_d.empresa = talho_joao
obs_d.save()
obs_d.colaboradores.add(joao)

obs_e = ObservacaoEmpresa()
obs_e.texto = "Tem ainda mais lixo"
obs_e.data_observacao = datetime.date(2009, 12, 6)
obs_e.empresa = talho_joao
obs_e.save()
obs_e.colaboradores.add(joao)
