import lib
import action_csv
import uuid
import cadastro_cliente
filename = "pedidos.csv"


def cadastrar():
    lib.limpar_tela()

    cliente = cadastro_cliente.localiza_cliente()
    pedido = {}

    pedido["id"] = str(uuid.uuid4())
    pedido["cliente_id"] = cliente["id"]
    pedido["nome"] = input("Digite o nome do produto: ")
    pedido["valor"] = input("Digite o valor do produto: ")
    pedido["quantidade"] = input("Digite a quantidade do produto: ")
    pedido["valor_total"] = float(pedido["valor"]) * float(pedido["quantidade"])

    lista = action_csv.ler(filename)
    lista.append(pedido)
    action_csv.salvar(lista, filename)
    lib.msg("Pedido cadastrado com sucesso!")
    input("Digite enter para continuar...")

def listar():
    lib.limpar_tela()
    lista = action_csv.ler(filename)
    for item in lista:
        print("-"*60)
        print("Id: " + item["id"])
        cliente = action_csv.busca_por_id(item["cliente_id"], "clientes.csv")
        print("Cliente: " + cliente["nome"])
        print("Nome: "+ item["nome"])
        print("Valor da unidade: R$" + item["valor"])
        print("Quantidade: " + item["quantidade"])
        print("Valor total: R$" + item["valor_total"])
    input("Digite enter para continuar...")
    lib.limpar_tela()