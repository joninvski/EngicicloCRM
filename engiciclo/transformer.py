from crm.models import Empresa, Vendedor

def create_empresa(cliente_csv):
    empresa = Empresa()
    empresa.nome = cliente_csv.nome_empresa
    empresa.nif = cliente_csv.nipc
    empresa.data_adesao = cliente_csv.data_adesao
    empresa.n_facturacao = cliente_csv.n_factura
    empresa.cliente_berner = cliente_csv.cliente_berner

    if cliente_csv.valor_contratado:
        empresa.cliente = True

    return empresa

def create_vendedor(cliente_csv):
    vendedor = Vendedor()
    vendedor.nome =  cliente_csv.vendedor

    return vendedor
