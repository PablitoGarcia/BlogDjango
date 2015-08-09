# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_contacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensajes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('mensaje', models.TextField(verbose_name='Mensaje')),
                ('published', models.BooleanField(default=False, verbose_name='Publicado?')),
                ('published_in', models.ForeignKey(to='blog.Entrada')),
            ],
        ),
    ]
