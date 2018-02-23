# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0006_auto_20180220_1645'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Venu',
            new_name='Venue',
        ),
    ]
