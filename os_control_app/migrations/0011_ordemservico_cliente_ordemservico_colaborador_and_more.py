# Generated by Django 5.2 on 2025-05-06 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('os_control_app', '0010_ordemservico_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordemservico',
            name='cliente',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='ordemservico',
            name='colaborador',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='ordemservico',
            name='funcao_colaborador',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='ordemservico',
            name='obs_tarefa',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
