from crm.models import Empresa, Pessoa, Morada, ServicoContratado, Transportadora, Recolha, Contrato, EmpresaMorada, Proposta, ObservacaoEmpresa, Colaborador, TipoProposta
from django.contrib import admin

class EmpresaMoradaInline(admin.TabularInline):
    model = EmpresaMorada

class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 2

class ContratoInline(admin.TabularInline):
    model = Contrato
    extra = 1

class RecolhaInline(admin.TabularInline):
    model = Recolha
    extra = 1

class ObservacaoEmpresaInline(admin.TabularInline):
    model = ObservacaoEmpresa 
    extra = 1

class ColaboradorInline(admin.TabularInline):
    model = Colaborador
    extra = 3

class EmpresaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,         {'fields': ['nome', 'n_entrada', 'n_facturacao', 'cliente']}),
        ('Mais dados', {'fields': ['data_inicio','comentario'], 'classes': ['collapse']}),
    ]
    inlines = [ContratoInline, RecolhaInline, EmpresaMoradaInline, PessoaInline]
    list_display = ('nome','nif','data_inicio')

class ContratoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,         {'fields': ['numero', 'data_inicio', 'data_fim']}),
    ]
    list_display = ('numero','data_inicio', 'data_fim')
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
        ('Dados Base',         {'fields': ['nome', 'empresa', 'data_nascimento']}),
    ]
    list_filter = ('empresa',)

class RecolhaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,         {'fields': ['data_pedido_recolha', 'recolha_efectuada', 'acompanhamento_tecnico', 'transportadora', 'empresa']}),
    ]
    list_filter = ('data_pedido_recolha', 'recolha_efectuada', 'acompanhamento_tecnico', 'transportadora', 'empresa')
    list_display = ('data_pedido_recolha', 'recolha_efectuada', 'acompanhamento_tecnico', 'transportadora', 'empresa')

class PropostaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,         {'fields': ['n_proposta', 'n_facturacao', 'n_campanha', 'n_fontes', 'n_trabalhadores', 'data_abertura', 'data_entrega', 'empresa', 'contrato', 'moradas', 'responsavel', 'decisao', 'data_decisao', 'tipo_proposta']}),
    ]
    list_display = ('n_proposta', 'empresa', 'n_campanha', 'n_fontes', 'n_trabalhadores','contrato','tipo_proposta')
    list_filter = ('empresa',  'moradas', 'contrato', 'decisao','tipo_proposta')

class TipoPropostaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,         {'fields': ['tipo']}),
    ]
    list_display = ('tipo',)

admin.site.register(Transportadora)
admin.site.register(Contrato, ContratoAdmin)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Proposta, PropostaAdmin)
admin.site.register(ObservacaoEmpresa, ObservacaoEmpresaAdmin)
admin.site.register(Colaborador)
admin.site.register(EmpresaMorada)
admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Recolha, RecolhaAdmin)
admin.site.register(TipoProposta, TipoPropostaAdmin)
