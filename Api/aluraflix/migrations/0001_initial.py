# Generated by Django 4.1.1 on 2022-10-03 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('cor', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.CharField(blank=True, max_length=200)),
                ('data_lancamento', models.DateField()),
                ('url', models.URLField()),
                ('categoriaId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aluraflix.categorias')),
            ],
        ),
    ]
