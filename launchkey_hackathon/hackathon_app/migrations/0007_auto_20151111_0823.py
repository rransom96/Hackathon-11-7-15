# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon_app', '0006_auto_20151111_0820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='issue_rel',
        ),
        migrations.AddField(
            model_name='post',
            name='subissue_rel',
            field=models.ForeignKey(default=1, to='hackathon_app.SubIssue'),
        ),
        migrations.AddField(
            model_name='subissue',
            name='issue_rel',
            field=models.ForeignKey(default=1, to='hackathon_app.Issue'),
        ),
    ]
