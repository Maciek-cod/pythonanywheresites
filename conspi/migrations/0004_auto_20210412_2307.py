# Generated by Django 3.1.2 on 2021-04-12 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conspi', '0003_auto_20210411_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]