# Generated by Django 4.1 on 2023-01-30 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_vendedor_cnpj_vendedor_email_vendedor_telefone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='numero_Casa',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
