# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0004_auto_20180220_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='time',
            field=models.CharField(max_length=2, choices=[(b'1', b'4 pm'), (b'2', b'8 pm')]),
        ),
    ]
