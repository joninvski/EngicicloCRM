#import settings

from django.contrib.auth.models import User
#from django.contrib.sites.models import Site
#from django.contrib.flatpages.models import FlatPage

import os
import datetime
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from crm.models import Empresa

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
