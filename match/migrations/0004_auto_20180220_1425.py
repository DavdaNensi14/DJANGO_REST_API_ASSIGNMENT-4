# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0003_team_team_logo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favourite',
            old_name='team',
            new_name='team_name',
        ),
    ]
