# Generated by Django 5.1 on 2024-08-15 01:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoPrint', '0006_remove_service_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='height',
        ),
        migrations.RemoveField(
            model_name='service',
            name='width',
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Ширина')),
                ('height', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Высота')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sizes', to='PhotoPrint.service', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Размер',
                'verbose_name_plural': 'Размеры',
            },
        ),
    ]
