# Generated by Django 4.0 on 2021-12-30 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas_app', '0004_extrato'),
    ]

    operations = [
        migrations.AddField(
            model_name='extrato',
            name='valor',
            field=models.FloatField(null=True),
        ),
    ]
