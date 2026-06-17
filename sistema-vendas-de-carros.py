import random
carrinho = {}
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
            print("▞▞▞▞▞▖🆁🅴🅶🅸🆂🆃🆁🅾 🅳🅴 🆅🅴🅸🅲🆄🅻🅾🆂▝▞▞▞▞▞   ")
            veiculo = input("tipo de veiculo")+str(0)
            veiculo += str(random.randint(0, 1000))
            nome,valor,quantidade = input("digite o nome do veiculo o valor e a quantidade").split()
            estoque[veiculo]={
                "nome": nome,
                "valor": float(valor),
                "quantidade": int(quantidade)}
        case 2:
            for veiculo,dados in estoque.items():
                print(f"identificação:{veiculo}\nnome:{dados["nome"]}\nvalor:R${dados["valor"]}\nquantidade:{dados["quantidade"]}")
        case 3:
            escolhaV = input("escolha um carro do catalogo")
            if escolhaV in estoque:
                qtd = int(input("quantos deseja comprar"))
                if estoque[escolhaV]["quantidade"] >= qtd:
                    estoque[escolhaV]["quantidade"] -= qtd
                    carrinho[escolhaV]={
                        "nome":estoque[escolhaV]["nome"],
                        "valor":estoque[escolhaV]["valor"],
                        "quantidade":qtd
                    }
                    print("Adicionado ao carrinho")
                else:
                    print("Quantidade nao disponivel em estoque")
            else:
                print("Item nao encontrado no estoque")
        case 4:
            for veiculo,dados in carrinho.items():
                print(f"identificação:{veiculo}\nnome:{dados["nome"]}\nvalor:R${dados["valor"]}\nquantidade:{dados["quantidade"]}")
        case 5:
            total = 0
            desconto = input("possui cupon de desconto? s/n")
            if desconto == "s":
                cupon = input("digite o cupon")
                match cupon:
                    case "DEV10":
                        desconto = 10
                    case "DEV20":
                        desconto = 20
                    case _:
                        print("cupon invalido")
            else:
                print("Area para confirmação de pagamento")

            for veiculo,dados in carrinho.items():
                subtotal = dados["valor"]*dados["quantidade"]
                if desconto == 10:
                    subtotal -= subtotal*10 / 100
                elif desconto == 20:
                    if subtotal > 500:
                        subtotal -= subtotal*20/100

                total += subtotal
                print(f"identificação:{veiculo}\nnome:{dados["nome"]}\nvalor:R${dados["valor"]}\nquantidade:{dados["quantidade"]}\nsubtotal da compra:R${subtotal} desconto aplicado de {desconto}%")
            print(f"total da compra: R${total}")
            finalizar = input("deseja finalizar a compra? s/n")
            if finalizar == "s":
                carrinho.clear()
                print("compra realizada com sucesso")
            else:
                print("compra cancelada")
        case 6:
            print("volte sempre")
            break

