# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon_app', '0002_auto_20151107_2156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post_rel',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='commentupvote',
            name='comment_upvotes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='mainpage_rel',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.RemoveField(
            model_name='postupvote',
            name='post_upvotes',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='CommentUpvote',
        ),
        migrations.DeleteModel(
            name='MainPage',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='PostUpvote',
        ),
    ]
