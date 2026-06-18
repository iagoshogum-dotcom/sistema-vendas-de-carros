import random
from funcoes_criadas import *
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
            print("▞▞▞▞▞▖🆁🅴🅶🅸🆂🆃🆁🅾 🅳🅴 🆅🅴🅸🅲🆄🅻🅾🆂▝▞▞▞▞▞\n   ")
            veiculo = input("tipo de veiculo")+str(0)
            veiculo += str(random.randint(0, 1000))
            nome,valor,quantidade = input("digite o nome do veiculo o valor e a quantidade").split()
            estoque[veiculo]={
                "nome": nome,
                "valor": float(valor),
                "quantidade": int(quantidade)}
        case 2:
            imprimir_dic(veiculo,estoque.items())
        case 3:
            carrinho_sistema(estoque,carrinho)
        case 4:
            imprimir_dic2(veiculo,carrinho.items())
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

