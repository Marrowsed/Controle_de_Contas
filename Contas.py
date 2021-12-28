import Pessoa
import Banco


class Contas:

    def __init__(self, pessoa: Pessoa, banco: Banco):
        self._pessoa = pessoa
        self._banco = banco
        self._value = 0
        self._credito = 0
        self.contas_corrente = []
        self.contas_credito = []
        self.parceladas = []
        self.balanco = {}

    def balancos(self):
        value = float(input("Digite o saldo da C/C: ").replace(",", "."))
        credito = float(input("Digite o saldo do Crédito: ").replace(",", "."))
        self.add_balanco(value, credito)

    def conta_corrente(self):
        print("---------------------------------------")
        print("1 - Adicionar / Retirar Saldo")
        print("---------------------------------------")
        print("2 - Adicionar Compra")
        print("---------------------------------------")
        print("3 - Verificar Extrato")
        print("---------------------------------------")
        print("4 - Sair")
        print("---------------------------------------")
        escolha = int(input("O que deseja fazer: "))
        if escolha == 1:
            self.add_contas_corrente()
        elif escolha == 2:
            compra = input("Digite o nome da compra: ")
            valor = float(input("Digite o valor da compra: R$"))
            self.adiciona_compra_corrente(compra, valor)
        elif escolha == 3:
            self.mostra_extrato()
        else:
            pass

    def add_contas_corrente(self):
        print("---------------------------------------")
        print("1 - Adicionar Saldo")
        print("---------------------------------------")
        print("2 - Retirar Saldo")
        print("---------------------------------------")
        print("3 - Sair")
        print("---------------------------------------")
        escolha = int(input("O que deseja fazer: "))
        if escolha == 1:
            valor = float(input("Digite o valor: R$").replace(",", "."))
            self.adiciona_corrente(valor)
        elif escolha == 2:
            if self.balanco[self._banco][0] <= 0:
                print("Saldo Indisponível")
            else:
                valor = float(input("Digite o valor: R$").replace(",", "."))
                self.desconta_corrente(valor)
        else:
            pass

    def add_contas_credito(self):
        print("---------------------------------------")
        print("1 - Adicionar Conta Parcelada")
        print("---------------------------------------")
        print("2 - Adicionar Conta À Vista")
        print("---------------------------------------")
        print("3 - Sair")
        print("---------------------------------------")
        escolha = int(input("O que deseja fazer: "))
        if escolha == 1:
            conta = input("Digite o nome da compra: ")
            valor = float(input("Digite o valor: R$").replace(",", "."))
            parcelas = int(input("Quantidade de parcelas: "))
            self.compra_parcelada(conta, valor, parcelas)
        elif escolha == 2:
            conta = input("Digite o nome da compra: ")
            valor = float(input("Digite o valor: R$").replace(",", "."))
            self.add_contas_lista(conta, valor)
        else:
            pass

    def conta_credito(self):
        print("---------------------------------------")
        print("1 - Adicionar Contas À Vista e Parceladas")
        print("---------------------------------------")
        print("2 - Saldo do Crédito")
        print("---------------------------------------")
        print("3 - Ver as contas")
        print("---------------------------------------")
        print("4 - Sair")
        print("---------------------------------------")
        escolha = int(input("O que deseja fazer: "))
        if escolha == 1:
            if self.balanco[self._banco][1] < 0:
                print("Não há crédito !")
            else:
                self.add_contas_credito()
        elif escolha == 2:
            print(f"R${self.balanco[self._banco][1]}")
        elif escolha == 3:
            self.show_contas_lista()
        else:
            pass

    #################### MENUS ACIMA ##########################################

    def add_balanco(self, value, credito):
        self._value = value
        self._credito = credito
        self.balanco[self._banco] = [self._value, self._credito]

    def desconta_corrente(self, valor):
        self.contas_corrente.append(("Retirada", f"R${valor}"))
        self.balanco[self._banco][0] -= valor

    def adiciona_corrente(self, valor):
        self.contas_corrente.append(("Adicionou", f"R${valor}"))
        self.balanco[self._banco][0] += valor

    def adiciona_compra_corrente(self, compra, valor):
        self.balanco[self._banco][0] -= valor
        self.contas_corrente.append((compra, valor))

    def mostra_extrato(self):
        if len(self.contas_corrente) == 0:
            print("Não há movimento !")
        else:
            print("NOME DA COMPRA, VALOR")
            for i in self.contas_corrente:
                print(i)
        print(f"C/C: R${self.balanco[self._banco][0]}")

    def add_contas_lista(self, conta, valor):
        self.contas_credito.append((conta, valor, 1))
        self.balanco[self._banco][1] -= valor
        print(f"R${self.balanco[self._banco][1]}")

    def compra_parcelada(self, conta, valor, parcelas):
        valor_parcelado = valor / parcelas
        self.parceladas.append((conta, valor_parcelado, parcelas))
        self.contas_credito.append(self.parceladas)
        self.balanco[self._banco][1] -= valor
        print(f"R${self.balanco[self._banco][1]}")

    def show_contas_lista(self):
        if len(self.contas_credito) == 0:
            print("Não há contas !")
        else:
            print("NOME DA CONTA, VALOR, PARCELAS")
            for i in self.contas_credito:
                print(i)
