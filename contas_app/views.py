from django.db.models import F
from django.shortcuts import render, redirect
from .models import *
from .form import AcionaPoupanca, ResgataPoupanca


def banco(request, pk):
    nome = Cliente.objects.all().get(user=request.user)
    conta = Conta.objects.all().get(id=pk)

    ctx = {'nome': nome, 'conta': conta}
    return render(request, 'banco.html', ctx)


def index(request):
    conta = Conta.objects.all()

    ctx = {'conta': conta}

    return render(request, 'index.html', ctx)


def poupanca(request, pk):
    nome = Cliente.objects.all().get(user=request.user)
    savings = Poupanca.objects.all().get(id=pk)
    conta = Conta.objects.all().get(poupanca=savings)

    ctx = {'conta': conta, 'nome': nome, 'poupanca': savings}

    return render(request, 'poupanca.html', ctx)

def aplicar(request, pk):
    nome = Cliente.objects.all().get(user=request.user)
    savings = Poupanca.objects.all().get(id=pk)
    conta = Conta.objects.all().get(poupanca=savings)
    if request.method == 'POST':
        form_aciona = AcionaPoupanca(request.POST)
        if form_aciona.is_valid():
            pp = form_aciona
            valor_acionado = pp['corrente'].value()
            Conta.objects.filter(poupanca=savings).update(corrente=F('corrente')-valor_acionado)
            Poupanca.objects.filter(id=pk).update(valor=F('valor')+valor_acionado)
            return redirect(f'/banco/poupanca/{pk}')


    form_aciona = AcionaPoupanca(
        initial={'poupanca': conta.poupanca.numero_conta_poupanca, 'cliente': conta.cliente.nome}
    )
    ctx = {'conta': conta, 'nome': nome, 'poupanca': savings, 'form_aciona': form_aciona}
    return render(request, 'a_poupanca/aplicar.html', ctx)

def resgatar(request, pk):
    nome = Cliente.objects.all().get(user=request.user)
    savings = Poupanca.objects.all().get(id=pk)
    conta = Conta.objects.all().get(poupanca=savings)
    if request.method == 'POST':
        form_resgata = ResgataPoupanca(request.POST)
        if form_resgata.is_valid():
            pr = form_resgata
            valor_resgatado = pr['corrente'].value()
            Conta.objects.filter(poupanca=savings).update(corrente=F('corrente') + valor_resgatado)
            Poupanca.objects.filter(id=pk).update(valor=F('valor') - valor_resgatado)
            return redirect(f'/banco/poupanca/{pk}')

    form_resgata = ResgataPoupanca(
        initial={'poupanca': conta.poupanca.numero_conta_poupanca, 'cliente': conta.cliente.nome}
    )
    ctx = {'conta': conta, 'nome': nome, 'poupanca': savings, 'form_resgata': form_resgata}
    return render(request, 'a_poupanca/resgatar.html', ctx)

def transferir(request, pk):
    nome = Cliente.objects.all().get(user=request.user)
    savings = Poupanca.objects.all().get(id=pk)
    conta = Conta.objects.all().get(poupanca=savings)
    if request.method == 'POST':
        form_transfere = AcionaPoupanca(request.POST)
        if form_transfere.is_valid():
            pt = form_transfere
            valor_acionado = pt['corrente'].value()
            Poupanca.objects.filter(id=pk).update(valor=F('valor') + valor_acionado)
            return redirect(f'/banco/poupanca/{pk}')

    form_transfere = AcionaPoupanca(
        initial={'poupanca': conta.poupanca.numero_conta_poupanca, 'cliente': conta.cliente.nome}
    )
    ctx = {'conta': conta, 'nome': nome, 'poupanca': savings, 'form_transfere': form_transfere}
    return render(request, 'a_poupanca/transferir.html', ctx)


def credito(request, pk):
    nome = Cliente.objects.all().get(user=request.user)
    conta = Conta.objects.all().get(id=pk)

    ctx = {'conta': conta, 'nome': nome}

    return render(request, 'credito.html', ctx)


def corrente(request,pk):
    nome = Cliente.objects.all().get(user=request.user)
    conta = Conta.objects.all().get(id=pk)

    ctx = {'conta': conta, 'nome': nome}

    return render(request, 'corrente.html', ctx)
