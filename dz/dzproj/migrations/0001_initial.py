# Generated by Django 5.0.3 on 2024-03-14 13:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('adress', models.CharField(max_length=100)),
                ('regdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('descriprion', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('count', models.IntegerField()),
                ('regdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill', models.DecimalField(decimal_places=2, max_digits=8)),
                ('regdate', models.DateTimeField(auto_now_add=True)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dzproj.client')),
            ],
        ),
    ]
