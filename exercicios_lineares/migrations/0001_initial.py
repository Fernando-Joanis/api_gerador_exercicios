# Generated by Django 4.0.5 on 2022-06-15 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fator1', models.TextField(max_length=5)),
                ('fator2', models.TextField(max_length=5)),
                ('operador', models.TextField(max_length=1)),
            ],
            options={
                'verbose_name': 'Exercicio',
                'verbose_name_plural': 'Exercicios',
            },
        ),
    ]
