# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='mainpage_rel',
            field=models.ForeignKey(to='hackathon_app.MainPage', default=1),
        ),
    ]
