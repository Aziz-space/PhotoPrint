# Generated by Django 5.1 on 2024-08-15 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoPrint', '0005_remove_service_sizes_service_height_service_width'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='description',
        ),
    ]
