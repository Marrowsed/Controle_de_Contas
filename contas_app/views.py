from django.db.models import F
from django.shortcuts import render, redirect
from .models import *
from .form import AcionaPoupanca, ResgataPoupanca, ColocaExtrato, DepositaCorrente, RetiraCorrente, TransfereCorrente, \
    CompraCorrente, CompraExtrato


def banco(request, pk):
    nome = Cliente.objects.all().get(user=request.user)
    conta = Conta.objects.all().get(id=pk)

    ctx = {'nome': nome, 'conta': conta}
    return render(request, 'banco.html', ctx)


def index(request):
    conta = Conta.objects.all()

    ctx = {'conta': conta}

    return render(request, 'index.html', ctx)

#### POUPANÇA
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
        form_extrato = ColocaExtrato(request.POST)
        if form_aciona.is_valid() and form_extrato.is_valid():
            ext = form_extrato
            valor_acionado = ext['valor'].value()
            Conta.objects.filter(poupanca=savings).update(corrente=F('corrente')-valor_acionado)
            Poupanca.objects.filter(id=pk).update(valor=F('valor')+valor_acionado)
            ext.save()
            return redirect(f'/banco/poupanca/{pk}')


    form_aciona = AcionaPoupanca(
        initial={'cliente': conta.cliente.id}
    )
    form_extrato = ColocaExtrato(
        initial={'acoes': 'Aplicou', 'conta': conta.id}
    )
    ctx = {'conta_pag': conta, 'nome': nome, 'poupanca': savings, 'form_aciona': form_aciona, 'form_extrato': form_extrato}
    return render(request, 'a_poupanca/aplicar.html', ctx)

def resgatar(request, pk):
    nome = Cliente.objects.all().get(user=request.user)
    savings = Poupanca.objects.all().get(id=pk)
    conta = Conta.objects.all().get(poupanca=savings)
    resgate = conta

    if request.method == 'POST':
        form_resgata = ResgataPoupanca(request.POST)
        form_extrato = ColocaExtrato(request.POST)
        if form_resgata.is_valid() and form_extrato.is_valid():
            ext = form_extrato
            valor_resgatado = ext['valor'].value()
            Conta.objects.filter(poupanca=savings).update(corrente=F('corrente') + valor_resgatado)
            Poupanca.objects.filter(id=pk).update(valor=F('valor') - valor_resgatado)
            ext.save()
            return redirect(f'/banco/poupanca/{pk}')

    form_resgata = ResgataPoupanca(
        initial={'cliente': resgate.cliente.id}
    )
    form_extrato = ColocaExtrato(
        initial={'acoes': 'Resgatou', 'conta': conta.id}
    )
    ctx = {'conta_pag': conta, 'nome': nome, 'poupanca': savings, 'form_resgata': form_resgata, 'form_extrato': form_extrato}
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

####CORRENTE
def corrente(request,pk):
    nome = Cliente.objects.all().get(user=request.user)
    conta = Conta.objects.all().get(id=pk)

    ctx = {'conta': conta, 'nome': nome}

    return render(request, 'corrente.html', ctx)

def comprou(request,pk):
    nome = Cliente.objects.all().get(user=request.user)
    conta = Conta.objects.all().get(id=pk)
    if request.method == "POST":
        form_compra = CompraCorrente(request.POST, instance=conta)
        form_extrato = CompraExtrato(request.POST)
        if form_compra.is_valid() and form_extrato.is_valid():
            ext = form_extrato
            valor_comprado = ext['valor'].value()
            Conta.objects.filter(id=pk).update(corrente=F('corrente') - valor_comprado)
            ext.save()
            return redirect(f'/corrente/{pk}')

    form_compra = CompraCorrente(
        initial={'cliente': conta.cliente.id}
    )
    form_extrato = CompraExtrato(
        initial={'acoes': 'Comprou', 'conta': pk}
    )

    ctx = {'conta': conta, 'nome': nome, "form_compra": form_compra, "form_extrato": form_extrato}

    return render(request, 'a_corrente/comprou.html', ctx)

def depositou(request,pk):
    nome = Cliente.objects.all().get(user=request.user)
    conta = Conta.objects.all().get(id=pk)

    if request.method == "POST":
        form_deposita = DepositaCorrente(request.POST)
        form_extrato = ColocaExtrato(request.POST)
        if form_deposita.is_valid() and form_extrato.is_valid():
            ext = form_extrato
            valor_depositado = ext['valor'].value()
            Conta.objects.filter(id=pk).update(corrente=F('corrente') + valor_depositado)
            ext.save()
            return redirect(f'/corrente/{pk}')

    form_deposita = DepositaCorrente(
        initial={'cliente': conta.cliente.id}
    )
    form_extrato = ColocaExtrato(
        initial={'acoes': 'Depositou', 'conta': pk}
    )


    ctx = {'conta': conta, 'nome': nome, "form_deposita": form_deposita, "form_extrato": form_extrato}

    return render(request, 'a_corrente/depositou.html', ctx)

def pix(request,pk):
    nome = Cliente.objects.all().get(user=request.user)
    conta = Conta.objects.all().get(id=pk)

    if request.method == "POST":
        form_pix = TransfereCorrente(request.POST)
        form_extrato = ColocaExtrato(request.POST)
        if form_pix.is_valid() and form_extrato.is_valid():
            ext = form_extrato
            valor_transferido = ext['valor'].value()
            Conta.objects.filter(id=pk).update(corrente=F('corrente') - valor_transferido)
            ext.save()
            return redirect(f'/corrente/{pk}')

    form_pix = TransfereCorrente(
        initial={'cliente': conta.cliente.id}
    )
    form_extrato = ColocaExtrato(
        initial={'acoes': 'Transferiu', 'conta': pk}
    )

    ctx = {'conta': conta, 'nome': nome, "form_pix": form_pix, "form_extrato": form_extrato}

    return render(request, 'a_corrente/pix.html', ctx)

def retirou(request,pk):
    nome = Cliente.objects.all().get(user=request.user)
    conta = Conta.objects.all().get(id=pk)

    if request.method == "POST":
        form_retira = RetiraCorrente(request.POST)
        form_extrato = ColocaExtrato(request.POST)
        if form_retira.is_valid() and form_extrato.is_valid():
            ext = form_extrato
            valor_retirado = ext['valor'].value()
            Conta.objects.filter(id=pk).update(corrente=F('corrente') - valor_retirado)
            ext.save()
            return redirect(f'/corrente/{pk}')

    form_retira = RetiraCorrente(
        initial={'cliente': conta.cliente.id}
    )
    form_extrato = ColocaExtrato(
        initial={'acoes': 'Retirou', 'conta': pk}
    )

    ctx = {'conta': conta, 'nome': nome, "form_retira": form_retira, "form_extrato": form_extrato}

    return render(request, 'a_corrente/retirou.html', ctx)
