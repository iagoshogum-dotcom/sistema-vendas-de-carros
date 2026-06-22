import random
import webbrowser
from funcoes_criadas import *
VERMELHO = "\033[38;5;196m"
RESET = "\033[0m"
GRAFITE = "\033[38;5;240m"
carrinho = {}
estoque = {}
print("Bem vindo a loja ")
webbrowser.open("https://www.youtube.com/watch?v=t-yCg-0-baE&list=RDt-yCg-0-baE&start_radio=1")
menu()
while True:
    escolha = int(input("\033[38;5;196m══🚘══\033[0m Escolha uma opção do menu\033[38;5;196m ══🚘══\033[0m:"))
    match escolha:
        case 1:
            veiculo = registrar_veiculo(estoque)
        case 2:
            imprimir_dic(veiculo,estoque.items())
        case 3:
            carrinho_sistema(estoque,carrinho)
        case 4:
            imprimir_dic2(veiculo,carrinho.items())
        case 5:
            finalizar_compra(carrinho,estoque)
        case 6:
            print("volte sempre")
            break

