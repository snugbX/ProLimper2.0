# Generated by Django 4.1 on 2023-01-23 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='complemento',
            field=models.CharField(max_length=255, null=True),
        ),
    ]