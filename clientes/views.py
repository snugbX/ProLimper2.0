from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Cliente
import re
from django.views.decorators.csrf import csrf_exempt
from django.urls import clear_url_caches


# Create your views here.

def clientes(request):
	if request.method == "GET":
		lista_clientes = Cliente.objects.all()
		return render(request, 'Cliente/clientes.html' , {'clientes': lista_clientes})
	elif request.method == "POST":
		nome = request.POST.get('nome')
		CPF = request.POST.get('cpf')
		CNPJ = request.POST.get('cnpj')
		telefone = request.POST.get('telefone')
		Whatsapp = request.POST.get('whatsapp')
		email = request.POST.get('email')
		endereco = request.POST.get('logradouro')
		numero_Casa = request.POST.get('numero')
		bairro = request.POST.get('bairro')
		complemento = request.POST.get('complemento')
		CEP = request.POST.get('cep')

		if numero_Casa=='':
			numero_Casa = None

		if Whatsapp == '1':
			Whatsapp = True
		else: 
			Whatsapp = False

		if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
			messages.error(request, 'Email invalido!!')
			return render(request, 'Cliente/clientes.html', {'nome': nome, 'CPF': CPF,
			'CNPJ': CNPJ, 'telefone': telefone ,'Whatsapp': Whatsapp, 'endereco': endereco,
			'bairro': bairro,'numero_Casa': numero_Casa,'complemento': complemento,'CEP': CEP, })

		if not re.fullmatch(re.compile(r'([0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2})+'), CPF):
			messages.error(request, 'CPF invalido!!')
			return render(request, 'Cliente/clientes.html', {'nome': nome, 'email': email,
			'CNPJ': CNPJ, 'telefone': telefone ,'Whatsapp': Whatsapp, 'endereco': endereco,
			'bairro': bairro,'numero_Casa': numero_Casa,'complemento': complemento,'CEP': CEP, })

		'''if not re.fullmatch(re.compile(r'([0-9]{2}\.?[0-9]{3}\.?[0-9]{3}\/?[0-9]{4}\-?[0-9]{2})+'), CNPJ):
			messages.error(request, 'CNPJ invalido!!')
			return render(request, 'Cliente/clientes.html', {'nome': nome, 'email': email,
			'CNPJ': CNPJ, 'telefone': telefone ,'Whatsapp': Whatsapp, 'endereco': endereco,
			'bairro': bairro,'numero_Casa': numero_Casa,'complemento': complemento,'CEP': CEP, })'''

		cliente = Cliente.objects.filter(CPF=CPF)

		if cliente.exists():
			messages.error(request, 'Cliente já existe com esse CPF!!')
			return render(request, 'Cliente/clientes.html', {'nome': nome, 'email': email,
			'CNPJ': CNPJ, 'telefone': telefone ,'Whatsapp': Whatsapp, 'endereco': endereco,
			'bairro': bairro,'numero_Casa': numero_Casa,'complemento': complemento,'CEP': CEP, })


		cliente = Cliente(
			nome = nome,
			CPF = CPF,
			CNPJ = CNPJ,
			telefone = telefone,
			Whatsapp = Whatsapp,
			email = email,
			endereco = endereco,
			numero_Casa = numero_Casa,
			bairro = bairro,
			complemento = complemento,
			CEP = CEP
		)

		cliente.save()
		return redirect('clientes')


def delete_cliente(request, pk):
    del_Cliente = get_object_or_404(Cliente, pk=pk)
    del_Cliente.delete()

    messages.info(request, "Cliente deletado com sucesso!!")
    return redirect('clientes')

@csrf_exempt
def update_cliente(request, pk):
	up_Cliente = get_object_or_404(Cliente, pk=pk)

	id_cli = up_Cliente.id
	nome = up_Cliente.nome
	CPF = up_Cliente.CPF
	CNPJ = up_Cliente.CNPJ
	telefone = up_Cliente.telefone
	Whatsapp = up_Cliente.Whatsapp
	email = up_Cliente.email
	endereco = up_Cliente.endereco
	bairro = up_Cliente.bairro
	numero_Casa = up_Cliente.numero_Casa
	complemento = up_Cliente.complemento
	CEP = up_Cliente.CEP

	if (request.method == "POST"):
		nome = request.POST.get('nome')
		CPF = request.POST.get('cpf')
		CNPJ = request.POST.get('cnpj')
		telefone = request.POST.get('telefone')
		Whatsapp = request.POST.get('whatsapp')
		email = request.POST.get('email')
		endereco = request.POST.get('logradouro')
		numero_Casa = request.POST.get('numero')
		bairro = request.POST.get('bairro')
		complemento = request.POST.get('complemento')
		CEP = request.POST.get('cep')

		if numero_Casa=='':
			numero_Casa = None

		if Whatsapp == '1':
			Whatsapp = True
		else: 
			Whatsapp = False

		if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
			messages.error(request, 'Email invalido!!')
			return render(request, 'Cliente/att_cliente.html', {'nome': nome, 'CPF': CPF,
			'CNPJ': CNPJ, 'telefone': telefone ,'Whatsapp': Whatsapp, 'endereco': endereco,
			'bairro': bairro,'numero_Casa': numero_Casa,'complemento': complemento,'CEP': CEP, })

		if not re.fullmatch(re.compile(r'([0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2})+'), CPF):
			messages.error(request, 'CPF invalido!!')
			return render(request, 'Cliente/att_cliente.html', {'nome': nome, 'email': email,
			'CNPJ': CNPJ, 'telefone': telefone ,'Whatsapp': Whatsapp, 'endereco': endereco,
			'bairro': bairro,'numero_Casa': numero_Casa,'complemento': complemento,'CEP': CEP, })

		cliente = Cliente.objects.filter(CPF=CPF).exclude(pk=pk)

		if cliente.exists():
			messages.error(request, 'Cliente já existe com esse CPF!!')
			return render(request, 'Cliente/att_cliente.html', {'nome': nome, 'email': email,
			'CNPJ': CNPJ, 'telefone': telefone ,'Whatsapp': Whatsapp, 'endereco': endereco,
			'bairro': bairro,'numero_Casa': numero_Casa,'complemento': complemento,'CEP': CEP, })

		cliente  = Cliente.objects.get(pk=pk)

		cliente.nome = nome
		cliente.CPF = CPF
		cliente.CNPJ = CNPJ
		cliente.telefone = telefone
		cliente.Whatsapp = Whatsapp
		cliente.email = email
		cliente.endereco = endereco
		cliente.numero_Casa = numero_Casa
		cliente.bairro = bairro
		cliente.complemento = complemento
		cliente.CEP = CEP
		

		cliente.save()
		return redirect('clientes')
	else:
		return render(request, 'Cliente/att_cliente.html', {'id': id_cli, 'nome': nome, 'CPF': CPF,
			'CNPJ': CNPJ, 'telefone': telefone ,'Whatsapp': Whatsapp, 'email': email, 'endereco': endereco,
			'bairro': bairro,'numero_Casa': numero_Casa,'complemento': complemento,'CEP': CEP})

