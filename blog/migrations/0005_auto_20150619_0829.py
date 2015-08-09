# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_mensajes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mensajes',
            options={'ordering': ['-fecha'], 'verbose_name': 'Mensaje', 'verbose_name_plural': 'Todos los mensajes'},
        ),
        migrations.AddField(
            model_name='mensajes',
            name='fecha',
            field=models.DateTimeField(default=None, verbose_name='Fecha del Mensaje', auto_now_add=True),
            preserve_default=False,
        ),
    ]
