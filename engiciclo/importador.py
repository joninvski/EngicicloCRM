import pdb
import csv
import transformer

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

class EmpresaCSV():
    def __init__(self, n_cliente, n_factura, n_estabelecimento, n_contrato, S, V, C, R, cliente_berner, data_adesao, vendedor, valor_contratado, nipc, nome_empresa, pessoas, telefone, fax, movel, email, instalacoes, localidade, cod_postal, concelho, distrito, instalacoes_facturacao, localidade_facturacao, cod_postal_facturacao, concelho_facturacao, distrito_facturacao):
        self.n_cliente = n_cliente
        self.n_factura = n_factura
        self.n_estabelecimento = n_estabelecimento
        self.n_contrato = n_contrato
        self.S = S
        self.V = V
        self.C = C
        self.R = R
        self.cliente_berner = cliente_berner
        self.data_adesao = data_adesao
        self.vendedor = vendedor
        self.valor_contratado = valor_contratado
        self.nipc = nipc.replace(' ','')
        self.nome_empresa = nome_empresa
        self.telefone = telefone
        self.fax = fax
        self.movel = movel
        self.email = email
        self.pessoas = pessoas
        self.instalacoes = instalacoes
        self.localidade = localidade
        self.cod_postal = cod_postal
        self.concelho = concelho
        self.distrito = distrito
        self.instalacoes_facturacao = instalacoes_facturacao
        self.localidade_facturacao = localidade_facturacao
        self.cod_postal_facturacao = cod_postal_facturacao
        self.concelho_facturacao = concelho_facturacao
        self.distrito_facturacao = distrito_facturacao

    def __str__(self):
        return str(self.n_cliente)

def create_empresa_CSV(row):
    return EmpresaCSV(\
                     n_cliente           =   row[0],\
                     n_factura           =   row[1],\
                     n_estabelecimento   =   row[1],\
                     n_contrato          =   row[3],\
                     S                   =   row[4],\
                     V                   =   row[5],\
                     C                   =   row[6],\
                     R                   =   row[7],\
                     cliente_berner      =   row[8],\
                     data_adesao         =   row[9],\
                     vendedor            =   row[10],\
                     valor_contratado    =   row[11],\
                     nipc                =   row[13],\
                     nome_empresa        =   row[14],\
                     pessoas             =   row[15],\
                     telefone            =   row[16],\
                     fax                 =   row[17],\
                     movel               =   row[18],\
                     email               =   row[19],\
                     instalacoes         =   row[21],\
                     localidade          =   row[22],\
                     cod_postal          =   row[23],\
                     concelho            =   row[24],\
                     distrito            =   row[25],\
                     instalacoes_facturacao        =   row[26],\
                     localidade_facturacao         =   row[27],\
                     cod_postal_facturacao         =   row[28],\
                     concelho_facturacao           =   row[29],\
                     distrito_facturacao           =   row[30]\
                     )

def create_clientes_csv(clientes_reader):
    """
    Create the cvs data related with the clientes file
    """
    lista_empresas = []
    for row in clientes_reader:
        if not row[0]: break

        empresa = create_empresa_CSV(row)
        lista_empresas.append(empresa)
    return lista_empresas

def get_clientes_csv_reader(clients_ods_path):
    clientes_reader = csv.reader(open(clients_ods_path, 'rb'), delimiter=',',quotechar='"')
    return clientes_reader

def skip_first_cliente_lines(clientes_reader):
    first_row = 9

    for row in clientes_reader:
        first_row -= 1
        if first_row <= 0:
            return

def main():
    clientes_reader = get_clientes_csv_reader('clientes.csv')
    skip_first_cliente_lines(clientes_reader)
    clientes_csv = create_clientes_csv(clientes_reader)

    for c in clientes_csv:
        empresa = transformer.create_empresa(c)
        vendedor = transformer.create_vendedor(c, empresa)
        pessoas = transformer.create_pessoas(c, empresa)
        moradas = transformer.create_moradas(c, empresa)
        contrato = transformer.create_contrato(c, empresa)

if __name__ == '__main__':
    main()
