estoque = {}
print("Bem vindo a loja ")
while True:
    print("-------------------------------")
    print("         o que deseja          ")
    print("-------------------------------")
    print()
    print("🔸1🔸registrar veiculo")
    print("🔸2🔸Visualizar estoque")
    print("🔸3🔸Adicionar item ao carrinho")
    print("🔸4🔸Visualizar carrinho")
    print("🔸5🔸Finalizar compra")
    print("🔸6🔸Sair do sistema")
    print()
    print("-------------------------------")
    escolha = int(input("qual sua escolha"))
    match escolha:
        case 1:
            print("---------------------------")
            print("     Registo de veiculos   ")
            print("---------------------------")
            veiculo = input("tipo de veiculo")
            estoque.setdefault(veiculo)
            nome,valor = input("digite o nome do veiculo e o valor separados por espaço").split()
            estoque[veiculo]={nome,int(valor)}
            print("estoque atualizado")
        case 2:
            for veiculo,dados in estoque.items():


