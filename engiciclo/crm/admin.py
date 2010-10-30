from crm.models import Empresa, Pessoa, Morada, ServicoContratado, Transportadora, Recolha, Contrato, EmpresaMorada
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

class EmpresaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,         {'fields': ['nome', 'n_entrada', 'n_facturacao', 'cliente']}),
        ('Mais dados', {'fields': ['data_inicio','comentario'], 'classes': ['collapse']}),
    ]
    inlines = [ContratoInline, RecolhaInline, EmpresaMoradaInline, PessoaInline]
    list_display = ('nome',)

admin.site.register(Transportadora)
admin.site.register(Empresa, EmpresaAdmin)
