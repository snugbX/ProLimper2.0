from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from clientes.models import Vendedor
import re
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def vendedores(request):
	if request.method == "GET":
		lista_vendedores = Vendedor.objects.all()
		return render(request, 'Vendedor/vendedor.html' , {'vendedores': lista_vendedores})
	elif request.method == "POST":
		nome = request.POST.get('nome')
		CPF = request.POST.get('cpf')
		email = request.POST.get('email')
		telefone = request.POST.get('telefone')
		Whatsapp = request.POST.get('whatsapp')
		loja = request.POST.get('loja')
		CNPJ = request.POST.get('cnpj')

		if Whatsapp == '1':
			Whatsapp = True
		else: 
			Whatsapp = False

		if not re.fullmatch(re.compile(r'([0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2})+'), CPF):
			messages.error(request, 'CPF invalido!!')
			return render(request, 'Vendedor/vendedor.html', {'nome': nome, 'email': email,'telefone': telefone , 'loja': loja, 'CNPJ': CNPJ})

		if not re.fullmatch(re.compile(r'([0-9]{2}\.?[0-9]{3}\.?[0-9]{3}\/?[0-9]{4}\-?[0-9]{2})+'), CNPJ):
			messages.error(request, 'CNPJ invalido!!')
			return render(request, 'Vendedor/vendedor.html', {'nome': nome,'cpf': CPF, 'email': email,'telefone': telefone, 'loja': loja})

		vendedor = Vendedor.objects.filter(CPF=CPF)

		if vendedor.exists():
			messages.error(request, 'Cliente já existe com esse CPF!!')
			return render(request, 'Vendedor/vendedor.html', {'nome': nome, 'email': email,'telefone': telefone, 'loja': loja, 'CNPJ': CNPJ})


		vendedor = Vendedor(
			nome = nome,
			CPF = CPF,
			email = email,
			telefone = telefone,
			whatsapp = Whatsapp,
			loja = loja,
			CNPJ = CNPJ,
		)

		vendedor.save()
		return redirect('vendedor')

def delete_vendedor(request, pk):
	del_Vendedor = get_object_or_404(Vendedor, pk=pk)
	del_Vendedor.delete()

	messages.info(request, "Vendedor deletado com sucesso!!")
	return redirect('vendedor')

@csrf_exempt
def update_vendedor(request, pk):

	up_vendedor = get_object_or_404(Vendedor, pk=pk)

	id_ven = up_vendedor.id
	nome = up_vendedor.nome
	CPF = up_vendedor.CPF
	email = up_vendedor.email
	telefone = up_vendedor.telefone
	Whatsapp = up_vendedor.whatsapp
	loja = up_vendedor.loja
	CNPJ = up_vendedor.CNPJ

	if (request.method == "POST"):

		nome = request.POST.get('nome')
		CPF = request.POST.get('cpf')
		email = request.POST.get('email')
		telefone = request.POST.get('telefone')
		Whatsapp = request.POST.get('whatsapp')
		loja = request.POST.get('loja')
		CNPJ = request.POST.get('cnpj')

		if Whatsapp == '1':
			Whatsapp = True
		else: 
			Whatsapp = False


		if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
			messages.error(request, 'Email invalido!!')
			return render(request, 'Vendedor/vendedor.html', {'nome': nome,'CPF': CPF,'telefone': telefone , 'loja': loja, 'CNPJ': CNPJ})

		if not re.fullmatch(re.compile(r'([0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2})+'), CPF):
			messages.error(request, 'CPF invalido!!')
			return render(request, 'Vendedor/vendedor.html', {'nome': nome, 'email': email,'telefone': telefone , 'loja': loja, 'CNPJ': CNPJ})

		if not re.fullmatch(re.compile(r'([0-9]{2}\.?[0-9]{3}\.?[0-9]{3}\/?[0-9]{4}\-?[0-9]{2})+'), CNPJ):
			messages.error(request, 'CNPJ invalido!!')
			return render(request, 'Vendedor/vendedor.html', {'nome': nome,'CPF': CPF, 'email': email,'telefone': telefone, 'loja': loja})

		vendedor = Vendedor.objects.filter(CPF=CPF).exclude(pk=pk)

		if vendedor.exists():
			messages.error(request, 'Cliente já existe com esse CPF!!')
			return render(request, 'Vendedor/vendedor.html', {'nome': nome, 'email': email,
				'telefone': telefone, 'loja': loja, 'CNPJ': CNPJ})

		vendedor = Vendedor.objects.get(pk=pk)
		
		vendedor.nome = nome
		vendedor.CPF = CPF
		vendedor.email = email
		vendedor.telefone = telefone
		vendedor.whatsapp = Whatsapp
		vendedor.loja = loja
		vendedor.CNPJ = CNPJ

		vendedor.save()
		return redirect('vendedor')
	else:
		return render(request, 'Vendedor/att.vendedor.html', {'id': id_ven, 'nome': nome, 'CPF': CPF,
		 'email': email,'telefone': telefone, 'whatsapp': Whatsapp, 'loja': loja, 'CNPJ': CNPJ})
		

