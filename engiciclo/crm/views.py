import pdb
# Create your views here.
from django.shortcuts import render_to_response

from django.http import HttpResponse
from crm.models import Empresa

def index(request):
    empresas_list = Empresa.objects.all().order_by('nome')
    return render_to_response('empresa/empresa_lista.html', {'empresas_list': empresas_list})

def detail(request, empresa_id):
    empresa = Empresa.objects.filter('id'=empresa_id)
    return render_to_response('empresa/empresa.html', {'empresa': empresa})
