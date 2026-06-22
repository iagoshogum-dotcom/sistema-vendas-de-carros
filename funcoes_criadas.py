import random



def imprimir_dic (n1,n2):
    print(f"""
            {"\033[38;5;196m══🚘══\033[0m" * 12}

                                         ⚫ESTOQUE DISPONÍVEL⚫

            {"\033[38;5;196m══🚘══\033[0m" * 12}
            """)
    for n1,dados in n2:
        print(f"""{"═══════🚘═══════"*3}
    {"ID":<5} | {"NOME":^15} | {"QUANTIDADE":<10} | {"VALOR":<10}
{"🏁"*22}
{n1:<5} | {dados["nome"]:<15} | {dados["quantidade"]:<10} | {dados["valor"]:<10}
{"═══════🚘═══════"*3}""")

def imprimir_dic2(n1, n2):
    print(f"""
            {"\033[38;5;196m══🚘══\033[0m" * 12}

                                        ⚫SEU CARRINHO⚫

            {"\033[38;5;196m══🚘══\033[0m" * 12}
            """)
    for n1, dados in n2:
        print(f"""{"═══════🚘═══════"*4}
{"ID":<5} | {"NOME":^15} | {"QUANTIDADE":<10} | {"VALOR":<10} | {"SUB VALOR":<10}
{"🏁"*22}
{n1:<5} | {dados["nome"]:<15} | {dados["quantidade"]:<10} | {dados["valor"]:<10} | {dados["subtotal"]:<10}
{"═══════🚘═══════"*4}""")



def registrar_veiculo(estoque):
    print(f"""
    {"\033[38;5;196m══🚘══\033[0m"* 12}

                                ⚫REGISTRO DE VEÍCULO⚫

    {"\033[38;5;196m══🚘══\033[0m"* 12}
    """)

    veiculo = input("tipo de veiculo ") + "0"
    veiculo += str(random.randint(0, 1000))

    nome, valor, quantidade = input(
        "digite o nome do veiculo o valor e a quantidade separados por virgula: ").split(",")

    estoque[veiculo] = {
        "nome": nome,
        "valor": float(valor),
        "quantidade": int(quantidade)
    }

    return veiculo

def carrinho_sistema(n1,n2):
    escolhaV = input("escolha um veiculo do catalogo")
    if escolhaV in n1:
        qtd = int(input("quantos deseja comprar"))
        if n1[escolhaV]["quantidade"] >= qtd:
            n1[escolhaV]["quantidade"] -= qtd
            n2[escolhaV] = {
                "nome": n1[escolhaV]["nome"],
                "valor": n1[escolhaV]["valor"],
                "quantidade": qtd,
                "subtotal": qtd * n1[escolhaV]["valor"]
            }
            print("Adicionado ao carrinho")
        else:
            print("Quantidade nao disponivel em estoque")
    else:
        print("Item nao encontrado no estoque")

def finalizar_compra(carrinho, estoque):
    print(f"""
    {"\033[38;5;196m══🚘══\033[0m" * 12}

                                ⚫RESUMO DA COMPRA⚫

    {"\033[38;5;196m══🚘══\033[0m" * 12}
    """)
    if len(carrinho) == 0:
        print("Carrinho vazio!")
        return

    total = 0
    desconto = 0

    possui_cupom = input("Possui cupom de desconto? s/n ")

    if possui_cupom.lower() == "s":
        cupom = input("Digite o cupom: ")

        match cupom:
            case "DEV10":
                desconto = 10
            case "DEV20":
                desconto = 20
            case _:
                print("Cupom inválido!")

    print("\n🛒 RESUMO DA COMPRA\n")

    for veiculo, dados in carrinho.items():

        subtotal_original = dados["valor"] * dados["quantidade"]
        subtotal = subtotal_original
        valor_desconto = 0

        if desconto == 10:
            valor_desconto = subtotal * 0.10
            subtotal -= valor_desconto

        elif desconto == 20 and subtotal > 500:
            valor_desconto = subtotal * 0.20
            subtotal -= valor_desconto

        total += subtotal

        print(f"""{"═══════🚘═══════"*4}
{"ID":<10} | {"NOME":<15} | {"QTD":<5} | {"VALOR":<12} | {"SUBTOTAL":<12}
{"🏁"*30}
{veiculo:<10} | {dados["nome"]:<15} | {dados["quantidade"]:<5} | R${dados["valor"]:<10.2f} | R${subtotal:<10.2f}
{"═══════🚘═══════"*4}""")

        if valor_desconto > 0:
            print(f"""
🎟️ DESCONTO APLICADO: {desconto}%
💰 VOCÊ ECONOMIZOU: R${valor_desconto:.2f}
{"═"*40}
""")

    print(f"""
{"\033[38;5;196m══🚘══\033[0m"*12}
                    ⚫TOTAL DA COMPRA: R${total:.2f}⚫
{"\033[38;5;196m══🚘══\033[0m"*12}
""")

    finalizar = input("Deseja finalizar a compra? s/n ")

    if finalizar.lower() == "s":
        carrinho.clear()
        print(f"""
        {"\033[38;5;196m══🚘══\033[0m" * 12}

                                   ✅ COMPRA REALIZADA COM SUCESSO!

        Obrigado pela preferência.

        {"\033[38;5;196m══🚘══\033[0m" * 12}
        """)

    else:
        print(f"""
        {"\033[38;5;196m══🚘══\033[0m" * 12}

                                   ❌ COMPRA CANCELADA

        {"\033[38;5;196m══🚘══\033[0m" * 12}
        """)

        limpar = input(
            "Deseja limpar o carrinho e devolver os itens ao estoque? s/n "
        )

        if limpar.lower() == "s":

            for veiculo, dados in carrinho.items():
                estoque[veiculo]["quantidade"] += dados["quantidade"]

            carrinho.clear()

            print("🔄 Carrinho limpo e estoque restaurado!")

        else:
            print("🛒 Carrinho mantido.")

