from Contas import *
from Pessoa import *

print("Relatório de Contas")
pessoa = Pessoa("Marcus")
print(f"Olá, {pessoa.nome} !")
banco = input("Digite o nome do Banco: ")
contas = Contas(pessoa, banco)
contas.balancos()

count = 1


def retorna():
    banco = input("Digite o nome do Banco: ")
    contas2 = Contas(pessoa, banco)
    contas2.balancos()
    i = 1
    while i != 0:
        print(f"Banco: {contas2._banco}")
        print("---------------------------------------")
        print("1 - Ações dentro da Conta Corrente")
        print("---------------------------------------")
        print("2 - Ações dentro da Conta Crédito")
        print("---------------------------------------")
        print("3 - Finalizar")
        print("---------------------------------------")
        escolha = int(input("Digite o número: "))
        if escolha == 1:
            contas2.conta_corrente()
        elif escolha == 2:
            contas2.conta_credito()
        else:
            print("Término")
            i = i -1



while count != 0:
    print(f"Banco: {contas._banco}")
    print("---------------------------------------")
    print("1 - Ações dentro da Conta Corrente")
    print("---------------------------------------")
    print("2 - Ações dentro da Conta Crédito")
    print("---------------------------------------")
    print("3 - Trocar de Banco")
    print("---------------------------------------")
    print("4 - Finalizar")
    print("---------------------------------------")
    escolha = int(input("Digite o número: "))
    if escolha == 1:
        contas.conta_corrente()
    elif escolha == 2:
        contas.conta_credito()
    elif escolha == 3:
        break
    else:
        print("Término")
        count = count - 1
retorna()