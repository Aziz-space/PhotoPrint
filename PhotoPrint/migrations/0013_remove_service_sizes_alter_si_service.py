# Generated by Django 5.1 on 2024-08-16 12:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoPrint', '0012_remove_si_name_si_height_si_width_alter_si_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='sizes',
        ),
        migrations.AlterField(
            model_name='si',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sizes', to='PhotoPrint.service'),
        ),
    ]
