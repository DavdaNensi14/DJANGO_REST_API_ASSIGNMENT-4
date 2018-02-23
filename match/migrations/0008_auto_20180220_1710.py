# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0007_auto_20180220_1710'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='venu',
            new_name='venue',
        ),
    ]
