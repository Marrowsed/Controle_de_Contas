from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

from .models import *


class AcionaPoupanca (ModelForm):
    class Meta:
        model = Conta
        fields = '__all__'
        exclude = ['credito', 'poupanca', 'banco']


class ResgataPoupanca (ModelForm):
    class Meta:
        model = Conta
        fields = "__all__"
        exclude = ['credito', 'poupanca', 'banco']

class TransferePoupanca (ModelForm):
    class Meta:
        model = Conta
        fields = "__all__"

