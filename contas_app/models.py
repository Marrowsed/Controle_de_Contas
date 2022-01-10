from django.db import models
from django.contrib.auth.models import User


class Banco(models.Model):
    nome = models.CharField(max_length=200)
    agencia = models.IntegerField(null=True)
    numero_conta_corrente = models.IntegerField(null=True)

    def __str__(self):
        return self.nome


class Poupanca(models.Model):
    numero_conta_poupanca = models.IntegerField(null=True)
    valor = models.FloatField(null=True)

    def __str__(self):
        return str(self.numero_conta_poupanca)


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200, null=True)
    sobrenome = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"


class Conta(models.Model):
    corrente = models.FloatField(null=True)
    credito = models.FloatField(null=True)
    banco = models.ForeignKey(Banco, null=True, on_delete=models.CASCADE)
    poupanca = models.ForeignKey(Poupanca, null=True, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"Conta do Banco: {self.banco.nome}"


class Extrato(models.Model):
    ACOES = (
        ("Aplicou", "Aplicou"),
        ("Resgatou", "Resgatou"),
        ("Comprou", "Comprou"),
        ("Parcelou", "Parcelou"),
        ("Depositou", "Depositou"),
        ("Retirou", "Retirou"),
        ("Transferiu", "Transferiu"),
    )
    conta = models.ForeignKey(Conta, null=True, on_delete=models.SET_NULL)
    acoes = models.CharField(max_length=200, null=True, choices=ACOES)
    valor = models.FloatField(null=True)
    obs = models.CharField(max_length=200, null=True)
    parcelas = models.IntegerField(null=True, default=1)

    def __str__(self):
        return f"{self.obs} : R${str(self.valor)}"
