from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

from .models import *

#POUPANÇA
class AcionaPoupanca (ModelForm):
    class Meta:
        model = Conta
        fields = '__all__'
        exclude = ['corrente', 'credito', 'poupanca', 'banco']


class ResgataPoupanca (ModelForm):
    class Meta:
        model = Conta
        fields = "__all__"
        exclude = ['corrente', 'credito', 'poupanca', 'banco']

class TransferePoupanca (ModelForm):
    class Meta:
        model = Conta
        fields = "__all__"

#CONTA CORRENTE
class DepositaCorrente (ModelForm):
    class Meta:
        model = Conta
        fields = "__all__"
        exclude = ['corrente','credito', 'poupanca', 'banco']

class RetiraCorrente (ModelForm):
    class Meta:
        model = Conta
        fields = "__all__"
        exclude = ['corrente','credito', 'poupanca', 'banco']

class TransfereCorrente (ModelForm):
    class Meta:
        model = Conta
        fields = "__all__"
        exclude = ['corrente','credito', 'poupanca', 'banco']

class CompraCorrente (ModelForm):
    class Meta:
        model = Conta
        fields = "__all__"
        exclude = ['corrente', 'credito', 'poupanca', 'banco']

#CONTA CRÉDITO
class ParcelouCredito (ModelForm):
    class Meta:
        model = Conta
        fields = "__all__"
        exclude = ['corrente', 'credito', 'poupanca', 'banco']

class PagouCredito (ModelForm):
    class Meta:
        model = Conta
        fields = "__all__"
        exclude = ['corrente', 'credito', 'poupanca', 'banco']

#EXTRATO
class ColocaExtrato (ModelForm):
    class Meta:
        model = Extrato
        fields = "__all__"
        exclude = ['parcelas', 'valor_parcelado', 'meses']

class CompraExtrato (ModelForm):
    class Meta:
        model = Extrato
        fields = "__all__"
        exclude = ['valor_parcelado', 'meses']

class PagouExtrato (ModelForm):
    class Meta:
        model = Extrato
        fields = "__all__"
        exclude = ['valor', 'meses']