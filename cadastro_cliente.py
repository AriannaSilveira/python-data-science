import lib
import action_csv
import uuid
filename = "clientes.csv"


def cadastrar():
    lib.limpar_tela()
    cliente = {}

    cliente["id"] = str(uuid.uuid4())
    cliente["nome"] = input("Digite o nome do cliente: ")
    cliente["telefone"] = input("Digite o telefone do cliente: ")
    cliente["email"] = input("Digite o email do cliente: ")

    lista = action_csv.ler(filename)
    lista.append(cliente)
    action_csv.salvar(lista, filename)
    lib.msg("Cliente cadastrado com sucesso!")
    input("Digite enter para continuar...")

def listar():
    lib.limpar_tela()
    lista = action_csv.ler(filename)
    for item in lista:
        print("-"*60)
        print("Nome: "+ item["nome"])
        print("Telefone: " + item["telefone"])
        print("E-mail: " + item["email"])
    input("Digite enter para continuar...")
    lib.limpar_tela()

def localiza_cliente():
    lib.limpar_tela()
    lista = action_csv.ler(filename)
    for idx, item in enumerate(lista):
        print("-"*60)
        print("Índice: "+ str(idx))
        print("Nome: "+ item["nome"])
        print("Telefone: " + item["telefone"])
        print("E-mail: " + item["email"])
    
    indice = input("Digite o indice de qual cliente você deseja localizar: ")
    cliente = lista[int(indice) - 1]
    if cliente == None:
        lib.msg("Opção invalida!")
        localiza_cliente()
    return cliente