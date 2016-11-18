# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 15:12
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(13)])),
                ('titulo', models.CharField(max_length=200)),
                ('Autor', models.CharField(max_length=200)),
                ('Editorial', models.CharField(max_length=200)),
                ('Pais', models.CharField(max_length=200)),
                ('Anio', models.DateTimeField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha_prestamo', models.DateTimeField(auto_now=True)),
                ('Fecha_devolucion', models.DateTimeField(auto_now_add=True)),
                ('Fecha_devolucionReal', models.DateTimeField()),
                ('Libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libros', to='exfinal.Libros')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_Completo', models.TextField()),
                ('Dpi', models.IntegerField(default=0)),
                ('Libros', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exfinal.Libros')),
            ],
        ),
        migrations.AddField(
            model_name='prestamo',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to='exfinal.Usuario'),
        ),
    ]
