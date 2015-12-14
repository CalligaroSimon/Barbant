# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BarZar', '0003_auto_20151209_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='biere',
            name='prix',
            field=models.TextField(null=True),
        ),
    ]
