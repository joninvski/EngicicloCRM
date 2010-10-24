# Create your views here.
from django.shortcuts import render_to_response

from django.http import HttpResponse
from crm.models import Empresa

def index(request):
    empresas_list = Empresa.objects.all().order_by('nome')
    return render_to_response('empresa/empresa_lista.html', {'empresas': empresas_list})

def detail(request, empresa_id):
    return HttpResponse("You're looking at poll %s." % empresa_id)
