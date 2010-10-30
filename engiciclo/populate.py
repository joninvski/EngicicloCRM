#import settings

from django.contrib.auth.models import User
#from django.contrib.sites.models import Site
#from django.contrib.flatpages.models import FlatPage

import os
import datetime
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from crm.models import Empresa, TipoServicoContratado, ServicoContratado

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
#Empresas
################################

bosh = Empresa()
bosh.nome= "Bosh"
bosh.data_inicio = datetime.date(2005, 12, 12)
bosh.cliente = True
bosh.n_entrada = 32
bosh.n_facturacao = 32
bosh.comentario = 'Comentario'
bosh.save()

ferrari = Empresa()
ferrari.nome= "Ferrari"
ferrari.data_inicio = datetime.date(2009, 12, 12)
ferrari.cliente = False 
ferrari.n_entrada = 10101
ferrari.n_facturacao = 20203
ferrari.comentario = 'Comentario'
ferrari.save()

porsche = Empresa()
porsche.nome= "Porshe"
porsche.data_inicio = datetime.date(2009, 12, 12)
porsche.cliente = False 
porsche.n_entrada = 10101
porsche.n_facturacao = 20203
porsche.comentario = 'Comentario'
porsche.save()

talho_joao = Empresa()
talho_joao.nome= "Talho do senhor Joao"
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
servico_contratado_bosh.empresa = bosh
servico_contratado_bosh.morada  = "Rua de baixo"
servico_contratado_bosh.valor_contratado = 123451
servico_contratado_bosh.tipo_servico_contratado = tipo_servico_seguranca
servico_contratado_bosh.save()

servico_contratado_talho = ServicoContratado()
servico_contratado_talho.empresa = talho_joao
servico_contratado_talho.morada  = "Bobadela"
servico_contratado_talho.valor_contratado = 100
servico_contratado_talho.tipo_servico_contratado = tipo_servico_residuos
servico_contratado_talho.save()
