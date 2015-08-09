# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20150807_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensajes',
            name='published',
            field=models.BooleanField(default=True, verbose_name='Publicado?'),
        ),
        migrations.AddField(
            model_name='mensajes',
            name='published_in',
            field=models.ForeignKey(default=True, to='blog.Entrada'),
        ),
    ]
