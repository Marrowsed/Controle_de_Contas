class Poupanca:

    def __init__(self):
        self.saldo = 0
        self.extrato = []

    def aplicar(self, valor):
        self.saldo += valor
        self.extrato.append(("Aplicou", f"R$ {valor}"))

    def resgatar(self, resgate):
        self.saldo -= resgate
        self.extrato.append(("Resgatou", f"R${resgate}"))

    def mostra_extrato(self):
        if len(self.extrato) == 0:
            print("Não há movimento !")
        else:
            for e in self.extrato:
                print(e)
        print(f"R$ {self.saldo}")

    def menu(self):
        print("---------------------------------------")
        print("1 - Adicionar Saldo")
        print("---------------------------------------")
        print("2 - Resgatar Saldo")
        print("---------------------------------------")
        print("3 - Verificar Extrato")
        print("---------------------------------------")
        print("4 - Sair")
        print("---------------------------------------")
        escolha = int(input("O que deseja fazer: "))
        if escolha == 1:
            valor = float(input("Digite o valor que quer aplicar: R$"))
            self.aplicar(valor)
        elif escolha == 2:
            if self.saldo < 0:
                print("Não há saldo !")
            else:
                valor = float(input("Digite o valor que quer resgatar: R$"))
                self.resgatar(valor)
        elif escolha == 3:
            self.mostra_extrato()
        else:
            pass
