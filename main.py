from Contas import *
from Pessoa import *
from Poupanca import *

print("Relatório de Contas")
cliente = Pessoa("Marcus")
print(f"Olá, {cliente.nome} !")
banco = input("Digite o nome do Banco: ")
poupanca = Poupanca()
contas = Contas(cliente, banco, poupanca)
contas.balancos()

count = 1


def retorna():
    banco2 = input("Digite o nome do Banco: ")
    contas2 = Contas(cliente, banco2, poupanca)
    contas2.balancos()
    i = 1
    while i != 0:
        print(f"Banco: {contas2.banco}")
        print("---------------------------------------")
        print("1 - Ações dentro da Conta Corrente")
        print("---------------------------------------")
        print("2 - Ações dentro da Conta Crédito")
        print("---------------------------------------")
        print("3 - Ações dentro da Poupança")
        print("---------------------------------------")
        print("4 - Finalizar")
        print("---------------------------------------")
        escolha2 = int(input("Digite o número: "))
        if escolha2 == 1:
            contas2.conta_corrente()
        elif escolha2 == 2:
            contas2.conta_credito()
        elif escolha2 == 3:
            contas2.poupanca.menu()
        else:
            print("Término")
            i = i - 1


while count != 0:
    print(f"Banco: {contas.banco}")
    print("---------------------------------------")
    print("1 - Ações dentro da Conta Corrente")
    print("---------------------------------------")
    print("2 - Ações dentro da Conta Crédito")
    print("---------------------------------------")
    print("3 - Ações dentro da Poupança")
    print("---------------------------------------")
    print("4 - Trocar de Banco")
    print("---------------------------------------")
    print("5 - Finalizar")
    print("---------------------------------------")
    escolha = int(input("Digite o número: "))
    if escolha == 1:
        contas.conta_corrente()
    elif escolha == 2:
        contas.conta_credito()
    elif escolha == 3:
        contas.poupanca.menu()
    elif escolha == 4:
        break
    else:
        print("Término")
        count = count - 1
if count == 1:
    retorna()
