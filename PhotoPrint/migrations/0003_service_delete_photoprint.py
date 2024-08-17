# Generated by Django 5.1 on 2024-08-14 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoPrint', '0002_remove_photoprint_category_remove_photoprint_tags_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='services/')),
                ('sizes', models.JSONField(default=list)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.DeleteModel(
            name='PhotoPrint',
        ),
    ]
