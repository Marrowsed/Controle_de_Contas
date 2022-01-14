from django.db.models import F
from django.shortcuts import render, redirect
from .models import *
from .form import AcionaPoupanca, ResgataPoupanca, ColocaExtrato, DepositaCorrente, RetiraCorrente, TransfereCorrente, \
    CompraCorrente, CompraExtrato, ParcelouCredito, PagouCredito, PagouExtrato


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

#####CRÉDITO
def credito(request, pk):
    nome = Cliente.objects.all().get(user=request.user)
    conta = Conta.objects.all().get(id=pk)
    extrato = conta.extrato_set.all()
    fatura = 0
    parcelaf = 0
    for valor in extrato:
        valorp = valor.valor_parcelado
        valorf = valor.valor
        fatura += valorp
        parcelaf += valorf


    ctx = {'conta': conta, 'nome': nome, 'fatura': fatura, 'parceladas': parcelaf}

    return render(request, 'credito.html', ctx)

def parcelou(request, pk):
    nome = Cliente.objects.all().get(user=request.user)
    conta = Conta.objects.all().get(id=pk)
    extrato = conta.extrato_set.all()
    fatura = 0
    for valor in extrato:
        valorf = valor.valor_parcelado
        fatura += valorf

    if request.method == "POST":
        form_parcela = ParcelouCredito(request.POST)
        form_extrato = CompraExtrato(request.POST)
        if form_parcela.is_valid() and form_extrato.is_valid():
            ext = form_extrato
            valor_retirado = ext['valor'].value()
            Conta.objects.filter(id=pk).update(credito=F('credito') - valor_retirado)
            ext.save()
            return redirect(f'/credito/{pk}')

    form_parcela = ParcelouCredito(
        initial={'cliente': conta.cliente.id}
    )
    form_extrato = CompraExtrato(
        initial={'acoes': 'Parcelou', 'conta': pk}
    )


    ctx = {'conta': conta, 'nome': nome, 'fatura': fatura, 'form_parcela': form_parcela, 'form_extrato': form_extrato}

    return render(request, 'a_credito/parcelou.html', ctx)

def parceladas(request, pk):
    nome = Cliente.objects.all().get(user=request.user)
    conta = Conta.objects.all().get(id=pk)
    extrato = conta.extrato_set.all()
    fatura = 0
    for valor in extrato:
        valorf = valor.valor_parcelado
        fatura += valorf


    ctx = {'conta': conta, 'nome': nome, 'fatura': fatura, 'extrato': extrato}

    return render(request, 'a_credito/parceladas.html', ctx)

def pagou(request, pk):
    nome = Cliente.objects.all().get(user=request.user)
    extrato = Extrato.objects.all().get(id=pk)
    conta = Conta.objects.all().get(extrato=extrato)
    form_pagou = PagouCredito(instance=conta)
    par_resto = extrato.parcelas

    if request.method == "POST":
        form_pagou = PagouCredito(request.POST, instance=conta)
        form_extrato = PagouExtrato(request.POST, instance=extrato)
        if form_pagou.is_valid() and form_extrato.is_valid():
            ext = form_extrato
            valor_pago = ext['valor_parcelado'].value()
            parcelas = ext['parcelas'].value()
            if par_resto >= int(parcelas):
                Extrato.objects.filter(id=pk).update(parcelas=F('parcelas') - parcelas)
                Extrato.objects.filter(id=pk).update(valor=F('valor') - (float(valor_pago) * int(parcelas)))
                Extrato.objects.filter(id=pk).update(valor_parcelado=F('valor_parcelado') + (float(valor_pago) * int(parcelas)))
                Conta.objects.filter(extrato=extrato).update(credito=F('credito') - (float(valor_pago) * int(parcelas)))
                ext.save()
            elif par_resto < 1:
                extrato.delete()
            else:
                raise ValueError("ACIMA")
            return redirect(f'/credito/{conta.id}')

    form_extrato = PagouExtrato(
        initial={'acoes': 'Pagou', 'conta': extrato.conta.id, 'obs': extrato.obs, 'valor_parcelado': extrato.valor_parcelado}
    )

    ctx = {'conta': conta, 'nome': nome, 'form_pagou': form_pagou, 'form_extrato': form_extrato}

    return render(request, 'a_credito/pagou.html', ctx)