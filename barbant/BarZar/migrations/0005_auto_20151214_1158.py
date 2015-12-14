# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BarZar', '0004_biere_prix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biere',
            name='prix',
            field=models.IntegerField(default=499),
        ),
    ]
