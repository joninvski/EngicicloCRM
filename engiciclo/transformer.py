import pdb
from crm.models import Vendedor, Pessoa, Empresa, EmpresaMorada, Contrato
import datetime

def create_empresa(cliente_csv):
    empresa = Empresa()
    empresa.n_entrada = cliente_csv.n_cliente
    empresa.nome = cliente_csv.nome_empresa
    empresa.nif = cliente_csv.nipc
    empresa.data_adesao = cliente_csv.data_adesao
    empresa.n_facturacao = cliente_csv.n_factura
    empresa.cliente_berner = cliente_csv.cliente_berner

    if cliente_csv.valor_contratado:
        empresa.cliente = True

    empresa.save()
    return empresa

def create_vendedor(cliente_csv, empresa):

    try:
        vendedor = Vendedor.objects.get(nome=cliente_csv.vendedor)

    except Exception:
        vendedor = Vendedor()
        vendedor.nome =  cliente_csv.vendedor
        vendedor.save()

    empresa.vendedores.add(vendedor)

    return vendedor

def create_pessoas(cliente_csv, empresa):
    nomes = cliente_csv.pessoas.replace(' e/ou  ', ' # ').replace(' e ', ' # ').replace(' ou ', ' # ').replace('/', ' # ')
    nomes = nomes.split(' # ') 

    lista_pessoas = []
    for nome in nomes:
        pessoa = Pessoa()
        pessoa.nome =  nome
        pessoa.telefone = cliente_csv.telefone
        pessoa.fax = cliente_csv.fax
        pessoa.movel = cliente_csv.movel
        pessoa.email = cliente_csv.email
        pessoa.contacto_principal = True
        pessoa.empresa = empresa
        pessoa.save()

    return lista_pessoas 

def create_moradas(cliente_csv, empresa):
    empresaMorada = EmpresaMorada()
    empresaMorada.rua = cliente_csv.instalacoes
    empresaMorada.localidade =  cliente_csv.localidade
    empresaMorada.cod_postal = cliente_csv.cod_postal
    empresaMorada.concelho = cliente_csv.concelho
    empresaMorada.empresa = empresa
    empresaMorada.save()

def create_contrato(cliente_csv, empresa):
    if(cliente_csv.n_contrato):
        contrato = Contrato()
        contrato.numero = cliente_csv.n_contrato
        contrato.data_inicio = datetime.datetime.strptime(cliente_csv.data_adesao, '%d/%m/%y')
        one_year = datetime.timedelta(weeks=40, days=84, hours=23, minutes=50, seconds=600)
        contrato.data_fim = contrato.data_inicio + one_year
        contrato.empresa = empresa
        contrato.save()
