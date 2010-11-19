from crm.models import Empresa, Pessoa, ServicoContratado, Transportadora
from crm.models import Recolha, Contrato, EmpresaMorada, Proposta, ObservacaoEmpresa
from crm.models import Colaborador, TipoProposta, TipoServicoContratado, Vendedor, CodigoLER
from crm.models import Alerta, EstadoAlerta, PedidoDeConsulta, TipoProposta, Sirapa
from django.contrib import admin
from django import forms
from django.forms import ModelMultipleChoiceField
from django.contrib.admin.widgets import AdminTextInputWidget
from django.db import models

import datetime

class ButtonableModelAdmin(admin.ModelAdmin):
    buttons=()

    def change_view(self, request, object_id, extra_context={}): 
        extra_context['buttons']=self.buttons 
        return super(ButtonableModelAdmin, self).change_view(request, object_id, extra_context)

    def button_view_dispatcher(self, request, object_id, command): 
        obj = self.model._default_manager.get(pk=object_id) 
        return getattr(self, command)(request, obj)  \
                or HttpResponseRedirect(request.META['HTTP_REFERER'])

    def get_urls(self):

        from django.conf.urls.defaults import patterns, url
        from django.utils.functional import update_wrapper

        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)
            return update_wrapper(wrapper, view)

        info = self.model._meta.app_label, self.model._meta.module_name

        return patterns('',
                        *(url(r'^(\d+)/(%s)/$' % but.func_name, wrap(self.button_view_dispatcher)) for but in self.buttons)
                       ) + super(ButtonableModelAdmin, self).get_urls()

class MyContratoAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MyContratoAdminForm, self).__init__(*args, **kwargs)
        if 'instance' in kwargs:
            contrato = kwargs['instance']
            self.fields['moradas'] = forms.ModelMultipleChoiceField(queryset=contrato.empresa.moradas, initial=kwargs['instance'].moradas,  widget=forms.CheckboxSelectMultiple())
        else:
            self.fields['moradas'] = forms.ModelMultipleChoiceField(queryset=EmpresaMorada.objects.all())

    class Meta:
        model = Contrato

class MyEmpresaAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MyEmpresaAdminForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Empresa
        fields = ('nome', 'n_entrada', 'n_facturacao', 'cliente', 'vendedores', 'data_inicio','comentario','cliente_berner', 'moradas')

class EmpresaMoradaInline(admin.TabularInline):
    model = EmpresaMorada

class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 2

class ComentarioInline(admin.TabularInline):
    model = Contrato
    extra = 1

class ContratoInline(admin.TabularInline):
    model = Contrato
    extra = 1
    exclude = ['moradas']

class RecolhaInline(admin.TabularInline):
    model = Recolha
    extra = 1

class ObservacaoEmpresaInline(admin.TabularInline):
    model = ObservacaoEmpresa
    extra = 1

class ColaboradorInline(admin.TabularInline):
    model = Colaborador
    extra = 3

class VendedorInline(admin.TabularInline):
    model = Vendedor

class EmpresaAdmin(admin.ModelAdmin):
    form = MyEmpresaAdminForm
    fieldsets = [ 
        (None,         {'fields': ['nome', 'n_entrada', 'n_facturacao', 'cliente', 'vendedores', 'moradas']}),
        ('Mais dados', {'fields': ['data_inicio','comentario','cliente_berner', ], 'classes': ['collapse']}),
    ]
    inlines = [ObservacaoEmpresaInline, ContratoInline, RecolhaInline, PessoaInline]
    list_display = ('n_entrada', 'nome','nif','data_inicio')
    list_per_page = 300
    search_fields = ['nome','nif']
    date_hierarchy = 'data_inicio'
    save_on_top = True
    filter_horizontal = ('moradas',)

class ContratoAdmin(admin.ModelAdmin):
    form = MyContratoAdminForm
    fieldsets = [
        (None,         {'fields': ['numero', 'data_inicio', 'data_fim', 'empresa', 'moradas']}),
    ]
    list_display = ('numero','data_inicio', 'data_fim', 'empresa')
    list_filter = ('empresa', )


class ObservacaoEmpresaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,         {'fields': ['texto']}),
    ]
    inlines = [ColaboradorInline]
    list_display = ('texto','data_observacao', 'empresa')
    list_filter = ('data_observacao', 'empresa')

class PessoaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Dados Base',         {'fields': ['nome', 'empresa', 'data_nascimento', 'email', 'fax','movel', 'contacto_principal']}),
    ]
    list_filter = ('empresa',)

class RecolhaAdmin(ButtonableModelAdmin):
    fieldsets = [
        (None,         {'fields': ['data_pedido_recolha', 'codigosLER', 'recolha_efectuada', 'acompanhamento_tecnico', 'transportadora', 'empresa', 'moradas']}),
    ]
    list_filter = ('data_pedido_recolha', 'recolha_efectuada', 'acompanhamento_tecnico', 'transportadora', 'empresa')
    list_display = ('data_pedido_recolha', 'recolha_efectuada',  'transportadora', 'empresa')
    filter_horizontal = ('moradas',)

    def show_map(self, obj, recolha):
        from django.shortcuts import render_to_response
        return render_to_response('empresa/recolha.html', {'recolha':recolha})
    show_map.short_description='Show map'

    buttons = [ show_map ]

class PropostaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,         {'fields': ['n_proposta', 'n_facturacao', 'n_campanha', 'n_fontes', 'n_trabalhadores', 'data_abertura', 'data_entrega', 'empresa', 'contrato', 'moradas', 'responsavel', 'decisao', 'data_decisao', 'tipo_proposta', 'pedido_de_consulta']}),
    ]
    list_display = ('n_proposta', 'empresa', 'n_campanha', 'n_fontes', 'n_trabalhadores','contrato','tipo_proposta')
    list_filter = ('empresa',  'moradas', 'contrato', 'decisao','tipo_proposta')

class TipoPropostaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,         {'fields': ['tipo']}),
    ]
    list_display = ('tipo',)

class PedidoDeConsultaAdmin(admin.ModelAdmin):
    list_filter = ('colaboradores',)

admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Vendedor)
admin.site.register(Contrato, ContratoAdmin)
admin.site.register(Transportadora)
admin.site.register(Proposta, PropostaAdmin)
admin.site.register(ObservacaoEmpresa, ObservacaoEmpresaAdmin)
admin.site.register(Colaborador)
admin.site.register(Recolha, RecolhaAdmin)
admin.site.register(EmpresaMorada)
admin.site.register(CodigoLER)
#admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(TipoProposta, TipoPropostaAdmin)
admin.site.register(ServicoContratado)
admin.site.register(TipoServicoContratado)
admin.site.register(Alerta)
admin.site.register(EstadoAlerta)
admin.site.register(PedidoDeConsulta, PedidoDeConsultaAdmin)
admin.site.register(Sirapa)
