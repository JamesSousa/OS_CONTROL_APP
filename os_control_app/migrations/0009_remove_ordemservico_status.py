# Generated by Django 5.2 on 2025-05-05 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('os_control_app', '0008_delete_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordemservico',
            name='status',
        ),
    ]
