# Generated by Django 4.0 on 2021-12-30 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contas_app', '0003_remove_cliente_conta_conta_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Extrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acao', models.CharField(max_length=200, null=True)),
                ('conta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contas_app.conta')),
            ],
        ),
    ]
