import pdb
from crm.models import Vendedor, Pessoa, Empresa

def create_empresa(cliente_csv):
    empresa = Empresa()
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
    nomes = cliente_csv.pessoas.replace(' e/ou', ' # ').replace(' e ', ' # ').replace(' ou ', ' # ').replace('/', ' # ')
    nomes = nomes.split(' # ') 

    lista_pessoas = []
    for nome in nomes:
        pessoa = Pessoa()
        pessoa.nome =  nome
        pessoa.telefone = cliente_csv.telefone
        pessoa.contacto_principal = True
        pessoa.empresa = empresa
        pessoa.save()

    return lista_pessoas 
