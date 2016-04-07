# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='reg_time',
            field=models.DateTimeField(default=1458208929),
        ),
    ]
