estoque = {1:{ "maclaren":120000.00,
               "ferrari puro sangue":1000000.00,
               "mustang gtr":400000.00}}
print("Bem vindo a loja ")
while True:
    print("-------------------------------")
    print("         o que deseja          ")
    print("-------------------------------")
    print()
    print("🔸1🔸Visualizar estoque")
    print("🔸2🔸Adicionar item ao carrinho")
    print("🔸3🔸Visualizar carrinho")
    print("🔸4🔸Finalizar compra")
    print("🔸5🔸Sair do sistema")
    print()
    print("-------------------------------")
    escolha = int(input("qual sua escolha"))
    match escolha:
        case 1:
            
