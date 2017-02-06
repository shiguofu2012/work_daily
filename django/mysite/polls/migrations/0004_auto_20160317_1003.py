# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_user_reg_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='reg_time',
            field=models.BigIntegerField(default=1458208984),
        ),
    ]
