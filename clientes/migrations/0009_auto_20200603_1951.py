# Generated by Django 2.2.10 on 2020-06-03 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0008_venda_nfe_emitida'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='produtos',
        ),
        migrations.CreateModel(
            name='ItensDoPedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.FloatField()),
                ('desconto', models.DecimalField(decimal_places=2, max_digits=5)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clientes.Produto')),
                ('venda', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clientes.Venda')),
            ],
        ),
    ]
