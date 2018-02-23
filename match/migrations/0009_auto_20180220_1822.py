# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0008_auto_20180220_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='time',
            field=models.CharField(max_length=2, choices=[(b'1', b'Day(4 pm)'), (b'2', b'Night(8 pm)')]),
        ),
    ]