def menu():
    print(f"""
    ╔══════🚘══════🚘══════🚘══════🚘══════🚘══════🚘══════🚘══════🚘══════🚘══════🚘══════🚘══════🚘═════╗                                                          
  ╔═║                                                                                                        ║═╗
███████╗███████╗ ██████╗ ██████╗ ██████╗  █████╗ ██████╗     ███╗   ███╗ ██████╗ ████████╗ ██████╗ ██████╗ ███████╗
██╔════╝██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗██╔══██╗    ████╗ ████║██╔═══██╗╚══██╔══╝██╔═══██╗██╔══██╗██╔════╝
█████╗  ███████╗██║     ██║   ██║██████╔╝███████║██████╔╝    ██╔████╔██║██║   ██║   ██║   ██║   ██║██████╔╝███████╗
██╔══╝  ╚════██║██║     ██║   ██║██╔══██╗██╔══██║██╔══██╗    ██║╚██╔╝██║██║   ██║   ██║   ██║   ██║██╔══██╗╚════██║
███████╗███████║╚██████╗╚██████╔╝██████╔╝██║  ██║██║  ██║    ██║ ╚═╝ ██║╚██████╔╝   ██║   ╚██████╔╝██║  ██║███████║
╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝     ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝
    ║      \033[38;5;240m                              ╔▄███████████████████████████▄╗                \033[0m                     ║
    ║      \033[38;5;240m                           ╔██▀                             ▀██╗             \033[0m                     ║
    ║      \033[38;5;240m                       ▀▀╔██▀                                 ▀██╗▀▀         \033[0m                     ║
    ║      \033[38;5;196m                       ▄██████████                       ██████████▄         \033[0m                     ║
    ║      \033[38;5;196m                    ▄█▀   █▄▄▄   ▀▀█████████████████████▀▀    ▄▄▄█  ▀█▄      \033[0m                     ║
    ║      \033[38;5;196m                    ██    █   ▀▄ ▄                        ▄ ▄▀   █   ██      \033[0m                     ║
    ║      \033[38;5;196m                    ██    ▀▀▀▀▀   ▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀    ▀▀▀▀▀   ██      \033[0m                     ║
    ║      \033[38;5;196m                    ██             ▀█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▀             ██      \033[0m                     ║
    ║      \033[38;5;196m                     ▀████████████▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄███████████▀       \033[0m                     ║
    ║      \033[38;5;196m                       ▀█    █▀▀▀▀▀▀                   ▀▀▀▀▀▀█    █▀         \033[0m                     ║
    ╠════🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁═══╣
    ║                                                                                                        ║
    ║                                       🔹 [1] Registrar veículo          🔹                             ║
    ║                                       🔹 [2] Visualizar estoque         🔹                             ║
    ║                                       🔹 [3] Adicionar item ao carrinho 🔹                             ║
    ║                                       🔹 [4] Visualizar carrinho        🔹                             ║
    ║                                       🔹 [5] Finalizar compra           🔹                             ║
    ║                                       🔹 [6] Sair do sistema            🔹                             ║
    ║                                                                                                        ║
    ╠═════🚘══════🚘══════🚘══════🚘══════🚘══════🚘══════🚘══════🚘══════🚘══════🚘══════🚘══════🚘══════╣
 
    """)
