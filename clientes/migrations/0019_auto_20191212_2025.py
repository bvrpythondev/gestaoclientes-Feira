# Generated by Django 2.2.1 on 2019-12-12 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0018_auto_20191212_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='clients_photos'),
        ),
    ]
