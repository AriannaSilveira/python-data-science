import lib
import cadastro_cliente
import cadastro_pedido

print("-" * 100)
print("                           PROGRAMA DE PRODUTOS DOS CLIENTES")
print("-" * 100)

while(True):
    print("\nSelecione uma das opções abaixo:")
    print("1 - Cadastro de clientes.")
    print("2 - Lista de clientes.")
    print("3 - Cadastro de pedidos.")
    print("4 - Lista de pedidos.")
    print("5 - Sair.\n")

    op = int(input("Digite a opção: "))

    if op == 1:
        cadastro_cliente.cadastrar()
    elif op == 2:
        cadastro_cliente.listar()
    elif op == 3:
        cadastro_pedido.cadastrar()
    elif op == 4:
        cadastro_pedido.listar()
    elif op == 5:
        break
    else:
        lib.msg("Opção inválida!")