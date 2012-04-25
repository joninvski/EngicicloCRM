import pdb
# Create your views here.
from django.shortcuts import render_to_response

from django.http import HttpResponse
from crm.models import Poster

def index(request):
#    empresas_list = Empresa.objects.all().order_by('nome')
    return render_to_response('posters/poster.html', {'empresas_list': None})

def confirmacao(request):
#    empresas_list = Empresa.objects.all().order_by('nome')
    return render_to_response('posters/poster.html', {'empresas_list': None})

#def detail(request, empresa_id):
#    empresa = Empresa.objects.filter('id'=empresa_id)
#    return render_to_response('empresa/empresa.html', {'empresa': empresa})

#def recolhas_list(request):
#    recolha_list = Recolha.objects.all().order_by('data_pedido_recolha')
#    return render_to_response('empresa/recolha_list.html', {'recolha_list': recolha_list})

#def recolhas_single(request, empresa_id):
#    recolha = Recolha.objects.filter(id=empresa_id)[0]
#    return render_to_response('empresa/recolha.html', {'recolha': recolha, 'moradas': recolha.moradas})
