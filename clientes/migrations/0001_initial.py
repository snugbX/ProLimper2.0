# Generated by Django 4.1 on 2023-01-19 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarrinhoServicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('CPF', models.CharField(max_length=20, unique=True)),
                ('CNPJ', models.CharField(blank=True, max_length=20, null=True)),
                ('telefone', models.CharField(max_length=30)),
                ('Whatsapp', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=255, null=True)),
                ('endereco', models.CharField(max_length=255)),
                ('bairro', models.CharField(max_length=255)),
                ('numero_Casa', models.IntegerField(blank=True, null=True)),
                ('CEP', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Loja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, null=True)),
                ('CNPJ', models.CharField(blank=True, max_length=20, null=True)),
                ('telefone', models.CharField(max_length=30)),
                ('whatsapp', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Servicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descricao', models.CharField(max_length=400)),
                ('Valor', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('CPF', models.CharField(max_length=20, unique=True)),
                ('loja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.loja')),
            ],
        ),
        migrations.CreateModel(
            name='OrdemDeServicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Valor_Total', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('data_Solicitacao', models.DateTimeField(auto_now_add=True)),
                ('data_Execucao', models.DateField(blank=True, null=True)),
                ('Status', models.CharField(choices=[('I', 'iniciado'), ('F', 'Finalizado'), ('N_I', 'Não iniciado'), ('C_P', 'Com problema')], max_length=4)),
                ('Carrinho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.carrinhoservicos')),
                ('Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
                ('Vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.vendedor')),
            ],
        ),
        migrations.AddField(
            model_name='carrinhoservicos',
            name='Servicos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.servicos'),
        ),
    ]