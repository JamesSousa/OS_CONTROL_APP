# Generated by Django 5.2 on 2025-05-04 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('os_control_app', '0004_alter_ordemservico_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordemservico',
            name='status',
            field=models.CharField(choices=[('aberto', 'Aberto'), ('em_espera', 'Em espera'), ('em_atraso', 'Em atraso'), ('pausado', 'Pausado'), ('nao_atribuido', 'Não atribuído'), ('encerra_hoje', 'Encerra hoje')], max_length=40),
        ),
    ]
