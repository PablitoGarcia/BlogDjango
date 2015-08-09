# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20150803_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensajes',
            name='published',
        ),
        migrations.RemoveField(
            model_name='mensajes',
            name='published_in',
        ),
    ]
