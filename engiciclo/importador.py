import csv
import transformer

class EmpresaCSV():
    def __init__(self, n_cliente, n_factura, n_estabelecimento, n_contrato, S, V, C, R, renovacao, cliente_berner, data_adesao, vendedor, valor_contratado, nipc, nome_empresa, telefone):
        self.n_cliente = n_cliente
        self.n_factura = n_factura
        self.n_estabelecimento = n_estabelecimento
        self.n_contrato = n_contrato
        self.S = S
        self.V = V
        self.C = C
        self.R = R
        self.renovacao = renovacao
        self.cliente_berner = cliente_berner
        self.data_adesao = data_adesao
        self.vendedor = vendedor
        self.valor_contratado = valor_contratado
        self.nipc = nipc
        self.nome_empresa = nome_empresa
        self.telefone = telefone

    def __str__(self):
        return str(self.n_cliente)

def create_empresa_CSV(row):
    print row[17]
    return EmpresaCSV(\
                     n_cliente           =   row[0],\
                     n_factura           =   row[1],\
                     n_estabelecimento   =   row[1],\
                     n_contrato          =   row[2],\
                     S                   =   row[3],\
                     V                   =   row[4],\
                     C                   =   row[5],\
                     R                   =   row[6],\
                     renovacao           =   row[7],\
                     cliente_berner      =   row[8],\
                     data_adesao         =   row[9],\
                     vendedor            =   row[12],\
                     valor_contratado    =   row[13],\
                     nipc                =   row[14],\
                     nome_empresa        =   row[15],\
                     telefone            =   row[17]\
                     )

def create_clientes_csv(clientes_reader):
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
        transformer.create_empresa(c)
        transformer.create_vendedor(c)

if __name__ == '__main__':
    main()
