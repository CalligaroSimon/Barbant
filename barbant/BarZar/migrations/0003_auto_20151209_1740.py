# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BarZar', '0002_biere_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='biere',
            name='image',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biere',
            name='populaire',
            field=models.BooleanField(default=False),
        ),
    ]
