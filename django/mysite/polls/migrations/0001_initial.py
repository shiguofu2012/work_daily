# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('uid', models.AutoField(serialize=False, primary_key=True)),
                ('nickname', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
