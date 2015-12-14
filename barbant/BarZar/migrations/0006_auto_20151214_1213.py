# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BarZar', '0005_auto_20151214_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biere',
            name='prix',
            field=models.FloatField(default=4.99),
        ),
    ]
