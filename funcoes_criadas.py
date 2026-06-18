def imprimir_dic (n1,n2):
    for n1,dados in n2:
        print(f"""{"═══════🚘═══════"*3}
    {"ID":<5} | {"NOME":^15} | {"QUANTIDADE":<10} | {"VALOR":<10}
{"🏁"*22}
{n1:<5} | {dados["nome"]:<15} | {dados["quantidade"]:<10} | {dados["valor"]:<10}
{"═══════🚘═══════"*3}""")

def imprimir_dic2 (n1,n2):
    for n1,dados in n2:
        print(f"""{"═══════🚘═══════"*4}
    {"ID":<5} | {"NOME":^15} | {"QUANTIDADE":<10} | {"VALOR":<10} | {"SUB VALOR":<10}
{"🏁"*22}
{n1:<5} | {dados["nome"]:<15} | {dados["quantidade"]:<10} | {dados["valor"]:<10} |  {n3:<10}
{"═══════🚘═══════"*4}""")

def imprimir_dic3 (n1,n2):
    for n1,dados in n2:
        print(f"""{"═══════🚘═══════"*4}
    {"ID":<5} | {"NOME":^15} | {"QUANTIDADE":<10} | {"VALOR":<10} | {"SUB VALOR":<10}
{"🏁"*22}
{n1:<5} | {dados["nome"]:<15} | {dados["quantidade"]:<10} | {dados["valor"]:<10} |  {dados["subtotal"]:<10}
{"═══════🚘═══════"*4}""")


def carrinho_sistema(n1,n2):
    escolhaV = input("escolha um carro do catalogo")
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

