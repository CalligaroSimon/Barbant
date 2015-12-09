# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BarZar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='biere',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
