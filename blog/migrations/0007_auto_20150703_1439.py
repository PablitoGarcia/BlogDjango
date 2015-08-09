# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150619_0837'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contacto',
        ),
        migrations.RemoveField(
            model_name='entrada',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='entrada',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='mensajes',
            name='published_in',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Entrada',
        ),
        migrations.DeleteModel(
            name='Mensajes',
        ),
    ]
