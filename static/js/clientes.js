function exibir_form(tipo){
	lista_cliente = document.getElementById('lista-cliente')
	add_cliente = document.getElementById('adicionar-cliente')
	att_cliente = document.getElementById('atualiza-cliente')
	if (tipo == "1") {
		add_cliente.style.display = "none"
		att_cliente.style.display = "none"
		lista_cliente.style.display = "block"
		
	}else if (tipo == "2") {
		att_cliente.style.display = "none"
		lista_cliente.style.display = "none"
		add_cliente.style.display = "block"
		
	}
}

/*
function attCliente(id){
	csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value

	data = new FormData()
	data.append('id_cliente', id)

	fetch("./att_Cliente/",{
		method: "POST",
		headers: {'X-CSRFToken': csrf_token,
		},
		body: data

	}).then(function(result){
		return result.json()
	}).then(function(data){
		console.log(data)
	})
}*/

