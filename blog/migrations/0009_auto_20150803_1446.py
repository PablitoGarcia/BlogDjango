# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_categoria_contacto_entrada_mensajes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contacto',
            options={'verbose_name': 'Contacto'},
        ),
        migrations.AlterModelOptions(
            name='mensajes',
            options={'ordering': ['-fecha'], 'verbose_name': 'Mensaje', 'verbose_name_plural': 'Todos los Comentarios'},
        ),
    ]
