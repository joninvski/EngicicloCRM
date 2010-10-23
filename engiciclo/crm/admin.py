from crm.models import Empresa, Pessoa, Morada, ServicoContratado, Transportadora, Recolha
from django.contrib import admin

class MoradaInline(admin.TabularInline):
    model = Morada 

class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 2

class ServicoContratadoInline(admin.TabularInline):
    model = ServicoContratado
    extra = 1

class RecolhaInline(admin.TabularInline):
    model = Recolha
    extra = 1

class EmpresaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,         {'fields': ['nome', 'n_entrada', 'n_facturacao', 'cliente']}),
        ('Mais dados', {'fields': ['data_inicio','comentario'], 'classes': ['collapse']}),
    ]
    inlines = [ServicoContratadoInline, RecolhaInline, MoradaInline, PessoaInline]
    list_display = ('nome',)

admin.site.register(Transportadora)
admin.site.register(Empresa, EmpresaAdmin)
