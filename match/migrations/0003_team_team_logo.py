# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0002_remove_team_team_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_logo',
            field=models.ImageField(null=True, upload_to=b'post_images/', blank=True),
            preserve_default=True,
        ),
    ]
