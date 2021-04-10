# Generated by Django 3.1.2 on 2021-04-10 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Question',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unweight_base', models.CharField(max_length=50)),
                ('base', models.CharField(max_length=50)),
                ('defenetely_true', models.CharField(max_length=50)),
                ('probably_true', models.CharField(max_length=50)),
                ('probably_false', models.CharField(max_length=50)),
                ('defenetely_false', models.CharField(max_length=50)),
                ('dont_know', models.CharField(max_length=50)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conspi.country')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conspi.question')),
            ],
            options={
                'verbose_name_plural': 'Answer',
            },
        ),
    ]
