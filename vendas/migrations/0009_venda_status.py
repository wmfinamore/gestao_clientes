# Generated by Django 2.2.13 on 2020-06-28 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0008_auto_20200627_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='status',
            field=models.CharField(choices=[('AB', 'Aberta'), ('FC', 'Fechada'), ('PC', 'Processando'), ('DC', 'Desconhecido')], default='DC', max_length=2),
        ),
    ]